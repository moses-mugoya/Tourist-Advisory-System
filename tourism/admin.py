from django.contrib import admin
from . models import Destinations, Expenses


class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'modified', 'charges']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Destinations, DestinationAdmin)


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['tour_start_date', 'tour_end_date', 'destination', 'amount_to_spend', 'number_of_people', 'user']


admin.site.register(Expenses, ExpenseAdmin)



