from django.db import models


class Spinner(models.Model):
    customer = models.ForeignKey('customers.Customer')

    name = models.CharField(max_length=255)


class UserSpinner(models.Model):
    customer = models.ForeignKey('customers.Customer')

    user = models.ForeignKey('users.User')
    spinner = models.ForeignKey('spinners.Spinner')


class Spin(models.Model):
    customer = models.ForeignKey('customers.Customer')

    user_spinner = models.ForeignKey('spinners.UserSpinner')
    duration = models.DurationField()
