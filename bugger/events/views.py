from django.views.generic import CreateView, DetailView
from .forms import EventForm
from .models import Event

class EventCreateView(CreateView):
    form_class = EventForm
    http_method_names = ['post']
    model = Event

class EventDetailView(DetailView):
    model = Event