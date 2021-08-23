from django.shortcuts import redirect, render

def is_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        return redirect('/webserver/admin/') if request.user.is_authenticated else view_func(request, *args, **kwargs)
    return wrapper

def is_unauthenticated(view_func):
    def wrapper(request, *args, **kwargs):
        return view_func(request, *args, **kwargs) if request.user.is_authenticated else redirect('/webserver/')
    return wrapper