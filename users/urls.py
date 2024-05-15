from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreation, CodeView

app_name = UsersConfig.name

urlpatterns = [
    path('reg/', UserCreation.as_view(), name='reg'),
    path('code/', CodeView.as_view(), name='code')
]