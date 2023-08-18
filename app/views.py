from django.shortcuts import render,HttpResponse
from django.contrib import messages
from app.models import log,log1,subject, ass, testtable
import re, collections
# Create your views here.
d = collections.defaultdict(list)
def index(request):
    return render(request, 'index.html')

def home(request):
    user1=log.objects.all()
    return render(request, 'home.html',{'users1' : user1,'subs' : subject.objects.all()})

def home1(request):
    user=log1.objects.all()
    return render(request, 'home1.html',{'users' : user,'subs' : subject.objects.all(),},)

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def signup1(request):
    return render(request, 'signup1.html')

def signin1(request):
    return render(request, 'signin1.html')

def assignment(request):
    user1=log.objects.all()
    return render(request, 'assignment.html',{'users1' : user1,'ass' : ass.objects.all(),})

def assignmentT(request):
    user=log1.objects.all()
    return render(request, 'assignmentTEACHER.html',{'users' : user,'ass' : ass.objects.all(),})

def test(request):
    user1=log.objects.all()
    return render(request, 'test.html',{'users1' : user1,'tests' : testtable.objects.all(),})

def testT(request):
    user=log1.objects.all()
    return render(request, 'testTEACHER.html',{'users' : user,'tests' : testtable.objects.all(),})

def meeting(request):
    context = {}
    return render(request, 'videoconference.html', context=context)

def meeting1(request):
    context = {}
    
    return render(request, 'videoconference1.html', context=context)

def reg(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        def ispresent(str):
            regex = ("^(?=.*[a-z])(?=." +
            "*[A-Z])(?=.*\\d)" +
            "(?=.*[-+_!@#$%^&*., ?]).+$")
            p = re.compile(regex)
            if(re.search(p, str) and len(str) >= 8):
                return True
            else:
                return False
        a = log.objects.filter(email=email).values('email')
        if a:
            messages.error(request, 'This email already exists!')
            return render(request, 'signin.html')
        if ispresent(password):
            user = log(username=name, email=email, password=password)
            user.save()
        else:
            messages.error(request, 'Password error')
            return render(request, 'signup.html')
        return render(request, 'signin.html')

def reg1(request):
    if request.method == "POST":
        name1 = request.POST.get('name1')
        email1 = request.POST.get('email1')
        password1 = request.POST.get('password1')
        def ispresent(str):
            regex = ("^(?=.*[a-z])(?=." +
            "*[A-Z])(?=.*\\d)" +
            "(?=.*[-+_!@#$%^&*., ?]).+$")
            p = re.compile(regex)
            if(re.search(p, str) and len(str) >= 8):
                return True
            else:
                return False
        a = log1.objects.filter(email1=email1).values('email1')
        if a:
            messages.error(request, 'This email already exists!')
            return render(request, 'signin1.html')
        if ispresent(password1):
            user = log1(username1=name1, email1=email1, password1=password1)
            user.save()
        else:
            messages.error(request, 'Password error')
            return render(request, 'signup1.html')
        return render(request, 'signin1.html')

def logout(request):
     del request.session['email1']
     return render(request, 'index.html')

def v(request):
       return render(request, 'view.html', {'s' : s,})

def logout1(request):
     del request.session['email']
     return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user1=log.objects.all()
        a = log.objects.filter(email=email,password=password).values('email','password')
        print(a)
        if a:
            user=log.objects.get(email=email)
            request.session['email'] = user.email
            return render(request, 'home.html', {'users1' : user1,'subs' : subject.objects.all()})
        else:
            messages.error(request, 'Invalid Credentials!')
            return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')

def login1(request):
    if request.method == "POST":
        email1 = request.POST.get('email1')
        password1 = request.POST.get('password1')
        subjectname = request.POST.get('subname')
        user=log1.objects.all()
        a = log1.objects.filter(email1=email1,password1=password1).values('email1','password1')
        print(a)
        if a:
            user1=log1.objects.get(email1=email1)
            request.session['email1'] = user1.email1
            return render(request, 'home1.html', {'users' : user,'subs' : subject.objects.all()})
        else:
            messages.error(request, 'Invalid Credentials!')
            return render(request, 'signin1.html')
    else:
        return render(request, 'signin1.html')



def sub(request):
    if request.session['email1']:
        user=log1.objects.all()
        session = request.session.get('email1')
        subjectname= request.POST.get('subname')
        #d[session].append(subjectname)
        sub=subject.objects.create(subjectname=subjectname)
        sub.email=session
        sub.save()
        return render(request, 'home1.html', {'users' : user,'subs' : subject.objects.all(),}, )

def tes(request):
    if request.session['email1']:
        user=log1.objects.all()
        session1 = request.session.get('email1')
        subjectname1= request.POST.get('subname1')
        question1= request.POST.get('tq')
        time1= request.POST.get('ttime')
        print("s,q,t",subjectname1,question1,time1)
        sub1 = testtable(email3=session1,subjectname3=subjectname1,question3=question1,time3=time1)
        sub1.save()
        return render(request, 'testTEACHER.html', {'users' : user,'tests' : testtable.objects.all(),}, )

def assign(request):
    if request.session['email1']:
        user=log1.objects.all()
        session = request.session.get('email1')
        subjectname= request.POST.get('subname2')
        question= request.POST.get('assignname')
        time= request.POST.get('atime')
        date= request.POST.get('adate')
        print(subjectname,question,time)
        sub=ass(email=session,subjectname=subjectname,question=question,time=time,date=date)
        sub.save()
        return render(request, 'assignmentTEACHER.html', {'users' : user,'ass' : ass.objects.all(),}, )


