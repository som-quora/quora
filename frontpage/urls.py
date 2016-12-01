from django.conf.urls import url, include
from . import views

# Create a new class that redirects the user to the index page, if successful at logging
#class MyRegistrationView(RegistrationView):
#    def get_success_url(self,request, user):
#        return '/rango/'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^question/$', views.askquestion, name='askquestion'),
    url(r'^postanswer/(?P<qid>\d+)/$', views.postanswer, name='postanswer'),
    url(r'^question/(?P<qid>\d+)/$', views.question, name='question'),
]