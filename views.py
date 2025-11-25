from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

def lesson_detail(request, course_id, lesson_id):
    # Здесь в будущем будет проверка оплаты
    course = get_object_or_404(Course, id=course_id)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    return render(request, 'courses/lesson.html', {'course': course, 'lesson': lesson})
