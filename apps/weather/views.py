from django.shortcuts import render
from .utils import get_weather_data
from .models import SearchHistory

def index(request):
    try:
        city = request.POST.get('city')
        contexts = {
            "history":SearchHistory.objects.all(),
            "error":"City not fount with this name"
        }
        if city:
            weather_json = get_weather_data(city)
            print(10, weather_json)
            if weather_json[1] == 200:
                history, created = SearchHistory.objects.get_or_create(city=city)
                history.search_count += 1
                history.save()
                contexts.update({'weather': weather_json[0], "error":False})
            print(1212, contexts)
            return render(request, 'weather.html', contexts)
        return render(request, 'index.html', contexts)
    except Exception as e:
        print(20, e)

def search_history_view(request):
    history = SearchHistory.objects.all()
    return render(request, 'history.html', {'history': history})