from django.shortcuts import render

def main_page(request):
    title = 'Главная страница'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
        'title': title,
        'cart': cart,
        'shop': shop
    }
    return render(request, 'fourth_task/main_page.html', context)

def second_page(request):
    title = 'Игры'
    shop = 'Магазин'
    cart = 'Корзина'
    game = {'games': ['game1', 'game2', 'game3']}
    buy = 'Купить'
    back = 'Вернуться'
    contex = {
        'title': title,
        'game': game,
        'buy': buy,
        'back': back,
        'shop': shop,
        'cart': cart
    }
    return render(request, 'fourth_task/second_page.html', contex)

def third_page(request):
    title= 'Корзина'
    back = 'Вернуться'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
        'title': title,
        'back': back,
        'cart': cart,
        'shop': shop
    }
    return render(request, 'fourth_task/third_page.html', context)