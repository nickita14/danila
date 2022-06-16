from django.http import HttpResponseNotFound, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Product, Category

class ShopMain(ListView):
    model = Product
    template_name = 'sweet_shop/shop.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShopMain, self).get_context_data(**kwargs)
        context['header'] = "Все наши товары"
        context['title'] = 'Магазин'
        return context

class SearchPage(ListView):
    paginate_by = 3
    model = Product
    template_name = 'sweet_shop/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('curds'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchPage, self).get_context_data(**kwargs)
        if len(context['products']) == 0:
            context['header'] = 'Таких сырков у нас нет'
        else:
            context['header'] = "Найденные товары"
            context['title'] = 'Поиск'
        return context

class ShowProduct(DetailView):
    model = Product
    template_name = 'sweet_shop/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ShowProduct, self).get_context_data(**kwargs)
        context['title'] = context['product'].name
        return context

class ProductCategory(ListView):
    model = Product
    template_name = 'sweet_shop/shop.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(categories__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategory, self).get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        context['title'] = f'Категория - {category.name}'
        context['header'] = f'Товары в категории {category.name}'
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
