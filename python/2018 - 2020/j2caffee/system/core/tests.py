from django.test import TestCase

# Create your tests here.

def test_increment_invoice_number():
    last_invoice = 'ORDER#00001'
    
    if not last_invoice:
        return 'ORDER#0001'
    
    invoice_no = last_invoice
    invoice_int = invoice_no.split('ORDER#')[-1]

    new_invoice_int = int(invoice_int) + 1

    new_invoice_no = f"ORDER#{'0' * 3}{new_invoice_int}"
    
    return str(new_invoice_no)

print(test_increment_invoice_number())