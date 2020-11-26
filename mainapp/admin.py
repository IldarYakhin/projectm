from django.contrib import admin


from mainapp.models import License
# Register your models here.
admin.site.register(License)
admin.site.site_header = 'Project Licences admin panel'


