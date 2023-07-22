from django.contrib import admin

from contacts.models import Contact

class ContactAdmin(admin.ModelAdmin):

    list_display= ('id','first_name','last_name','email','car_title','city','create_date')
    list_display_links=('id','first_name','last_name')
    list_per_page=25
admin.site.register(Contact,ContactAdmin)
# Register your models here.
