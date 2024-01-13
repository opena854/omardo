from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import ShortUrl


# Create your views here.
def get_redirect(request, key):
    url = get_object_or_404(ShortUrl, key=key)

    # return HttpResponseRedirect(url.url)
    return render(
        request,
        "shortener/redirect.html",
        {"output": "found: {url}".format(url=url.url)},
    )
