from django.contrib import admin
from .models import Task, SubTask, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'status',
    ]
    ordering = [
        '-status',
    ]

    # fields = [
    #     'title',
    #     'description',
    #     'status',
    # ]

    readonly_fields = [
        'deadline',
        'created_at',
        'description',
        'title',
    ]

    fieldsets = [
        (
            'Основная информация',
            {
                'fields': ['title', 'description','status',],
                'description': 'Основная информация',
                'classes': ['wide'],
            }
        ),
        (
            'Даты',
            {
                'fields': ['deadline', 'created_at'],
                'description': 'Даты',
                'classes': ['collapse'],
            }
        )
        ]


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status',
    ]
    ordering = [
        '-status',
    ]

    readonly_fields = [
        'deadline',
        'created_at',
        'description',
        'title',
    ]

    fieldsets = [
        (
            'Основная информация',
            {
                'fields': ['title', 'description','status',],
                'description': 'Основная информация',
                'classes': ['wide'],
            }
        ),
        (
            'Даты',
            {
                'fields': ['deadline', 'created_at'],
                'description': 'Даты',
                'classes': ['collapse'],
            }
        )
        ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    ordering = [
        '-name',
    ]

    readonly_fields = [
        'name',
    ]



# Register your models here.
