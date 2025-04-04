from django.contrib import admin

from users.models import User

from carts.admin import CartTabAdmin

from orders.admin import OrderTabulareAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "last_name", "first_name", "email",]
    search_fields = ["username", "last_name", "first_name", "email",]

    inlines = [CartTabAdmin, OrderTabulareAdmin]





