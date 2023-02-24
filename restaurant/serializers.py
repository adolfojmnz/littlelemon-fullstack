from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['first_name', 'reservation_date', 'reservation_time', 'reservation_slot']