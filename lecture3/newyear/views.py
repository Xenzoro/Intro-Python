from django.shortcuts import render
from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now() #calls function to store date into now variable
    return render(request, "newyear/index.html.old", {
        "newyear": now.month == 1 and now.day == 1 # this verifies to see if date is New years day
    })