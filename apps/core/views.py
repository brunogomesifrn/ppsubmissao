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
>>>>>>> e47dc81bd6bb72d576420a6f55955370937ed095
