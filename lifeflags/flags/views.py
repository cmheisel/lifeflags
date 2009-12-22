from django.http import HttpResponse

def show(request, slug):
    return HttpResponse("Yo mo fo")
