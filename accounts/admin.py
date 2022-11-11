from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # para mostras mas columnas dentro del admin
from .models import Account # clase cre se creo en acounsts

#campos a mostras
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')#columnas
    list_display_links = ('email', 'first_name', 'last_name')# lik sobre esos campos
    readonly_fields = ('last_login', 'date_joined') # ultimo login
    ordering = ('date_joined',)#organizas de manera acendente

    #filtro

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
#registar clase para que recinosca los usurios modelo
admin.site.register(Account, AccountAdmin)

