from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class ProductCategoryModel(models.Model):
    category = models.CharField(max_length = 120, unique = True, blank = False)

    def __str__(self):
        return self.category

    class Meta:
        db_table = 'product_category'
        ordering = ['-pk']

class DoughModel(models.Model):
    dough = models.CharField(max_length = 150, verbose_name = 'Entity Item Name')
    qty = models.FloatField(default = 1)

    def __str__(self):
        return self.dough

    class Meta:
        db_table = 'dough'

class DoughsLogModel(models.Model):
    STATUS_OPTION = [
        ('ADDED', 'ADD'),
        ('REMOVED', 'REMOVE')
    ]

    product = models.ForeignKey(DoughModel, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now = True)
    qty_added = models.FloatField()
    status = models.CharField(max_length = 10, choices = STATUS_OPTION)

    class Meta:
        db_table = 'doughlog'

class ProductsModel(models.Model):
    category = models.ForeignKey(ProductCategoryModel, on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 150, unique = True)
    dough = models.ForeignKey(DoughModel, blank = True, null = True, default = None, on_delete = models.SET_NULL, verbose_name = 'Entity')
    qty = models.FloatField(default = 1)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    online_price = models.DecimalField(max_digits = 10, default = 0.00, decimal_places = 2)

    class Meta:
        db_table = 'products'
        ordering = ['-pk']

class ProductsLogModel(models.Model):
    STATUS_OPTION = [
        ('ADDED', 'ADD'),
        ('REMOVED', 'REMOVE')
    ]

    product = models.ForeignKey(ProductsModel, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now = True)
    qty_added = models.IntegerField()
    status = models.CharField(max_length = 10, choices = STATUS_OPTION)

    class Meta:
        db_table = 'productlog'

def increment_invoice_number():
    from random import randint

    last_invoice = InvoiceModel.objects.all().order_by('pk').last()

    generate_order_no = f"ORDER#{randint(99999999, 9999999999)}"

    if last_invoice is not None:
        while generate_order_no == last_invoice.invoice_no:
            generate_order_no = f"ORDER#{randint(99999999, 9999999999)}"

    new_invoice_no = generate_order_no

    return str(new_invoice_no)

class InvoiceModel(models.Model):
    date = models.DateField(auto_now = True)
    invoice_no = models.CharField(max_length = 150, default = increment_invoice_number, blank = True, null = True)
    cash = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    cash_discount = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)
    discount = models.CharField(max_length = 3, default = 'N/D')
    discount_person = models.CharField(max_length = 20, default = 'N/D')
    tableno = models.CharField(max_length = 150, default = 'Not Available', blank = False, null = True)
    status = models.CharField(max_length = 150, default = 'not paid', blank = False, null = True)
    typeoforder = models.CharField(max_length = 150, default = 'resto', blank = False, null = True)

    def __str__(self):
        return self.invoice_no

    class Meta:
        db_table = 'invoice'
        ordering = ['-pk']

class OrderModel(models.Model):
    date = models.DateField(auto_now = True)
    invoice_no = models.ForeignKey(InvoiceModel, on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 150, blank = False, null = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    qty = models.FloatField(default = 1)

    class Meta:
        db_table = 'orders'
        ordering = ['-pk']


@receiver(post_save, sender = OrderModel, dispatch_uid='signals.ordermodel_removeqty')
def removeQty(sender, instance = None, created = False, **kwargs):
    product = ProductsModel.objects.get(product_name = instance.product_name)
    if product.dough != None:
        dough = DoughModel.objects.get(pk = product.dough.pk)
        dough.qty = dough.qty - (product.qty * instance.qty)
        dough.save()
    else:
        product.qty = product.qty - instance.qty
        product.save()

@receiver(post_delete, sender = OrderModel, dispatch_uid='signals.ordermodel_restockqty')
def restockQty(sender, instance, **kwargs):
    product = ProductsModel.objects.get(product_name = instance.product_name)
    if product.dough != None:
        dough = DoughModel.objects.get(pk = product.dough.pk)
        dough.qty = dough.qty + (product.qty * instance.qty)
        dough.save()
    else:
        update_qty = abs(product.qty + instance.qty)
        product.qty = update_qty
        product.save()

class ExpenseModel(models.Model):
    date = models.DateField()
    expense_title = models.CharField(max_length = 120)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    qty = models.IntegerField()

    class Meta:
        db_table = 'expense'
        ordering = ['-pk']


class TableModel(models.Model):
    table = models.CharField(max_length = 100, blank = False, null = True, unique = True, error_messages = {"unique": "Table name is already exists!"})

    class Meta:
        db_table = 'tables'

class DiscountModel(models.Model):
    discount = models.CharField(max_length = 3, blank = False, null = True, unique = True, error_messages = {"unique": "Discount is already exists!"}, verbose_name = 'Discount %')

    class Meta:
        db_table = 'discount'
