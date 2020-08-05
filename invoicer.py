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

rawText = getRawText('BelBrands1.pdf')
print(rawText)

#Invoice Date Regexes
invoiceANDdateRegex = re.compile(r'Invoice ?Date\n([0-9/]+)', re.IGNORECASE)
dueDateRegex = re.compile(r'Due ?Date')

invoiceRegex = re.compile(r'Invoice ?Date', re.IGNORECASE)
invoiceMO = invoiceRegex.findall(rawText)

dateRegex = re.compile(r'\d\d?/\d\d?/\d\d?')
dateMO = dateRegex.findall(rawText)

#Finding the Invoice and Due Dates
if invoiceANDdateRegex.findall(rawText):
    invoiceDateMO = invoiceANDdateRegex.findall(rawText)
    print('Invoice Date: ' + invoiceDateMO[0])
elif len(dateMO) >= 2 and invoiceMO:
    print('Invoice Date: ' + dateMO[0])
else:
    print('Invoice Date not found!')

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
