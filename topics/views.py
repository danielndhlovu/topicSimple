from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from topics.models import ProjectTopics
from .foms import ProposeForm, EditForm


class IndexView(ListView):
    model = ProjectTopics
    template_name = 'pages/home.html'
    ordering = ['-topic_date']


class ProjectDetailsView(DetailView):
    model = ProjectTopics
    template_name = 'pages/detail/details.html'


class AddTopic(CreateView):
    model = ProjectTopics
    form_class = ProposeForm
    template_name = 'pages/propose/topic-propose.html'


class UpdateTopic(UpdateView):
    model = ProjectTopics
    form_class = EditForm
    template_name = 'pages/propose/update.html'


class DeleteTopic(DeleteView):
    model = ProjectTopics
    template_name = 'd.html'
    success_url = reverse_lazy('index')
