from django.contrib import admin

from .models import Team
# to dislpay image in admin 

from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-raidus: 50px;">'.format(object.photo.url))

     # change the title thumnail to photo    
    thumbnail.short_description='photo'  

    list_display=['id','thumbnail','first_name','designation','created_date']
    list_display_links=['id',"thumbnail","first_name"]
    search_fields=['first_name','last_name','designation']
    list_filter=('designation',)

admin.site.register(Team,TeamAdmin)
# Register your models here.
