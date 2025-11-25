from django.contrib import admin
from .models import Course, Lesson

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline] # Позволяет добавлять уроки прямо внутри курса
    list_display = ('title', 'price', 'created_at')
