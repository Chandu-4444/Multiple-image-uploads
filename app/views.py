from django.shortcuts import render

from .models import MultipleImage

def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')

        for image in images:
            MultipleImage.objects.create(images=image)
        
        
    images = MultipleImage.objects.all()
    return render(request, 'index.html', {'images': images})