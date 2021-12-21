import mptt

from django.db import models

from mptt.models import TreeForeignKey, MPTTModel


class Categories(MPTTModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, )

    def __str__(self):
        return self.name

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']




class Products(models.Model):
    name = models.CharField(max_length=50)
    category = TreeForeignKey(Categories, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return self.name
