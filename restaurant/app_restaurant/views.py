from django.shortcuts import render, redirect
from .forms import RestaurantForm, SearchForm
from .models import Restaurant

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_restaurants')
    else:
        form = RestaurantForm()
    return render(request, 'add_restaurant.html', {'form': form})


def show_restaurants(request):
    form = SearchForm(request.GET)

    if form.is_valid():
        specialization = form.cleaned_data.get('specialization')
        if specialization:
            restaurants = Restaurant.objects.filter(specialization__icontains=specialization)
            return render(request, 'app_restaurant/show_filtered_restaurants.html',
                          {'restaurants': restaurants, 'form': form})

    restaurants = Restaurant.objects.all()
    return render(request, 'app_restaurant/show_restaurants.html', {'restaurants': restaurants, 'form': form})


