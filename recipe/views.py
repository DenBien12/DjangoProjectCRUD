from django.shortcuts import render, redirect
from .models import Recipe
from django.http import HttpResponse
# Create your views here.

def recipes(request):
    if request.method == 'POST':
        data = request.POST

        image = request.FILES.get('image')
        name = data.get('name')
        description = data.get('description')

        Recipe.objects.create(
            image=image,
            name=name,
            description=description,
        )
        return redirect('/')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            recipe_name_icontains=request.GET.get('search')
        )
    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST

        image = request.FILES.get('image')
        name = request.FILES.get('name')
        description = data.get('descrition')

        queryset.name = name
        queryset.description = description

        if image:
            queryset.image = image
        
        queryset.save()

        return redirect('/')
    
    context = {'receipe': queryset}
    return render(request, 'update_receipe.html', context)