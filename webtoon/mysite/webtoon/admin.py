from django.contrib import admin
from .models import Webtoon , Photo
# Register your models here.
admin.site.register(Webtoon)
admin.site.register(Photo)

class UserAdmin(admin.ModelAdmin) :
    list_display = ('username', 'password')