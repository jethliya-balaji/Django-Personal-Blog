from django.core.paginator import Paginator

def paginate(request, data, per_page):
    paginator = Paginator(data, per_page)
    page = request.GET.get('page')
    paginated_data = paginator.get_page(page)
    return paginated_data