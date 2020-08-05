import PyPDF4, os, re

def getRawText(pdfFile):
    text = ''
    os.chdir('c:\\users\\HM2-Laptop\\Documents')
    pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        text = text + pageObj.extractText()

    pdfFileObj.close()
    return text

def findInvoiceAndDueDates(rawText):
    #Invoice Date and Due Date Regexes
    invoiceANDdateRegex = re.compile(r'Invoice ?Date\n([0-9/]+)', re.IGNORECASE)
    dueDateRegex = re.compile(r'(Due ?Date)|(TotalAmountDueon)', re.IGNORECASE)

    invoiceRegex = re.compile(r'Invoice ?Date', re.IGNORECASE)
    invoiceMO = invoiceRegex.findall(rawText)

    dateRegex = re.compile(r'\d\d?/\d\d?/\d\d?')
    dateMO = dateRegex.findall(rawText)

    #Find the Invoice Date(s)
    if invoiceANDdateRegex.findall(rawText):
        invoiceDateMO = invoiceANDdateRegex.findall(rawText)
        print('Invoice Date: ' + invoiceDateMO[0])
    elif len(dateMO) >= 2 and invoiceMO:
        print('Invoice Date: ' + dateMO[0])
    else:
        print('Invoice Date not found!')

    #Find the Due Date(s)
    if dueDateRegex.findall(rawText) and len(dateMO) >= 2:
        print('Due Date: ' + dateMO[1])
    else:
        print('Due date not found!')

#Find Account Number and Invoice Number
def findAccountNumber(rawText):
    #Account Number Regexes
    fullAccountNumberRegex = re.compile(r'AccountNumber\n(\d+)', re.IGNORECASE)
    altAccountNumberRegex = re.compile(r'(\w+ )?Account ?Number', re.IGNORECASE)
    accountNumberRegex = re.compile(r'\d+\n')

    #Find the Account Number
    if fullAccountNumberRegex.findall(rawText):
        accountNumberMO = fullAccountNumberRegex.findall(rawText)
        print('Account Number: ' + accountNumberMO[0])
    elif altAccountNumberRegex.findall(rawText):
        print('Account Number Found')

    else:
        print('Account Number not found!')

#Test Cases
text1 = getRawText('BelBrands1.pdf')
findInvoiceAndDueDates(text1)
findAccountNumber(text1)

text2 = getRawText('BelBrands2.pdf')
findInvoiceAndDueDates(text2)
findAccountNumber(text2)

text3 = getRawText('BelBrands3.pdf')
findInvoiceAndDueDates(text3)
findAccountNumber(text3)

text4 = getRawText('BelBrands4.pdf')
findInvoiceAndDueDates(text4)
findAccountNumber(text4)

text5 = getRawText('BelBrands5.pdf')
findInvoiceAndDueDates(text5)
findAccountNumber(text5)

text6 = getRawText('invoice.pdf')
findInvoiceAndDueDates(text6)
findAccountNumber(text6)
