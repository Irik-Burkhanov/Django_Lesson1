from django.urls import path
from application2.views import func1_app2, func2_app2, func3_app2

urlpatterns = [
    path('func1_app2/',func1_app2),
    path('func2_app2/',func2_app2),
    path('func3_app2/',func3_app2),
]