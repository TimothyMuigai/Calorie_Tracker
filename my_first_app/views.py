from django.shortcuts import render,redirect
from .models import Calorie
from django.utils.timezone import now
from django.contrib import messages
# Create your views here.

def show_cal(request):
    food_items = Calorie.objects.all()
    calorie_amount = 0
    for items in food_items:
        calorie_amount+=items.amount_of_calories
    return render(request, 'table.html', {'calorie_amount': calorie_amount, 'food_items': food_items})

def add_data(request):
    if request.method == 'POST':
        food_name = request.POST['food_name']
        amount_of_calories = request.POST['amount_of_calories']
        Calorie.objects.create(food_name=food_name, amount_of_calories=amount_of_calories)
        messages.success(request, "Calorie entry added successfully!")
        return redirect('show_cal')
    return render(request, 'table.html')

def remove_cal(request, itemId):
    Calorie.objects.get(id=itemId).delete()
    messages.success(request, "Calorie entry removed successfully!")
    return redirect('show_cal')

def reset_calories(request):
    today = now().date()
    Calorie.objects.filter(date_added=today).delete()
    messages.success(request, "The day calorie count has been cleared!")
    return redirect('show_cal')