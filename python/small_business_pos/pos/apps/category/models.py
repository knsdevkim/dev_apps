from django.db import models

class CategoryModel(models.Model):
    name         = models.CharField(max_length = 150, blank = False, null = False, unique = True, verbose_name = 'Category Name')
    date_created = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_product_category'