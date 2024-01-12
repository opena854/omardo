from random import randint, randrange
from django.shortcuts import render


def get_random_data():
    emoji_list = "😀😁😂🤣😃😄😅😆😉😊😋😎😘🥰😗🤗🤩🤨😐😑😶😏😣😮😯😫😖😤😬🤠🙈"
    adverbio = ("cuando", "donde", "que")
    accion = (
        "saludo",
        "digo hola",
        "doy la bienvenida",
        "agradezco la visita",
        "informo cosas",
        "pongo un emoji aleatorio",
    )
    delayinterval = (1, 2, 3, 4)

    def rnd(list):
        return list[randrange(0, len(list))]

    return {
        "emoji": rnd(emoji_list),
        "adverbio": rnd(adverbio),
        "accion": rnd(accion),
        "delayinterval": rnd(delayinterval),
    }


# Create your views here.
def home(request):
    return render(
        request,
        "main/base.html",
        get_random_data(),
    )
