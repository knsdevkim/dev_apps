from django.db import models

class OrderModel(models.Model):
    order_no     = models.CharField(max_length = 250, blank = False, null = False, verbose_name = 'Order No.')
    order_type   = models.CharField(max_length = 10, default = 'local', blank = False, null = False, verbose_name = 'Order Type')
    cash         = models.DecimalField(default = 0.00, max_digits = 15, decimal_places = 2, verbose_name = 'Customer Cash')
    discount     = models.PositiveIntegerField(default = 0, blank = False, null = False, verbose_name = 'Discount %', help_text = 'if applicable')
    status       = models.CharField(max_length = 10, blank = False, null = False, verbose_name = 'Order Status')
    date_created = models.DateField(auto_now = True)

    def __str__(self):
        return self.order_no

    class Meta:
        db_table = 'tbl_orders'

class ItemOrderModel(models.Model):
    fk           = models.ForeignKey(OrderModel, on_delete = models.CASCADE, related_name = 'fk_o_rn')
    product_name = models.CharField(max_length = 150, blank = False, null = False)
    price        = models.DecimalField(max_digits = 15, decimal_places = 2)
    qty          = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return f'{self.fk} - {self.product_name}'

    class Meta:
        db_table = 'tbl_item_orders'