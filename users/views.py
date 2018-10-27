from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """logout user"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """user register"""
    if request.method != 'POST':
        # show empty regist table
        form = UserCreationForm()
    else:
        # chulitianhaodebiaodan
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            print('***')
            new_user = form.save()
            print('test0')
            # rangyonghuzidongdenglu,zaichongdingxiangdaozhuye
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request, authenticated_user)
            print('test')
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form':form}
    return render(request, 'users/register.html' ,context)