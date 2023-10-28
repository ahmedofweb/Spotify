from django.contrib import admin
from .models import *

@admin.register(Qoshiqchi)
class QoshiqchiAdmin(admin.ModelAdmin):
    list_display = ['ism', 'davlat']

@admin.register(Albom)
class AlbomAdmin(admin.ModelAdmin):
    list_display = ['nom', 'qoshiqchi']


@admin.register(Qoshiq)
class QoshiqAdmin(admin.ModelAdmin):
    list_display = ['nom', 'janr']

@admin.register(Izoh)
class IzohAdmin(admin.ModelAdmin):
    list_display = ['matn']
