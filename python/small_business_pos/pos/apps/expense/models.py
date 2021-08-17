from django.db import models

from datetime import datetime 

class ExpenseModel(models.Model):
    name         = models.CharField(max_length = 150, blank = False, null = False, verbose_name = 'Expense Item')
    cost         = models.DecimalField(max_digits = 15, decimal_places = 2, blank = False, null = False, verbose_name = 'Cost')
    qty          = models.PositiveIntegerField(default = 1, blank = False, null = False, verbose_name = 'Qty')
    date         = models.DateField(default = datetime.now, blank = False, null = False, verbose_name = 'Date')
    date_created = models.DateField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_expense'