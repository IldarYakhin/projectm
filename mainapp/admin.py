from django.contrib import admin
from django.contrib.auth.models import Group
from mainapp.models import License

# Register your models here.
admin.site.site_header = 'Project Licences admin panel'


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('idlicense', 'code', 'duration', 'activated',)
    list_filter = ('activated',)
    change_list_template = ('admin/licences_admin.html')

admin.site.register(License, LicenseAdmin)
admin.site.unregister(Group)


