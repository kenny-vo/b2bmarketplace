import django_tables2 as tables
from django_tables2.utils import A
from .models import Listing


class ListingTable(tables.Table):
    topic = tables.LinkColumn('listing-detail', args=[A('pk')])
    budget = tables.LinkColumn('listing-detail', args=[A('pk')])
    location = tables.LinkColumn('listing-detail', args=[A('pk')])

    class Meta:
        model = Listing
        fields = ('topic', 'budget', 'location', 'description',
                  'requirement1', 'requirement2', 'requirement3')
