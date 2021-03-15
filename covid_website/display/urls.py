from django.urls import path
from.import views
urlpatterns=[
path('hospitail/',views.hospitail_detail,name='hospitail_detail'),
path('survey/',views.survey , name='covid_survey'),
path('home' ,views.index , name='home_page'),
path('login/',views.login , name='login_page'),
path('',views.signup,name='signup_page')

]