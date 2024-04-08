from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from lms.models import Course, Lesson, Subscriptions
from lms.paginators import CoursePagination, LessonPagination
from lms.permissions import IsStaff, IsOwner
from lms.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from django.http import Http404, HttpResponseRedirect

from users.serializers import UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CoursePagination

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwner | IsStaff, IsAuthenticated]
        elif self.action == 'update':
            self.permission_classes = [IsOwner | IsStaff, IsAuthenticated]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]


class SubscriptionView(APIView):
    queryset = Course.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = request.data.get('course_id')

        if course_id is None:
            return Response({"message": "Отсутствует идентификатор курса в запросе"}, status=400)

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise Http404("Курс с таким идентификатором не найден")

        subs_item = Subscriptions.objects.filter(user=user, course=course)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка на курс удалена'
        else:
            Subscriptions.objects.create(user=user, course=course)
            message = 'Подписка на курс добавлена'

        return Response({"message": message})


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsStaff]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff, IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]