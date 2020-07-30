from django.contrib import admin
from .models import Language,Framework,car,manufacturer

class LanguageAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Language,LanguageAdmin)
admin.site.register(Framework)
admin.site.register(car)
admin.site.register(manufacturer)

