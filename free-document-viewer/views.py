import shutil
from django.shortcuts import render
from .django_app import Analysis
from django.utils.datastructures import MultiValueDictKeyError
import os


def home(request):
    if request.method == 'POST':
        try:
            file = request.FILES['file']
            
            # Checking if the directory exists and if it doesn't it creates it.
            if os.path.isdir('df') == True:
                pass
            else:
                os.mkdir('df')

            # Opening the file and writing the file to the directory.
            with open(f"df/{file}", 'wb') as f:
                f.write(file.read())

            data = Analysis(f"df/{file}")

            return render(request, 'home/index.html', {"data": data.to_html()})

        # This is a try/except block. It is trying to get the file from the request. If it fails, it
        # will return the error message.
        except MultiValueDictKeyError:
            return render(request, 'home/index.html', {"data": "<h3>No file found.</h3>"})
        except:
            return render(request, 'home/index.html', {"data": "<h3>Some error. App is in early development...</h3>"})
    # Trying to delete the directory. If it fails, it will pass.
    try:
        shutil.rmtree('./df')
    except FileNotFoundError:
        pass
    return render(request, 'home/index.html')
