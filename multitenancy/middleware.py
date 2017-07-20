from customers.models import Customer


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
