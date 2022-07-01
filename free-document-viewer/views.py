from django.shortcuts import render
from .django_app import Analysis,descriptive

def home(request):
    if request.method == 'POST':
        file = request.FILES['file']

        with open(f"{file}",'wb') as f:
            f.write(file.read())

        data = Analysis(f"{file}")
        desc = descriptive(data=data)

        return render(request, 'home/index.html',{"data":data.to_html(),"desc":desc.to_html()})
    
    return render(request, 'home/index.html')