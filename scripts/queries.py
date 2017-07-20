from django.db.models.aggregates import Avg

from spinners.models import Spin, Spinner
from customers.models import Customer

customer = Customer.objects.first()

# get the avarage spin duration duration
avg_duration = (Spin.objects
                .filter(user_spinner__user__customer=customer)
                .aggregate(avg=Avg('duration')))['avg']

print('Average duration:', avg_duration, 's')

avg_duration = (Spin.objects
                .filter(customer=customer)
                .aggregate(avg=Avg('duration')))['avg']

print('Average duration:', avg_duration, 's')


# get a list of spinners ordered from the fastest to the slowest
spinners = (Spinner.objects
            .filter(customer=customer)
            .annotate(
                avg_duration=Avg('owned_spinners__spins__duration'))
            .order_by('-avg_duration'))

print('Average duration for spinner:')
for spinner in spinners:
    print(spinner.name, ':', spinner.avg_duration)
