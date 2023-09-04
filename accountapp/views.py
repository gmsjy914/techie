from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import Registration


# Create your views here.


def hello_world(request, HttpResponseRedirct=None):
    if request.method == "POST":
        email = request.POST.get('email')

        reg = Registration()
        reg.email = email
        reg.save()

        reg_all = Registration.objects.all()

        return HttpResponseRedirect(reverse("accountapp:hello_world"))

    reg_all = Registration.objects.all()

    temp = "건담쵝오!"
    return render(request, "accountapp/hello_world.html",
                  context={"temp": temp,
                           "red_all": reg_all})
