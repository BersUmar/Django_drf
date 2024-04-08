from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from lms.models import Lesson, Course
from users.models import User
from django.urls import reverse


class SubscribeTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@gmail.com", is_superuser=True, password="2648")
        self.client.force_authenticate(user=self.user)
        Course.objects.create(name='test')

    def test_retrieve_subscribe(self):
        """ Тестирование функционала работы подписки на обновления курса"""

        data = {
            "course_id": 1,
            "user": 1
        }

        response = self.client.post(
            '/subscription/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class LessonTestCase(APITestCase):
    """
    Класс для тестирования API уроков.

    Методы:
    - setUp: Подготовка тестового окружения.
    - test_create_lesson: Тест создания урока.
    - test_list_lesson: Тест вывода списка уроков.
    - test_destroy_lesson: Тест удаления урока.
    - test_update_lesson: Тест изменения урока.
    """

    def setUp(self) -> None:
        """
        Подготовка тестового окружения:
        - Получение JWT-токена для аутентификации клиента.
        """

        self.client = APIClient()

        self.user = User.objects.create(
            email="test@test.ru",
            is_staff=True,
            is_active=True,
            is_superuser=False,
        )
        self.user.set_password("test_user")
        self.user.save()

        self.course = Course.objects.create(
            name="Test_course",
            desc="Test_course",
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            name='Test_lesson',
            desc='Test_lesson',
            owner=self.user,
            course=self.course
        )

        self.client.force_authenticate(user=self.user)

    def test_list_lessons(self):
        """Тестирование вывода списка уроков"""

        response = self.client.get(
            reverse('lms:lessons-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        """Тестирование создания урока"""

        data = {
            "name": "test_lesson2",
            "desc": "test_lesson2",
            "course": 1
        }

        response = self.client.post(
            reverse('lms:lessons-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_lesson(self):
        """Тестирование изменения информации об уроке"""
        lesson = Lesson.objects.create(
            name='Test_lesson',
            desc='Test_lesson',
            owner=self.user,
            course=self.course,
            # video_link='https://www.youtube.com/'
        )

        response = self.client.patch(
            f'/Lessons/update/{lesson.id}/',
            {'desc': 'change'}
        )

        print(response.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        lesson = Lesson.objects.create(
            name='Test_lesson',
            desc='Test_lesson',
            owner=self.user,
            course=self.course
        )

        response = self.client.delete(
            f'/Lessons/delete/{lesson.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )