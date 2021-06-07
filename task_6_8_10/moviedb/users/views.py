
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import list, detail

from .models import CustomUser


def my_login_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            redir = redirect('social:begin', backend='vk-oauth2')
            redir['Location'] += f'?next={request.path}'
            return redir
        else:
            return func(request, *args, **kwargs)
    return wrapper


def login(request):
    return render(request, 'users/templates/login.html')


class UserReviewsView(detail.DetailView):
    model = CustomUser
    template_name = 'users/templates/user_reviews.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.review_set.all()
        return context


class UsersIndexView(list.ListView):
    model = CustomUser
    template_name = 'users/templates/index.html'
    context_object_name = 'users_list'

    def get_queryset(self, **kwargs):
        context = super().get_queryset(**kwargs)
        return context.filter(is_staff=False)

class UserDetailView(detail.DetailView):
    model = CustomUser
    template_name = 'users/templates/details.html'
