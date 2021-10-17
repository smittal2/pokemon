

def login_required(func):
    """
    :param func:
    :return:
    This is a decorator when applied on a function will return invalid request if user is not authenticated
    """
    return func


def required_fields(*arg):
    def required_decorator(func):
        def func_wrapper(request, *args, **kwargs):
            fields = []
            x= set(list())

            for i in arg:
                fields.append(i)

            fields = set(fields)

            if request.method == 'POST':
                x = set(request.POST.keys())
            elif request.method == 'GET':
                x = set(request.GET.keys())

            f = fields - x

            st = ', '.join(list(f)) + ' missing'

            if f:
                return Response(dict(status=0, message=st))
            else:
                return func(request, *args, **kwargs)

        return func_wrapper

    return required_decorator