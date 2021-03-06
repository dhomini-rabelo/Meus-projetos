from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SlugField)



class Category(Model):
    name = CharField(verbose_name='Nome', max_length=128)
    slug = SlugField(verbose_name='Url', max_length=256)
    img = ImageField(verbose_name='Img', upload_to='categories/%Y/%m/%d')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

