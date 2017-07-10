import django_tables2 as tables
from .models import Listing


class ListingTable(tables.Table):
    class Meta:
        model = Listing
        exclude = ('User', )
