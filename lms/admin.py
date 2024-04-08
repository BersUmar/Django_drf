from django.contrib import admin
from lms.models import Course, Lesson, Subscriptions


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner',)

@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course',)


@admin.register(Subscriptions)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course',)