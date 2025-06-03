from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

@login_required
def profile_list_view(request):
    context = { 
        'object_list': User.objects.filter(is_active=True)
    }
    return render(request, "profiles/list.html", context)



@login_required
def profile_view(request, username=None ,*args, **kwargs):
    user = request.user
    print(user.has_perm("profiles.view_profile"))
    # <app_label>.view_<modelname>
    # <app_label>.add_<modelname>
    # <app_label>.delete_<modelname>
    # <app_label>.change_<modelname>
    print('user.has_perm("auth.view_user")', user.has_perm("auth.view_user"))
    print('user.has_perm("visits.view_pagevisit")', user.has_perm('visits.view_pagevisit'))
    #profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    return HttpResponse(f"Hello {username} - {profile_user_obj.id} - {user.id} - {is_me}") # f string

@login_required
def profile_detail_view(request, username=None ,*args, **kwargs):
    user = request.user
    print(
        user.has_perm("subscriptions.basic"),
        user.has_perm("subscriptions.basic_ai"),
        user.has_perm("subscriptions.advanced"),
        user.has_perm("subscriptions.pro")
        )
    # user_groups = user.groups.all()
    # print(user_groups)
    # if user_groups.filter(name__icontains='basic').exists():
    #     return HttpResponse("Congrats")
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    context = {
        'instance': profile_user_obj,
        'owner': is_me
    }
    return render(request, "profiles/detail.html", context)

