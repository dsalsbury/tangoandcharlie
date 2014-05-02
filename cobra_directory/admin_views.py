import pdb
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User
from cobra_directory.models import UserProfile

def roster(request):
    users = User.objects.all()
    users_list = []
    for u in users:
        profile = None
        try:
            profile = u.get_profile()
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=u)
        users_list.append(profile)
    context = {
        'users_list': users_list,
        }

    return render_to_response(
        "cobra_directory/users_list.html",
        context,
        RequestContext(request, {}),
    )

roster = staff_member_required(roster)

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = UserProfile.objects.get(user=user)

    context = { 'profile' : profile }

    return render_to_response(
        "cobra_directory/profile.html",
        context,
        RequestContext(request, {}),
    )

profile = staff_member_required(profile)
