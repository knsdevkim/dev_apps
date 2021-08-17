from django.shortcuts import redirect 


def authenticated(view_function):
    def wrapper(request, *args, **kwargs):
        return redirect('/evaluation-list/') if request.user.is_authenticated else view_function(request, *args, **kwargs) 
    return wrapper