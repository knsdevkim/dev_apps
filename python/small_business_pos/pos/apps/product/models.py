from django.db import models

from apps.category.models import CategoryModel

class ProductModel(models.Model):
    fk           = models.ForeignKey(CategoryModel, on_delete = models.CASCADE, related_name = 'fk_c_rn')
    image        = models.ImageField(upload_to = 'products/', default = '', blank = True, null = True, verbose_name = 'Product Image', help_text = 'Optional')
    name         = models.CharField(max_length = 150, blank = False, null = False, unique = True, verbose_name = 'Product Name')
    local_price  = models.DecimalField(default = 0.00, max_digits = 15, decimal_places = 2, blank = False, null = False, verbose_name = 'Price')
    online_price = models.DecimalField(default = 0.00, max_digits = 15, decimal_places = 2, blank = False, null = False, verbose_name = 'Online Price', help_text = 'if applicable')
    stock        = models.PositiveIntegerField(default = 1, blank = False, null = False, verbose_name = 'Stock(s)')
    date_created = models.DateField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_products'