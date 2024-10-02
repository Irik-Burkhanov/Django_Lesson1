from django.urls import path
from application3.views import func1_app3, func2_app3, func3_app3

urlpatterns = [
    path('func1_app3/',func1_app3),
    path('func2_app3/',func2_app3),
    path('func3_app2/',func3_app3),
]