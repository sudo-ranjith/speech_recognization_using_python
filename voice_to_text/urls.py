from django.conf.urls import url
from .views import home, speech

urlpatterns = [
    url(r'home', home, name='home'),
    url(r'speech', speech, name='speech')
]
