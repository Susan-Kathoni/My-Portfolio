from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category, Portfolio


# Create your views here.
def portfolio_page(request):
    return render(request, 'portfolio/portfolio.html')

def portfolio_details(request, portfolio_id):
    item = Portfolio.objects.get(id=portfolio_id)
    context = {
        'item': item
    }
    return render(request, 'portfolio.html', context)
