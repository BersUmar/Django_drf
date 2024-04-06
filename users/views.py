from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer
from rest_framework.filters import OrderingFilter


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson')
    ordering_fields = ('date_of_payment',)


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer