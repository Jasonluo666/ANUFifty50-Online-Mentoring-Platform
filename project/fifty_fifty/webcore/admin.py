from django.contrib import admin
from .models import Profile
from .models import Xpairs
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["uniId","role","user","gender","degree_programme","degree_major","paired_with"]



admin.site.register(Profile,ProfileAdmin)
admin.site.register(Xpairs)
