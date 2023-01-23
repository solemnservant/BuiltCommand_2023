from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Member, Location, Lease, Soft_Service, Hard_Service, Safety_Service
from .forms import MemberForm, LocationForm
from django.http import Http404

# Create your views here.
@login_required
def member(request, member_id):
    """Comapany page for updating facilities info"""
    member = Member.objects.get(id = member_id)
    location = Location.objects.all()
    lease = Lease.objects.all()
    softServ = Soft_Service.objects.all()
    hardServ = Hard_Service.objects.all()
    safetyServ = Safety_Service.objects.all()

    # Make sure the information belongs to the currently logged in member only
    if member.owner != request.user:
        raise Http404

    context = {'member': member, 
               'location': location,
               'lease': lease,
               'softServ': softServ,
               'hardServ': hardServ,
               'safetyServ': safetyServ}

    return render(request, 'members/member.html', context)

@login_required
def all_members(request):
    '''Shows list of all members'''
    all_members = Member.objects.filter(owner=request.user).order_by ('date_added')
    context = {'members':all_members}
    return render(request, 'members/all_members.html', context)

def index(request):
    """Test Page"""
    return render(request, 'members/index.html')

@login_required
def new_member(request):
    '''Add a new office'''
    if request.method != 'POST':
        #No data submitted; create a blank form
        form = MemberForm()
    else:
        # POST data submitted; process data
        form = MemberForm(data = request.POST)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.owner = request.user
            new_member.save()
            return redirect('members:all_members')

    #Display a blank or invalid form.
    context = {"form": form}
    return render(request, 'members/new_member.html', context)

@login_required
def edit_member(request, member_id):
    """Edit an existing Entry."""
    member = Member.objects.get(id=member_id)
    location = Location.objects.get(id=member_id)

    if member.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Inital request; pre-fill form with the current company info.
        form = MemberForm(instance=member)
        localForm = LocationForm(instance=location)
    else:
        # Post data submitted; process data.
        form = MemberForm(instance=member, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('members:member', member_id=member.id)

    context = {'form': form, 'member': member, 'localForm':localForm}
    return render(request, 'members/edit_member.html', context)