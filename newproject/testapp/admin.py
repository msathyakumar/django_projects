from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.person),
admin.site.register(models.Family),
admin.site.register(models.Person_shirts),
admin.site.register(models.school_student),
admin.site.register(models.Article),
admin.site.register(models.Reporter),