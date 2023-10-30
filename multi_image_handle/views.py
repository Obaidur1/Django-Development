from django.shortcuts import render
from .models import Property, PropertyImages

import time


# Create your views here.
# 35% more efficient then lower one
def add_property_view(request):
    if request.method == "POST":
        start_time = time.time()
        name = request.POST.get("name")
        price = request.POST.get("price")
        property = Property.objects.create(name=name, price=price)
        print(name, price)
        images = request.FILES.getlist("images")
        property_images = [
            PropertyImages(property=property, image=image) for image in images
        ]
        if property_images:
            PropertyImages.objects.bulk_create(property_images)
        execution_time = time.time() - start_time
        print(f"Execution time: {execution_time} seconds")
    data = Property.objects.all()
    return render(request, "add_property.html", {"data": data})


def add_property_view2(request):
    if request.method == "POST":
        start_time = time.time()
        name = request.POST.get("name")
        price = request.POST.get("price")
        property = Property.objects.create(name=name, price=price)
        print(name, price)
        images = request.FILES.getlist("images")
        for image in images:
            PropertyImages.objects.create(property=property, image=image)
        execution_time = time.time() - start_time
        print(f"Execution time: {execution_time} seconds")
    data = Property.objects.all()
    return render(request, "add_property.html", {"data": data})
