from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            Message = "Invalid login details supplied."
            return render_to_response('login.html', locals())
    else:
        return render_to_response('login.html', {}, context)

def home(request):
    context = RequestContext(request)
    try:
        return render_to_response('home.html')
    except:
        return render_to_response('login.html', {}, context)

@login_required
def user_logout(request):
    try:
        context = RequestContext(request)
        logout(request)

        return render_to_response('login.html', {}, context)
    except:
        return render_to_response('login.html', {}, context)