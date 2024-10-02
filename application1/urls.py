from django.urls import path
from application1.views import func1_app1, func2_app1, func3_app1

urlpatterns = [
    path('func1_app1/',func1_app1),
    path('func2_app1/',func2_app1),
    path('func3_app1/',func3_app1),
]