from django.shortcuts import redirect
# ****** Authentication ******
def auth(view_functio):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return view_functio(request,*args,**kwargs)
    return wrapper

# ****** GEST ******
def gest(view_functio):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_functio(request,*args,**kwargs)
    return wrapper