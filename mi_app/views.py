from django.shortcuts import render
from mi_app.models import ToyotaLegacy, Comments
from . import forms
# Create your views here.
def index(request):
    ToyotaLegacy_list = ToyotaLegacy.objects.order_by('email')
    my_context = {'interes1': "Jugar Video Juegos", 'interes2': "Ver The big Bang Theory", 'interes3': "Tomar Coffee", 'toyota': ToyotaLegacy_list}
    return render(request, 'index.html', context=my_context)
    #return HttpResponse("<h1> HOLA!!! </h1>")

#Crar un formulario para mostrar
def form_user_view(request):
    form = forms.FormUser()

    #Print(request.method)
    if request.method == 'POST':
        form = forms.FormUser(request.POST)
        if form.is_valid():
            print('VALIDADO')
            print("NAME: ", form.cleaned_data['name'])
            print("Email: ", form.cleaned_data['email'])
            print("Text: ", form.cleaned_data['text'])
            coment = Comments.objects.get_or_create(name = form.cleaned_data['name'], email = form.cleaned_data['email'], text = form.cleaned_data['text'])[0]

            coment.save()

    return render(request, 'mi_app/form_page.html', {'form': form})