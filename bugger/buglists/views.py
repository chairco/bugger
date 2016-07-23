#  buglists/views.py
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

from .models import Buglist

from .forms import BuglistForm

class BuglistCreateView(CreateView):
    template_name = 'buglists/buglist_formset.html'
    form_class = BuglistForm
    model = Buglist


class BuglistUpdateView(UpdateView):
    from django.http import Http404
    template_name = 'buglists/buglist_formset.html'
    is_update_view = True
    model = Buglist
    form_class = BuglistForm

    #@method_decorator(permission_required('buglists.delete_buglist', login_url='/accounts/login/'))
    #def dispatch(self, *args, **kwargs):
    #    return super(BuglistUpdateView, self).dispatch(*args, **kwargs)

class BuglistList(ListView):

    model = Buglist


class BuglistDetail(DetailView):

    model = Buglist