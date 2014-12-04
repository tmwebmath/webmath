from django.shortcuts import render

def index(request):
    #pages = Page.objects.all()
    return render(request, "courses/courses.html", locals())

