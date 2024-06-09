from django.shortcuts import render


# Create your views here.
def first_page(request):
    return render(request, 'html/home_page.html')


def about(request):
    return render(request, 'html/about_page.html')
