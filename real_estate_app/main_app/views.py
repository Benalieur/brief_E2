from django.shortcuts import render
from django.http import HttpResponse
from .forms import HouseForm

def index(request):
    return render(request, 'index.html')

def result(request):
    return render(request, 'result.html')

def predict(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house_instance = form.save(commit=False)  # Crée l'instance sans la sauvegarder en base de données pour l'instant
            
            pred = house_instance.predict_model()

            if pred != 0:
                return render(request, 'result.html', {'data': int(pred)})
            else:
                return HttpResponse("The Input is not Correct")
    else:
        form = HouseForm()

        return render(request, 'index.html', {'form': form})