import pdb
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.admin.views.decorators import staff_member_required

from cobra_directory.models import MyUser

def roster(request):
    users_list = MyUser.objects.all()
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
    profile = MyUser.objects.get(id=user_id)

    context = { 'profile' : profile }

    return render_to_response(
        "cobra_directory/profile.html",
        context,
        RequestContext(request, {}),
    )

profile = staff_member_required(profile)
