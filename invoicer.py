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

    #Finding the Invoice Date(s)
    if invoiceANDdateRegex.findall(rawText):
        invoiceDateMO = invoiceANDdateRegex.findall(rawText)
        print('Invoice Date: ' + invoiceDateMO[0])
    elif len(dateMO) >= 2 and invoiceMO:
        print('Invoice Date: ' + dateMO[0])
    else:
        print('Invoice Date not found!')

    #Finding the Due Date(s)
    if dueDateRegex.findall(rawText) and len(dateMO) >= 2:
        print('Due Date: ' + dateMO[1])
    else:
        print('Due date not found!')

#Test Cases
text1 = getRawText('BelBrands1.pdf')
findInvoiceAndDueDates(text1)

text2 = getRawText('BelBrands2.pdf')
findInvoiceAndDueDates(text2)

text3 = getRawText('BelBrands3.pdf')
findInvoiceAndDueDates(text3)

text4 = getRawText('BelBrands4.pdf')
findInvoiceAndDueDates(text4)

text5 = getRawText('BelBrands5.pdf')
findInvoiceAndDueDates(text5)

text6 = getRawText('invoice.pdf')
findInvoiceAndDueDates(text6)

# invoiceNumberRegex = re.compile(r'InvoiceNumber\n(\d+)')
# mo = invoiceNumberRegex.findall(text)
# print('Invoice Number: ' + mo[0])
#
# accountNumberRegex = re.compile(r'AccountNumber\n(\d+)')
# mo = accountNumberRegex.findall(text)
# print('Account Number: ' + mo[0])
#
# billingNumberRegex = re.compile(r'BillingNumber\n(\d+)')
# mo = billingNumberRegex.findall(text)
# print('Billing Number: ' + mo[0])
