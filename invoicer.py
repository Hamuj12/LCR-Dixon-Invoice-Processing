import PyPDF4
import os
import re


# parses through the pdf file and outputs raw text

def getRawText(pdfFile, pdfDir):
    text = ''
    os.chdir('c:\\users\\HM2-Laptop\\Documents\\Invoice tests\\Bel Brands Invoices\\' + pdfDir)
    pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        text = text + pageObj.extractText()

    pdfFileObj.close()
    return text


# find the invoice date and due date

def findInvoiceAndDueDates(rawText):

    # Invoice Date and Due Date Regexes

    invoiceANDdateRegex = re.compile(r'Invoice ?Date\n([0-9/]+)', re.IGNORECASE)
    dueDateRegex = re.compile(r'(Due ?Date)|(TotalAmountDueon)', re.IGNORECASE)

    invoiceRegex = re.compile(r'Invoice ?Date', re.IGNORECASE)
    invoiceMO = invoiceRegex.findall(rawText)

    dateRegex = re.compile(r'\d\d?/\d\d?/\d\d?')
    dateMO = dateRegex.findall(rawText)

    # Find the Invoice Date(s) if they are listed after "Invoice Date"

    if invoiceANDdateRegex.findall(rawText):
        invoiceDateMO = invoiceANDdateRegex.findall(rawText)
        print ('Invoice Date: ' + invoiceDateMO[0])
    elif len(dateMO) >= 2 and invoiceMO:

    # Find the invoice date(s) if they are not listed with their respective dates

        print ('Invoice Date: ' + dateMO[0])
    else:
        print ('Invoice Date not found!')

    # Find the Due Date(s)

    if dueDateRegex.findall(rawText) and len(dateMO) >= 2:
        print ('Due Date: ' + dateMO[1])
    else:
        print ('Due date not found!')


# Find the Account Number

def findAccountNumber(rawText):

    # Account Number Regexes

    fullAccountNumberRegex = re.compile(r'Account ?Number\n(\d+)', re.IGNORECASE)

    accountNumFollowedByInvoiceNumExistsRegex = re.compile(r'(\w+ )?Account ?Number\n(?=(Invoice ?Number)\n)', re.IGNORECASE)
    accountNumberRegex = re.compile(r'(^\d{8,10}\n$)')

    # Find the Account Number if it is listed after "Account number"

    if fullAccountNumberRegex.findall(rawText):
        accountNumberMO = fullAccountNumberRegex.findall(rawText)
        acctNumber = accountNumberMO[0]
    elif accountNumFollowedByInvoiceNumExistsRegex.findall(rawText):

    # Find the account number if account number and invoice numbers exist but are not listed with their respective numbers

        altAccountNumMO = accountNumberRegex.findall(rawText)
        acctNumber = altAccountNumMO
    else:
        print ('Account Number not found!')

    return str(acctNumber)


# Find the invoice numbers

def findInvoiceNumber(rawText):

    # invoice number Regexes

    invoiceNumberRegex = re.compile(r'Invoice ?Number\n(\d+)', re.IGNORECASE)

    # find the invoice numbers

    if invoiceNumberRegex.findall(rawText):
        invoiceNumberMO = invoiceNumberRegex.findall(rawText)
        invNumber = invoiceNumberMO[0]
    else:
        print ('Invoice Number not found!')

    return str(invNumber)


# Find the PO number(s)

def findPONumber(rawText):

    # PO Number Regexes

    fullPONumberRegex = re.compile(r'P.?O.? ?Number:?\n(\d+)', re.IGNORECASE)

    poNumberFollowedByWordsNotPONumberRegex = re.compile(r'\b(P.?O.? ?Number:?(\n)?[a-zA-Z]+-?[a-zA-Z]+\n?[a-zA-Z]+\n?[0-9]+)\b', re.IGNORECASE)
    poNumberRegex = re.compile(r'(\b\d{8,10}\b)')

    # find the PO number(s) if listed after "PO Number"

    if fullPONumberRegex.findall(rawText):
        poNumberMO = fullPONumberRegex.findall(rawText)
        print ('PO Number: ' + poNumberMO[0])

    elif poNumberFollowedByWordsNotPONumberRegex.findall(rawText):
        # find the PO Number(s) if numbers are not listed after the identifier

        altPONumberMO = poNumberRegex.findall(rawText)

        # remove duplicate numbers

        removeInvNumbers(rawText, altPONumberMO)
        removeAcctNumbers(rawText, altPONumberMO)
        removeBillNumbers(rawText, altPONumberMO)
        removeBillNumbers(rawText, altPONumberMO)

        print ('PO Number: ' + altPONumberMO[1])
        return altPONumberMO
    else:
        print ('PO Number not found!')


def findBillingNumber(rawText):

    # billing number Regexes

    billingNumberRegex = re.compile(r'Billing ?Number\n(\d+)', re.IGNORECASE)

    # find the billing numbers

    if billingNumberRegex.findall(rawText):
        billingNumberMO = billingNumberRegex.findall(rawText)
        billNumber = billingNumberMO[0]
    else:
        print ('Billing Number not found!')

    return billNumber


def removeAcctNumbers(text, numberList):
    #removes duplicate account numbers from match object lists

    for numbers in numberList:
        if numbers == findAccountNumber(text):
            numberList.remove(numbers)

    return numberList


def removeInvNumbers(text, numberList):
    #removes duplicate invoice numbers from match object lists

    for numbers in numberList:
        if numbers == findInvoiceNumber(text):
            numberList.remove(numbers)

    return numberList


def removeBillNumbers(text, numberList):
    #removes duplicate billing numbers from match object lists

    for numbers in numberList:
        if numbers == findBillingNumber(text):
            numberList.remove(numbers)

    return numberList
