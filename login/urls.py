from django import urls, include


urlpatterns = [
    path('', include('login.urls'))
]
