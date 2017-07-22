from django.db.models.aggregates import Avg

from spinners.models import Spin, Spinner
from customers.models import Customer

customer = Customer.objects.first()

request = Object()
request.customer = customer

# get the avarage spin duration duration
avg_duration = (Spin.objects
                .filter(user_spinner__user__customer=request.customer)
                .aggregate(avg=Avg('duration')))['avg']

print('Average duration:', avg_duration, 's')

avg_duration = (Spin.objects
                .filter(customer=request.customer)
                .aggregate(avg=Avg('duration')))['avg']

print('Average duration:', avg_duration, 's')


# get a list of spinners ordered from the fastest to the slowest
spinners = (Spinner.objects
            .filter(customer=request.customer)
            .annotate(
                avg_duration=Avg('owned_spinners__spins__duration'))
            .order_by('-avg_duration'))

print('Average duration for spinner:')
for spinner in spinners:
    print(spinner.name, ':', spinner.avg_duration)
