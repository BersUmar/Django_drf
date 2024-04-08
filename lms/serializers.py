from rest_framework import serializers
from lms.models import Course, Lesson, Subscriptions
from lms.vaidators import URLValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        # validators = [URLValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(source='lesson_set.all', many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    is_subscribe = serializers.SerializerMethodField()

    def get_is_subscribe(self, obj):
        # Получаем текущего пользователя из запроса
        user = self.context['request'].user

        for sub in Subscriptions.objects.filter(user=user, course=obj.pk):
            for user in obj.user.all():
                if sub.user == user:
                    return True
        return False

    class Meta:
        model = Subscriptions
        fields = ["course", "user"]