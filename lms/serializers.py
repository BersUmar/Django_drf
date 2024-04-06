from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source='lesson_set.all.count')
    lessons = LessonSerializer(source='lesson_set.all', many=True)

    class Meta:
        model = Course
        fields = '__all__'