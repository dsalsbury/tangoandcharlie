import pdb
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.admin.views.decorators import staff_member_required

from cobra_directory.models import MyUser
from django.db.models import Q

def roster(request):
    users_list = MyUser.objects.all().order_by('year', 'lastname', 'firstname')
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

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        users = MyUser.objects.filter(Q(email__icontains=q) | Q(firstname__icontains=q) | Q(lastname__icontains=q)).order_by('year', 'lastname', 'firstname')
        return render(request, 'cobra_directory/users_list.html',
            {'users_list': users, 'query': q,})
    if 'email' in request.GET:
        email    = request.GET['email']
        job      = request.GET['job']
        location = request.GET['location']
        major    = request.GET['major']
        query    = "Email: " + email + ", Job: " + job + ", Location: " + location + ", Major: " + major


        users = MyUser.objects.filter(Q(email__icontains=email) & Q(current_job__icontains=job) & Q(current_location__icontains=location) & Q(major__icontains=major)).order_by('year', 'lastname', 'firstname') 
        return render(request, 'cobra_directory/users_list.html',
            {'users_list': users, 'query': query,})
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
