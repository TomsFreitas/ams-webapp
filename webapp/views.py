from django.shortcuts import render


# Create your views here.
type_user = True

def serveindex(request):
    return render(request, 'index.html')


def serveform(request):
    return render(request, 'form.html')

def servereadings(request):
    pass

def serveoptions(request):
    return render(request, 'options.html')

def servelogin(request):
    return render(request, 'login.html')

def servewebapp(request):
    print(request.POST)
    user = request.POST['user']
    password = request.POST['pass']

    if user == "osvaldo@gmail.com" and password == "password":
        return render(request, 'webapp_user.html')
    elif user == "aneves@empresax.pt" and password == "password":
        return render(request, 'webapp_tecnico.html')
    else:
        tparam = {'error': True}
        return render(request, 'login.html', tparam)

def servesupport(request):
    return render(request, 'support.html')

def redirectsup(request):
    if type_user:
        return render(request, 'webapp_user.html')