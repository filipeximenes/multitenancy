from model_mommy import mommy

from customers.models import Customer
# from user.models import User
# from spinners.models import Spinner


Customer.objects.all().delete()


mommy.make('customers.Customer', name='default')

customer = mommy.make('customers.Customer', name='test')
user = mommy.make('users.User', customer=customer)

poke_spinner = mommy.make(
    'spinners.Spinner', customer=customer,
    name='PokeSpinner')

user_spinner = mommy.make(
    'spinners.UserSpinner', customer=customer,
    user=user, spinner=poke_spinner)

mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=178)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=345)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=45)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=235)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=89)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=475)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=123)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=349)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=874)


ninja_spinner = mommy.make(
    'spinners.Spinner', customer=customer,
    name='NinjaSpinner')

user_spinner = mommy.make(
    'spinners.UserSpinner', customer=customer,
    user=user, spinner=ninja_spinner)

mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=158)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=345)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=95)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=345)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=89)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=195)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=344)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=349)
mommy.make(
    'spinners.Spin', customer=customer,
    user_spinner=user_spinner, duration=654)


mommy.make(
    'spinners.Spinner', customer=customer,
    name='BoringSpinner')
