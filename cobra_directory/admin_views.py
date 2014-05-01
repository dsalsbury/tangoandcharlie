import pdb
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User

def roster(request):
    users_list = User.objects.all()
    context = {'users_list': users_list,}

    return render_to_response(
        "cobra_directory/users_list.html",
        context,
        RequestContext(request, {}),
    )

roster = staff_member_required(roster)
