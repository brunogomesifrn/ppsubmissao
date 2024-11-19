from django.shortcuts import render

def home(request):
<<<<<<< HEAD
    return render(request, 'index.html'),
def contato(request):
   return render(request,  'contato.html')
=======
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')
<<<<<<< HEAD

def perfil(request):
    return render(request, 'perfil.html')
=======
>>>>>>> e47dc81bd6bb72d576420a6f55955370937ed095
>>>>>>> 709a91b606ec96f4683e9019238efd6accfa6d3f
