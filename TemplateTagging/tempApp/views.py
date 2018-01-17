from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'tempApp/index.html')

def relative(request):
    return render(request,'tempApp/relative_url_templates.html')


def other(request):
    return render(request,'tempApp/other.html')    
