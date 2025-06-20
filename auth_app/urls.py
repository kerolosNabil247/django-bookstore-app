from django.urls import path
from .views import login_pg, signup, signout

app_name = 'auth_app'
urlpatterns = [
    path('login', login_pg, name='login'),
    path('signout', signout, name='signout'),
    path('signup', signup, name='signup'),
]