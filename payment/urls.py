from django.urls import path
from .views import PaymeCallBackAPIView, PaymeInitializationView

urlpatterns = [
    path("", PaymeCallBackAPIView.as_view(), name="payme"),
    path("init/", PaymeInitializationView.as_view(), name="init"),
]
