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
    return render(request, 'third_task/main_page.html', context)

def second_page(request):
    title = 'Игры'
    game = 'Игра'
    buy = 'Купить'
    back = 'Вернуться'
    contex = {
        'title': title,
        'game': game,
        'buy': buy,
        'back': back
    }
    return render(request, 'third_task/second_page.html', contex)

def third_page(request):
    title_url = 'Корзина'
    title = 'Извините, корзина пуста'
    back = 'Вернуться'
    context = {
        'title_url': title_url,
        'title': title,
        'back': back
    }
    return render(request, 'third_task/third_page.html', context)
