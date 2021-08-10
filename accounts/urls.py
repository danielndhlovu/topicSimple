from django.urls import path
from .views import StudentViewReg

urlpatterns = [
    path('signup/', StudentViewReg.as_view(), name='sign_up'),

]
