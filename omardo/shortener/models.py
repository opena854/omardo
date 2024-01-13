import datetime
import string

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib import admin
from uuid import uuid4


class IntToBase:
    def __init__(self, number, base=10):
        self.number = number
        self.base = base

    def __iter__(self):
        self.remain = self.number
        return self

    def __next__(self):
        if self.remain <= 0:
            raise StopIteration
        x = self.remain % self.base
        self.remain = self.remain // self.base
        return x


class User(models.Model):
    key = models.UUIDField(default=uuid4, unique=True)
    email = models.EmailField("Correo Electrónico", max_length=254, null=True)
    email_verified = models.BooleanField(default=False)
    created = models.DateTimeField()

    def __str__(self):
        return self.email if self.email else self.key.hex


class ShortUrl(models.Model):
    def exists(key):
        return ShortUrl.objects.filter(key=key).exists()

    def generate_key():
        letters = string.digits + string.ascii_lowercase
        base = uuid4().hex

        for i in range(0, 24):
            key_int = int(base[i : i + 8], 16)
            key_test = "".join([letters[a] for a in IntToBase(key_int, len(letters))])

            if not ShortUrl.exists(key_test):
                break
        else:
            raise Exception("Please retry.")

        return key_test

    key = models.CharField(max_length=20, default=generate_key, unique=True)
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{url_base}/_/{key}".format(url_base="https://omar.do", key=self.key)
