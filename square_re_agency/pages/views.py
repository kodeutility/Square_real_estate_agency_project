from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    return render(request,'pages/index.html',{'listings':listings})

def about(request):
    realtors = Realtor.objects.all()
    mvp_realtors = Realtor.objects.filter(is_mvp=True)[:1]
    return render(request,'pages/about.html',locals())
