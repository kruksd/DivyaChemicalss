from django.contrib import admin
from numpy import product

from divyaChemicalsWebsite.models import blogPage, divyaProducts, downloadModel;  

# Register your models here.
admin.site.register(blogPage)
admin.site.register(divyaProducts)
admin.site.register(downloadModel)
