from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Employs)
class EmploysAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'employ_id', 'name', 'sex', 'job', 'position'
    )


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'employ_id', 'reason', 'date', 'days', 'money',
    )


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'employ_id', 'reason', 'date', 'money'
    )


@admin.register(Punish)
class PunishAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'employ_id', 'reason', 'date', 'money'
    )


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'employ_id', 'pay_type', 'car_number'
    )


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'employ_id', 'pay_type', 'base_salary', 'date',
        'total_punish', 'total_prize', 'total_salary'
    )
