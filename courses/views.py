from django.shortcuts import render

def index(request):
    #pages = Page.objects.all()
    return render(request, "courses/index.html", locals())

