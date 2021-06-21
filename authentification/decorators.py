from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user_accident(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('accident:list_accident')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func
def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('Vous n\'est pas autorisez à acceder a cette section')
        return wrapper_func
    return decorator