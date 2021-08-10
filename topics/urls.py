from django.urls import path
from .views import IndexView, ProjectDetailsView, AddTopic, UpdateTopic, DeleteTopic

urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('detail/<int:pk>', ProjectDetailsView.as_view(), name='details'),
   path('suggets_topic/', AddTopic.as_view(), name='proposed'),
   path('updateTopic/edit/<int:pk>', UpdateTopic.as_view(), name='update_Topic'),
   path('Topic/<int:pk>/delete', DeleteTopic.as_view(), name='delete_topic'),
]
