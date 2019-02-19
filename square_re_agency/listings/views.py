from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from listings.models import Listing

# Create your views here.
def index(request):
    listings_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings_list, 2)

    page = request.GET.get('page')
    listings = paginator.get_page(page)
    return render(request,'listings/listings.html',{'listings':listings})

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    return render(request,'listings/listing.html',{'listing':listing})

def search(request):
    return render(request,'listings/search.html')
