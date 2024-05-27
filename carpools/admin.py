from django.contrib import admin
from .models import Carpool, CompletedCarpool, Caution

@admin.register(Carpool)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_num', 'title', 'type', 'content', 'created_at', 'end_carpool')

@admin.register(CompletedCarpool)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'post_num', 'host_name', 'carpool_date', 'created_at')

@admin.register(Caution)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')

