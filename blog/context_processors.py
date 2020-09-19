from blog.models import Category

def get_categories(request):
    categories = Category.objects.order_by('id').values_list('id', 'name')

    return {
        'categories': categories
    }