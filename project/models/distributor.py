from django.db import models
from .company import Company
from django.contrib.auth.models import User
from .dealer import Dealer


class Distributor(Company):
    dealer = models.ManyToManyField(Dealer, related_name='distributors', related_query_name='distributor', blank=True)
    staff = models.ManyToManyField(User, related_name='distributors', related_query_name='distributor', blank=True)
