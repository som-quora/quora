from django.conf.urls import url, include
from . import views

# Create a new class that redirects the user to the index page, if successful at logging
#class MyRegistrationView(RegistrationView):
#    def get_success_url(self,request, user):
#        return '/rango/'

urlpatterns = [
    url(r'^$', views.home, name='home'),
]