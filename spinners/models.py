from django.db import models


class Spinner(models.Model):
    customer = models.ForeignKey('customers.Customer')

    name = models.CharField(max_length=255)


class UserSpinner(models.Model):
    customer = models.ForeignKey('customers.Customer')

    user = models.ForeignKey('users.User', related_name='owned_spinners')
    spinner = models.ForeignKey('spinners.Spinner', related_name='owned_spinners')


class Spin(models.Model):
    customer = models.ForeignKey('customers.Customer')

    user_spinner = models.ForeignKey('spinners.UserSpinner', related_name='spins')
    duration = models.PositiveIntegerField()
