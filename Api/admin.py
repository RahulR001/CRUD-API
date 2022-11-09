from django.contrib import admin
from .models import APITodolist


# ========== class-to-create-adminpage-detailed-view ==========

class todo(admin.ModelAdmin):
    list_display = ['tasktitle', 'taskDesc']

admin.site.register(APITodolist, todo)
