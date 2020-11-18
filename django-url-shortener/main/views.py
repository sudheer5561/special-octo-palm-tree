from django.shortcuts import render, get_object_or_404, redirect

from .models import ShortLink


def redirect_view(request, link_name):
    link = get_object_or_404(ShortLink, short=link_name)
    return redirect(to=link.full, permanent=True)
