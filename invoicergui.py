import PySimpleGUI as sg
import os.path
from invoicer import *

def testCases(invoice):
    # tests all regex functions and prints results

    text = getRawText(invoice)
    dateList = findInvoiceAndDueDates(text)
    accountNumber = findAccountNumber(text)
    invoiceNumber = findInvoiceNumber(text)
    PONumber = findPONumber(text)

    results = "Inovice date: " + dateList[0] + "\nDue date: " + dateList[1] + "\nAccount number: " + accountNumber + "\nInvoice number: " + invoiceNumber + "\nPO number: " + PONumber
    print(results)
    return results


file_list_column = [
    [
        sg.Text("Invoice Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20), key="-FILE LIST-"
        )
    ],
]

file_viewer_column = [
    [sg.Text("Choose a document from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Multiline(size=(40, 5), key="-RESULT-")],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(file_viewer_column),
    ]
]

window = sg.Window("Invoice Viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith((".pdf"))
        ]    
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":
        try:
            
            os.chdir(os.path.abspath(folder))
            filename = values["-FILE LIST-"][0]
            window["-TOUT-"].update(filename)
            window["-RESULT-"].update(testCases(filename))
        except:
            window["-RESULT-"].print("File not found")

window.close()

