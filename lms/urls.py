from django.urls import path
from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter
from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, SubscriptionView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'Course', CourseViewSet, basename='course')

urlpatterns = [
                  path('Lessons/create/', LessonCreateAPIView.as_view(), name='lessons-create'),
                  path('Lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons-get'),
                  path('Lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lessons-update'),
                  path('Lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lessons-delete'),
                  path('Lessons_list/', LessonListAPIView.as_view(), name='lessons-list'),
                  path('subscription/', SubscriptionView.as_view(), name='Subscription')
              ] + router.urls
