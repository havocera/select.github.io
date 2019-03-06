from django.contrib import admin

from .models import Area, Set
# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    pass

class SetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Area,AreaAdmin)
admin.site.register(Set,SetAdmin)


