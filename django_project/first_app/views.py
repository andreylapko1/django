from django.http import HttpResponse

def hello_by_name(request, name):
    return HttpResponse(f"<h1>Hello, {name}!</h1>")