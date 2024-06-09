from django.urls import path
from main_blog.views import first_page, about

urlpatterns = [
    path('', first_page, name='first_page'),
    path('about/', about, name='about'),
]
