from django.shortcuts import render

# Create your views here.
from hwapp.models import Phrases


def helloworld(request, pk=1):

    firstword = Phrases.objects.get(pk=pk)
    secondword = Phrases.objects.get(pk=pk)

    context = {

        "firstwordname": firstword,
        "secondwordname": secondword,
    }

    return render(request, "helloworld.html", context)
