from django.shortcuts import render


def _home(request):
    return render(request, "recipes\home.html")
