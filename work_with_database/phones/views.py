from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', None)
    template = 'catalog.html'

    # sort_options = {
    #     'name': 'name',
    #     'min_price': 'price',
    #     'max_price': '-price'
    # }
    #
    # # Если фильтр не указан или указан неверный фильтр order_by не делаю
    # if not sort or not sort_options.get(sort, None):
    #     phones = Phone.objects.all()
    # else:
    #     phones = Phone.objects.all().order_by(sort_options.get(sort))

    phones = Phone.objects.all()

    match sort:
        case 'name':
            phones = phones.order_by('name')
        case 'min_price':
            phones = phones.order_by('price')
        case 'max_price':
            phones = phones.order_by('-price')
        case _:
            pass

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # Получаю объект или ошибку 404
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
