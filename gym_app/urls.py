from django.urls import path
from .views import SignUpPage, Thankyou, HomePage,SignIn, Signout, CaloriePage

urlpatterns = [
    path('',HomePage,name='home'),
    path('calorie/',CaloriePage,name='calorie'),
    path('signup/',SignUpPage,name='signup'),
    path('signin/',SignIn,name='signin'),
    path('signout/',Signout,name='signout'),
    path('thankyou/',Thankyou,name='thankyou'),
]
