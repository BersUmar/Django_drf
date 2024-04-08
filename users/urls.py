from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentsListAPIView, PaymentsCreateAPIView, UserListAPIView, UserCreateAPIView, \
    UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, MyTokenObtainPairView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('users_create/', UserCreateAPIView.as_view(), name='users-create'),
    path('users_retrieve/<int:pk>/', UserRetrieveAPIView.as_view(), name='users-get'),
    path('users_update/<int:pk>/', UserUpdateAPIView.as_view(), name='users-update'),
    path('users_delete/<int:pk>/', UserDestroyAPIView.as_view(), name='users-delete'),
    path('users_list', UserListAPIView.as_view(), name='users-list'),

    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
    path('payments/create', PaymentsCreateAPIView.as_view(), name='payments-create'),
]