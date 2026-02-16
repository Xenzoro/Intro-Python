from django.urls import path, include

from . import views #located in the same directory as urls.py, so we can import it using a relative import. this allows us to access the view functions defined in views.py and associate them with specific URL patterns in our application.

urlpatterns = [
    path("", views.index, name="index"), #"" is the default route that loads the empty string
    path("brian/", views.brian, name="brian"),
    path("david/", views.david, name="david"),
    path("<str:name>", views.greet, name="greet"), #rather than prescribing where it should go to, we can use a variable to capture the name from the URL and pass it to the greet view function. the <str:name> syntax indicates that we want to capture a string from the URL and assign it to the variable name. when we visit a URL that matches this pattern, such as /hello/John/, the greet view will be called with name set to "John", and it will return a personalized greeting message.
    path('newyear/', include("newyear.urls")), #this line tells Django to include the URL patterns defined in the newyear app's urls.py file whenever a URL starts with "newyear/". this allows us to organize our URL patterns in a modular way, keeping the URL configuration for the newyear app separate from the main project URLs. when a user visits a URL that starts with "newyear/", Django will look for matching patterns in the newyear app's urls.py file and route the request accordingly.)

]