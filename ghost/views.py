from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponse
from ghost.models import BRoast
from ghost.forms import Add_BRoast

def homepage(request, *args, **kwargs):
    keys = kwargs.keys()
    print(kwargs)
    if("pk" in keys and "vote" in keys):
        post = BRoast.objects.get(pk=kwargs['pk'])
        if(kwargs['vote'] == "upvote"):
            post.upboats += 1
        if(kwargs['vote'] == "downvote"):
            post.downrowts += 1
        post.save()
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    broasts = BRoast.objects.all()
    broasts = sorted(BRoast.objects.all(), key=lambda x: x.time_submit)

    
    if('byvote' in keys):
        broasts = sorted(broasts, key=lambda x : x.downrowts - x.upboats)
    elif('boasts' in keys):
        broasts = sorted(BRoast.objects.filter(boast_or_roast=False), key=lambda x: x.time_submit)
    elif('roasts' in keys):
        broasts = sorted(BRoast.objects.filter(boast_or_roast=True), key=lambda x: x.time_submit)
    
    return render(request, "broasts.html", {"broasts":broasts})


def broast_form(request):
    if request.method == "POST":
        form = Add_BRoast(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BRoast.objects.create(
                boast_or_roast = data["boast_or_roast"],
                content = data["content"],
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = Add_BRoast()
    return render(request, "generic_forms.html", {'form': form})