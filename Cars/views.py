from django.shortcuts import get_object_or_404, redirect, render
from .models import Cars
# from .forms import ChangeImageForm
import os

# Create your views here.
def Home(request):
    Cars_info = Cars.objects.filter(active=True)
    params = {'Cars_information': Cars_info}
    return render(request,"home.html",params)


def ChangeImage(request,id):
    prod = Cars.objects.get(id=id)
    if request.method == "POST":
        if len(request. FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES["image"]
        prod.Brand = request.POST.get('Brand')
        prod.model_name = request.POST.get('model_name')
        prod.save()
        return redirect('/')
    context = {'prod':prod}
    return render(request, 'ChangeImage.html', context)

