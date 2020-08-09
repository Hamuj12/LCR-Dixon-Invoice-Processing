from invoicer import *

def test(invoice):
    text = getRawText(invoice)
    findInvoiceAndDueDates(text)
    findAccountNumber(text)

test('BelBrands1.pdf')
