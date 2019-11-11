from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponse
from ghost.models import BRoast
from ghost.forms import AddBRoast

def homepage(request):
    broasts = BRoast.objects.all()
    return render(request, "posts.html", {broasts})


def broast_form(request):
    return render(request, "generic_forms.html")