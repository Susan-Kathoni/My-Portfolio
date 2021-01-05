from portfolio.models import Category, Portfolio

def portfolio_context(request):
    portfolio_category = Category.objects.filter(is_draft=False)
    portfolio = Portfolio.objects.filter(is_draft=False)
    return {'portfolio_category': portfolio_category, 'portfolio': portfolio}
