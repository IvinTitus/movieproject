from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Movie
from .forms import Movieform
from django.views.generic import ListView, DetailView,CreateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.


#def home(request):
#    k = Movie.objects.all()
#    return render(request, "home.html", {'m': k})

class MovieList(ListView):  #displays all objects/records retieving from a model
    model=Movie
    template_name="home.html"
    context_object_name="m"

# def addmovie(request):
#     if (request.method == "POST"):
#         t = request.POST['t']
#         d = request.POST['d']
#         y = request.POST['y']
#         i = request.FILES['i']
#         m = Movie.objects.create(title=t, desc=d, year=y , image=i)
#         m.save()
#         return home(request)
#     return render(request, "addmovie.html" )

class Movieadd(CreateView):
    model=Movie
    template_name="addmovie.html"
    fields="__all__"
    success_url=reverse_lazy('film:home')



#def moviedetails(request, p):
#    d = Movie.objects.get(id=p)
#    return render(request, "moviedetails.html", {'d': d})

class MovieDetail(DetailView):
    model=Movie
    template_name="moviedetails.html"
    context_object_name="d"

# class Moviedelete(DetailView):
    # model=Movie
    # success_url=reverse_lazy('movieapp:index')
    # template_name='delete.html'

def movieedit(request, p):
    movie = get_object_or_404(Movie, id=p)

    if request.method == "POST":
        form = Movieform(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return render(request, "moviedetails.html", {'d': movie})
    else:
        form = Movieform(instance=movie)

    return render(request, "editmovie.html", {"form": form})


def deletemovie(request, p):
    movie = Movie.objects.get(id=p)
    movie.delete()
    return render(request,"home.html") # Redirect to the home page or any other desired page


