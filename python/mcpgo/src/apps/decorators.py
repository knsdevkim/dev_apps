from django.shortcuts import render, redirect


def authenticated_user(views_func):
    def wrapper(request, *args, **kwargs):
        return redirect('/dashboard/') if request.user.is_authenticated else views_func(request, *args, **kwargs)
    return wrapper


def unauthenticated_user (views_func):
    def wrapper(request, *args, **kwargs):
        return views_func(request, *args, **kwargs) if request.user.is_authenticated else redirect('/')
    return wrapper


def allowed_users(allowed_roles=[]):
    def decorator(views_func):
        group = None
        def wrapper(request, *args, **kwargs):
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return views_func(request, *args, **kwargs)
            else:
                return render(request, 'errors/403.html', context = {})
        return wrapper
    return decorator
