<<<<<<< HEAD
from invoicer import *

def test(invoice):
    text = getRawText(invoice)
    findInvoiceAndDueDates(text)
    findAccountNumber(text)

test('BelBrands1.pdf')
=======
from invoicer import *

def test(invoice):
    text = getRawText(invoice)
    findInvoiceAndDueDates(text)
    findAccountNumber(text)

test('BelBrands1.pdf')
>>>>>>> 4eee32d72d5fe004cbb72f9489542bdb605bd026
