import PyPDF4, os, re

#parses through the pdf and outputs raw text
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

#find the invoice and due dates
def findInvoiceAndDueDates(rawText):
    #Invoice Date and Due Date Regexes
    invoiceANDdateRegex = re.compile(r'Invoice ?Date\n([0-9/]+)', re.IGNORECASE)
    dueDateRegex = re.compile(r'(Due ?Date)|(TotalAmountDueon)', re.IGNORECASE)

    invoiceRegex = re.compile(r'Invoice ?Date', re.IGNORECASE)
    invoiceMO = invoiceRegex.findall(rawText)

    dateRegex = re.compile(r'\d\d?/\d\d?/\d\d?')
    dateMO = dateRegex.findall(rawText)

    #Find the Invoice Date(s) if they are listed after "Invoice Date"
    if invoiceANDdateRegex.findall(rawText):
        invoiceDateMO = invoiceANDdateRegex.findall(rawText)
        print('Invoice Date: ' + invoiceDateMO[0])
    #Find the invoice date(s) if they are not listed with their respective dates
    elif len(dateMO) >= 2 and invoiceMO:
        print('Invoice Date: ' + dateMO[0])
    else:
        print('Invoice Date not found!')

    #Find the Due Date(s)
    if dueDateRegex.findall(rawText) and len(dateMO) >= 2:
        print('Due Date: ' + dateMO[1])
    else:
        print('Due date not found!')

#Find the Account Number
def findAccountNumber(rawText):
    #Account Number Regexes
    fullAccountNumberRegex = re.compile(r'Account ?Number\n(\d+)', re.IGNORECASE)

    accountNumFollowedByInvoiceNumExistsRegex = re.compile(r'(\w+ )?Account ?Number\n(?=(Invoice ?Number)\n)', re.IGNORECASE)
    accountNumberRegex = re.compile(r'(^\d{8,10}\n$)')

    #Find the Account Number if it is listed after "Account number"
    if fullAccountNumberRegex.findall(rawText):
        accountNumberMO = fullAccountNumberRegex.findall(rawText)
        print('Account Number: ' + accountNumberMO[0])
    #Find the account number if account number and invoice numbers exist but are not listed with their respective numbers
    elif accountNumFollowedByInvoiceNumExistsRegex.findall(rawText):
        altAccountNumMO = accountNumberRegex.findall(rawText)
        print('Account Number: ' + altAccountNumMO)
    else:
        print('Account Number not found!')

#Find the invoice numbers
def findInvoiceNumber(rawText):
    #invoice number Regexes
    invoiceNumberRegex = re.compile(r'Invoice ?Number\n(\d+)', re.IGNORECASE)

    #find the invoice numbers
    if invoiceNumberRegex.findall(rawText):
        invoiceNumberMO = invoiceNumberRegex.findall(rawText)
        print('Invoice Number: ' + invoiceNumberMO[0] + '\n')
    else:
        print('Invoice Number not found!')
