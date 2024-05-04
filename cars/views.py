from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Cars, Category


# Create your views here.
def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)


def get_cars(request, pk):
    cars = Cars.objects.filter(category=pk)
    context = {
        'cars': cars
    }
    return render(request, 'cars.html', context=context)


def detail(request, pk):
    car = Cars.objects.get(pk=pk)
    context = {
        'car': car
    }
    return render(request, 'detail.html', context=context)


def add_cars(request):
    form = CarForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cars:get_info')
    context = {
        'form': form
    }
    return render(request, 'create.html', context=context)


def update_cars(request, pk):
    data = Cars.objects.get(pk=pk)
    form = CarForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('cars:get_info')
    context = {
        'form': form
    }
    return render(request, 'update.html', context=context)
