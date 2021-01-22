
from django.shortcuts import render
import sqlite3
import random
from django.conf import settings

# Create your views here.
type_user = True




def serveindex(request):
    print(settings.BASE_DIR)
    return render(request, 'index.html')


def serveform(request):
    return render(request, 'form.html')

def servereadings(request):
    pass

def serveoptions(request):
    random_value = random.random()
    print(random_value)
    if random_value < 0.05:
        return render(request, 'options_2.html')
    else:
        return render(request, 'options.html')

def servelogin(request):
    return render(request, 'login.html')

def servewebapp(request):
    print(request.POST)
    user = request.POST['user']
    password = request.POST['pass']
    conn = sqlite3.connect(str(settings.BASE_DIR) + "/sqlite.db")
    c = conn.cursor()
    res = c.execute("Select * from users where email=?", (user,))
    for row in res:
        if row:
            if user == row[1] and password == row[2]:
                if random.random() < 0.5:
                    return render(request, 'webapp_user.html')
                else:
                    return render(request, 'webapp_user_good.html')

    res = c.execute("Select * from company_user where email=?", (user,))
    for row in res:
        if row:
            if user == row[1] and password == row[2]:
                return render(request, 'webapp_tecnico.html')

    tparam = {'error': True}
    return render(request, 'login.html', tparam)

def servesupport(request):
    return render(request, 'support.html')

def redirectsup(request):
    if type_user:
        return render(request, 'webapp_user.html')