from django.shortcuts import render
from django.http import HttpResponse
from .forms import HouseForm


def predict(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house_instance = form.save(commit=False)
            pred = house_instance.predict_model()
            
            if pred != 0:
                return render(request, 'predict.html', {'house_instance': house_instance, 'pred': int(pred)})
            else:
                return HttpResponse("The Input is not Correct")
    else:
        form = HouseForm()

    return render(request, 'predict.html', {'form': form})