from django.shortcuts import render


def function_based_view(request):
    return render(request, 'second_task/function_based.html')

def class_based_view(request):
    return render(request, 'second_task/class_based.html')
