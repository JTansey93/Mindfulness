from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from affirmations.models import Affirmation

class UserAffirmationtListView(ListView):
    model = Affirmation
    template_name = 'affirmation-list'
    context_object_name = 'affirmations'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return Affirmation.objects.filter(author=user).order_by('-date_posted')

class AffirmationCreateView(LoginRequiredMixin, CreateView):
    '''A class based view which allows you to create posts'''

    model = Affirmation
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''A class based view which allows you to create posts'''

    model = Affirmation
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class AffirmationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''A class based view which presents a detailed view of posts'''

    model = Affirmation
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
