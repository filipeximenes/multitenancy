from .threadlocal import thread_local

from customers.models import Customer

"""
Swtich the middleware to change from
'Single Schema' to 'Multi Db' multitenancy
"""


def tenant_middleware(get_response):
    def middleware(request):
        host = request.get_host().split(':')[0]
        subdomain = host.split('.')[0]

        try:
            customer = Customer.objects.get(name=subdomain)
        except Customer.DoesNotExist:
            customer = None

        request.customer = customer

        response = get_response(request)
        return response

    return middleware


def multidb_middleware(get_response):
    def middleware(request):
        host = request.get_host().split(':')[0]
        subdomain = host.split('.')[0]

        try:
            customer = Customer.objects.get(name=subdomain)
        except Customer.DoesNotExist:
            customer = None

        request.customer = customer

        @thread_local(using_db=customer.name)
        def execute_request(request):
            return get_response(request)

        response = execute_request(request)

        return response

    return middleware
