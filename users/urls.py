from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentsListAPIView, UserListAPIView, PaymentsCreateAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
    path('users_list/', UserListAPIView.as_view(), name='users-list'),
    path('payments/create', PaymentsCreateAPIView.as_view(), name='payments-create'),
]