from api import views as api_views
from django.urls import path

urlpatterns = [
    path('user/token/', api_views.CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
]