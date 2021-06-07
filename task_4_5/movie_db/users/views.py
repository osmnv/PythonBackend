
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views import generic
from django.shortcuts import render, redirect

from application import generic_views
from .models import User
from .forms import AddUserForm


class IndexView(generic.ListView):
    template_name = 'templates/users/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.all()


class DetailView(generic_views.JsonDetailView):
    model = User

@require_http_methods(["GET", "POST"])
def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('users:index')
    else:
        form = AddUserForm()
        return render(request, 'templates/users/add_user.html', {'form': form})
