
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.generic import ListView
from django.core import serializers
from django.shortcuts import render, redirect

from application import generic_views
from .models import Movie, Review
from .forms import AddReviewForm, AddMovieForm


class IndexView(ListView):
    template_name = 'templates/movies/index.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return Movie.objects.all()


class DetailView(generic_views.JsonDetailView):
    model = Movie


@require_http_methods(["GET", "POST"])
def add_movie(request):
    if request.method == "POST":
        form = AddMovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            movie.save()
            return redirect('movies:index')
    else:
        form = AddMovieForm()
        return render(request, 'templates/movies/add_movie.html', {'form': form})

@require_GET
def reviews(request, pk):
    try:
        reviews = Review.objects.filter(movie_id=pk)
        data = serializers.serialize("json", reviews, fields=('user_id', 'date', 'movie_id', 'text'), indent=4)
        return HttpResponse(data, content_type="application/json")
    except Review.DoesNotExist:
        raise Http404('No reviews available')

@require_http_methods(["GET", "POST"])
def add_review(request, pk):
    if request.method == "POST":
        form = AddReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie_id = Movie.objects.get(id=pk)
            review.save()
            return redirect('movies:reviews', pk=pk)
    else:
        form = AddReviewForm()
        return render(request, 'templates/movies/add_review.html', {'form': form})
        
