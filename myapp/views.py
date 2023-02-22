from django.shortcuts import render
from myapp.forms import MenuForm
from .models import Menu
from django.http import JsonResponse

# Add code for form_view() function below

def form_view(request):
    form_class = MenuForm
    template_name = 'menu_items.html'

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'success'})
        return JsonResponse({'message': 'Invalid!'})
    return render(request, template_name, {'form': form_class()})
