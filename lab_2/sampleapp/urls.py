from django.conf.urls import url
from sampleapp import views
urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
	]