from django.contrib import admin

from .models import ToDoList, Task


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('name', 'description')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'todo_list', 'status', 'due_date', 'completed')
    list_editable = ('completed',)
    list_filter = ('status', 'completed')
    ordering = ('due_date',)
    
    def save_model(self, request, obj, form, change):
        if obj.completed:
            obj.status = 'Completed'
        else:
            if obj.status == 'Completed':
                obj.status = 'Pending'
        super().save_model(request, obj, form, change)
