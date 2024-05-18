from django.shortcuts import render
from .models import Accommodation
from django.shortcuts import get_object_or_404
from .models import ListOfCountries
from django.contrib import admin
from django.urls import path

def main(request):
    return render(request, 'myapp/index.html')


def accommodations(request):
    title = 'размещение'

    list_of_accommodations = Accommodation.objects.filter(is_active=True)

    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations,
    }

    return render(request, 'myapp/accommodations.html', content)



def accommodation(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'accommodation': get_object_or_404(Accommodation, pk=pk),
    }

    return render(request, 'myapp/accommodation_details.html', content)


urlpatterns = [
    # path('admin/', admin.site.urls),
]

