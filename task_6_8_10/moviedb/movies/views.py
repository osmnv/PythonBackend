
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import list, detail, edit

from .models import Movie, Review
from .tasks import new_movie


class MovieIndexView(list.ListView):
    model = Movie
    context_object_name = 'movies_list'
    template_name = 'movies/templates/movies_index.html'

    def get_queryset(self):
        movies = self.model.objects.all()
        search_query = self.request.GET.get('search_query')
        if search_query is not None:
            movies = movies.filter(title__icontains=search_query)
        return movies


class MovieDetailView(detail.DetailView):
    model = Movie
    template_name = 'movies/templates/movie_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.review_set.all()
        return context


class MovieAddView(edit.CreateView):
    model = Movie
    fields = ['title', 'rel_date', 'producer', 'descr', 'genres', 'poster']
    template_name = 'movies/templates/movie_add.html'

    def form_valid(self, form):
        self.object = form.save()
        new_movie.delay(
            form.cleaned_data['title'],
            self.request.user.username
        )
        return HttpResponseRedirect(self.get_success_url())


class MovieEditView(edit.UpdateView):
    model = Movie
    fields = ['title', 'rel_date', 'producer', 'descr', 'genres', 'poster']
    template_name = 'movies/templates/movie_edit.html'


class MovieDeleteView(edit.DeleteView):
    model = Movie
    template_name_suffix = None
    success_url = reverse_lazy('movies:movies_index')


class ReviewAddView(edit.CreateView):
    model = Review
    fields = ('text',)
    template_name = 'movies/templates/review_add.html'

    def form_valid(self, form):
        review = form.save(commit=False)
        review.user = self.request.user
        review.movie = get_object_or_404(Movie, id=self.kwargs['pk'])
        review.save()
        self.success_url = review.movie.get_absolute_url()
        return super().form_valid(form)