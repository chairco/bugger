#  buglists/views.py
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.http import Http404

#from events.forms import EventForm

from .models import Buglist, Tracker

from .forms import BuglistForm, TrackerForm, BuglistFormSet


class FormsetMixin(object):
    object = None

    def get(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def get_formset_class(self):
        return self.formset_class

    def get_formset(self, formset_class):
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {
            'instance': self.object
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form, formset):
        buglist = form.save(commit=False)
        if self.request.user.is_authenticated():
            buglist.owner = self.request.user
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return redirect(self.object.get_absolute_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class BuglistCreateView(FormsetMixin, CreateView):
    template_name = 'buglists/buglist_formset.html'
    model = Buglist
    form_class = BuglistForm
    formset_class = BuglistFormSet


class BuglistUpdateView(FormsetMixin, UpdateView):
    from django.http import Http404
    is_update_view = True
    template_name = 'buglists/buglist_formset.html'
    model = Buglist
    form_class = BuglistForm
    formset_class = BuglistFormSet

    #@method_decorator(permission_required('buglists.delete_buglist', login_url='/accounts/login/'))
    #def dispatch(self, *args, **kwargs):
    #    return super(BuglistUpdateView, self).dispatch(*args, **kwargs)

class BuglistList(ListView):

    model = Buglist


class BuglistDetail(DetailView):

    model = Buglist


class BuglistTracker(CreateView):
    template_name = 'buglists/buglist_tracker.html'
    form_class = TrackerForm
    model = Tracker

    def form_valid(self, form):
        tracker = form.save(commit=False)
        if self.request.user.is_authenticated():
            tracker.owner = self.request.user
        form.save()
        return super(BuglistTracker, self).form_valid(form)
        


def buglist_detail(request, pk):
    try:
        buglist = Buglist.objects.get(pk=pk)
    except Buglist.DoesNotExist:
        raise Http404
    #event_form = EventForm(initial={'buglist': buglist}, submit_title='建立追蹤')
    #event_form.helper.form_action = reverse('event_create')
    event_form = TrackerForm(initial={'buglist': buglist}, submit_title='建立追蹤')
    event_form.helper.form_action = reverse('buglist_tracker')
    return render(request, 'buglists/buglist_detail.html', {
        'object': buglist, 'event_form': event_form,
    })
