from django.contrib import admin
# to dislpay image in admin 

from django.utils.html import format_html
from .models import Car

class CarAdmin(admin.ModelAdmin):

     def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-raidus: 50px;"/>'.format(object.car_photo.url))

     # change the title thumnail to photo    
     thumbnail.short_description='Car Image' 

     list_display=['id','thumbnail','car_title','city','color','model','year','body_style','fuel_type','is_featured']
     list_display_links=('id','thumbnail','car_title')
     list_editable=('is_featured',)
     search_fields=('id','car_title','city','color','body_style','fuel_type','model')
     list_filter=('city','model','body_style','fuel_type')



admin.site.register(Car,CarAdmin)
# Register your models here.


