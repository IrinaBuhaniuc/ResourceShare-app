from django.shortcuts import render

from .models import User

# Create your views here.

def user_list(request):
    users = User.objects.all()
    user_cnt = users.count()

    context = {
        'users': users,
        'user_cnt': user_cnt
    }
    
    return render(request, 'user/user_list.html', context)