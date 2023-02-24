from django.shortcuts import render
from django.core import serializers
from django.views import View

from datetime import datetime

from .models import Menu, Booking
from .forms import BookingForm


class GetBookingsAsJSONMixin:

    def get_bookings(self):
        bookings = Booking.objects.filter(reservation_date=datetime.today().date())
        if bookings.exists():
            return serializers.serialize('json', bookings)
        return {'bookings': 'No Booking'}


class Bookings(GetBookingsAsJSONMixin, View):
    template_name = 'bookings.html'

    def get(self, request):
        context = {
            'bookings': self.get_bookings()
        }
        return render(request, self.template_name, context)


class Book(GetBookingsAsJSONMixin, View):
    form_class = BookingForm
    template_name = 'book.html'

    def get(self, request):
        context = {
            'form': self.form_class(),
            'bookings': self.get_bookings()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            context = {
                'form': self.form_class(request.POST),
                'bookings': self.get_bookings(),
                'errors': form.errors.as_data(),
            }
            return render(request, self.template_name, context)
        form.save()
        return self.get(request)


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 