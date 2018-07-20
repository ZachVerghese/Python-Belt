from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def login(request):
    return render(request, 'belt_app/login.html')


def process_registration(request):
    result= User.objects.validate_registration(request.POST)
    if len(result)>0:
        for key in result.keys():
            messages.error(request,result[key])
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
        user= User.objects.create(first_name=request.POST['first_name'], last_name = request.POST['last_name'], email= request.POST['email'], password= hashed_pw)
        request.session['user_id']=user.id
        return redirect('/quotes')

def process_login(request):
    user= User.objects.filter(email=request.POST['email'])
    if len(user) == 0:
        messages.error(request,"No user with that email exists")
        return redirect('/')
    else:
        user=user.first()
    password_validation = bcrypt.checkpw(request.POST['password'].encode(), user.password.encode())
    if password_validation:
        request.session['user_id']=user.id
        return redirect('/quotes')
    else:
        messages.error(request,"Information is Incorrect")
        return redirect('/')


def index(request):
    if 'count' not in request.session:
        request.session['count']=0
    the_user= User.objects.get(id=request.session['user_id'])
    all_quotes=Quote.objects.all()
    context={
        "user":the_user,  
        "quotes":all_quotes,
    }
    return render(request,'belt_app/index.html', context)

def create(request):
    result= Quote.objects.validate_quote(request.POST)
    if len(result)>0:
        for key in result.keys():
            messages.error(request,result[key])
        return redirect('/quotes')
    else:
        the_user= User.objects.get(id=request.session['user_id'])
        Quote.objects.create(author=request.POST['author'], content=request.POST['content'], uploader= the_user)
        return redirect('/quotes')
    

def edit(request):
    user= User.objects.get(id=request.session['user_id'])
    context={
        "user":user,  
    }
    return render(request, 'belt_app/edit.html', context)

def update(request):
    user=User.objects.get(id=request.session['user_id'])
    result= User.objects2.validate_registration(request.POST)
    result2 = User.objects3.validate_registration(request.POST)

    if user.email != request.POST['email']:
        if len(result)>0:
            for key in result.keys():
                messages.error(request,result[key])
            return redirect('/edit')
        else:
            the_user= User.objects.get(id=request.session['user_id'])
            the_user.first_name=request.POST['first_name']
            the_user.last_name=request.POST['last_name']
            the_user.email=request.POST['email']
            the_user.save()
            return redirect('/quotes')
    else: 
        if len(result2)>0:
            for key in result2.keys():
                messages.error(request,result2[key])
            return redirect('/edit')
        else:
            the_user= User.objects.get(id=request.session['user_id'])
            the_user.first_name=request.POST['first_name']
            the_user.last_name=request.POST['last_name']
            the_user.email=request.POST['email']
            the_user.save()
            return redirect('/quotes')

def show_user(request,user_id):
    the_user= User.objects.get(id=user_id)
    the_quotes= Quote.objects.filter(uploader=the_user)
    context={
        "user":the_user,
        "quotes":the_quotes
    }
    return render(request,'belt_app/user.html', context)

def logout(request,user_id):
    del request.session['user_id']
    return redirect('/')

def delete(request,quote_id):
    the_quote=Quote.objects.get(id=quote_id)
    the_quote.delete()
    return redirect('/quotes')

def add_like(request,quote_id):
    the_quote=Quote.objects.get(id=quote_id)
    the_user=User.objects.get(id=request.session['user_id'])
    the_quote.likes.add(the_user)
    count = the_quote.likes.count()
    # request.session['count']+=count
    return redirect('/quotes')