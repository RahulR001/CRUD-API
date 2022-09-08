from django.contrib import admin
from .models import APITodolist


# Register your models here.

class todo(admin.ModelAdmin):
    list_display = ['tasktitle', 'taskDesc']


admin.site.register(APITodolist, todo)
