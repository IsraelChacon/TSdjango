from django.shortcuts import render

# Create your views here.
def index(request):
    my_context = {'interes1': "Jugar Video Juegos", 'interes2': "Ver The big Bang Theory", 'interes3': "Tomar Coffee"}
    return render(request, 'index.html', context=my_context)
    #return HttpResponse("<h1> HOLA!!! </h1>")