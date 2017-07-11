import django_filters
from .models import Listing

class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = ['topic', 'budget', 'location', 'description', 'requirement1', 'requirement2', 'requirement3']
        order_by = ['pk']
