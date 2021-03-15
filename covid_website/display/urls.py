from django.urls import path
from.import views
urlpatterns=[
path('hospitail/',views.hospitail_detail,name='hospitail_detail'),
path('survey/',views.survey , name='covid_survey'),
path('' ,views.index , name='home_page'),
path('login/',views.login , name='login_page'),
path('signup/',views.signup,name='signup')

]