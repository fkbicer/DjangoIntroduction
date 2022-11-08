from .company import Company
from django.db import models
from django.contrib.auth.models import User


class Dealer(Company):
    staff = models.ManyToManyField(User, related_name='dealers', related_query_name='dealer')
