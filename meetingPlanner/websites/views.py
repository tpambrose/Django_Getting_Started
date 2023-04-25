from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting
# Create your views here.


def welcome(request):
    """greeting view function"""

    return render(request,
                  "websites/welcome.html",
                  {
                      "meetings":Meeting.objects.all()
                  })
