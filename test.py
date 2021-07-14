import unittest
from invoicer import *

def test(invoice, fileDir):
    # tests all regex functions and prints results

    text = getRawText(invoice, fileDir)
    findInvoiceAndDueDates(text)
    print('Account Number: ' + findAccountNumber(text))
    print('Invoice Number: ' + findInvoiceNumber(text))
    findPONumber(text)
    print('\n')


# test GRAINGER and TOYOTA invoices

test('Grainger1.pdf', 'Grainger')
test('Grainger2.pdf', 'Grainger')
test('Grainger3.pdf', 'Grainger')
test('Grainger4.pdf', 'Grainger')
test('Grainger5.pdf', 'Grainger')
test('Toyota1.pdf', 'Toyota')
