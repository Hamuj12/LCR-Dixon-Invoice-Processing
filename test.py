import unittest
from invoicer import *

def test(invoice):
    text = getRawText(invoice)
    findInvoiceAndDueDates(text)
    findAccountNumber(text)
    findInvoiceNumber(text)

test('BelBrands1.pdf')
test('BelBrands2.pdf')
test('BelBrands3.pdf')
test('BelBrands4.pdf')
test('BelBrands5.pdf')
test('invoice.pdf')
