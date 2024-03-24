from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic
from finance.models import User, Club

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "auth/signup.html"

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def general_user_view(request):
    username = request.user.username
    user_instance = User.objects.get(email=username)
    managed_clubs = len(user_instance.manager_of.all())
    memmber_clubs = []
    managed_clubs = []
    all_clubs = []
    if user_instance.is_institution:
        for club in Club.objects.all():
            all_clubs.append(club.name)
        context = {
            'username': username,
            'managed_clubs': managed_clubs,
            'member_clubs': memmber_clubs,
            'all_clubs': all_clubs,
            'if_admin' : 1
        }
        return render(request, 'finance/general_user.html', context)
            
    for club in user_instance.manager_of.all():
        managed_clubs.append(club.name)
    for club in user_instance.member_of.all():
        memmber_clubs.append(club.name)
    
    my_variable = "Hello, Django!"
    context = {
        'my_variable': my_variable,
        'username': username,
        'managed_clubs': managed_clubs,
        'member_clubs': memmber_clubs,
        'all_clubs': all_clubs,
        'if_admin' : 0
    }
    return render(request, 'finance/general_user.html', context)

@login_required
def member_view(request):
    user = request.user
    #TODO: add list of members in the club
    #TODO: show list of executives
    #TODO: show due payment status
    #TODO: send back reuqest for reimbursement
    return render(request, 'finance/member.html')

@login_required
def manager_view(request):
    user = request.user
    return render(request, 'finance/manager.html')
    

@login_required
def institution_view(request):
    user = request.user
    return render(request, 'finance/institution.html')

@login_required
def user_payment(request):
    user = request.user
    return render(request, 'finance/payment.html')

@login_required
def reimbursement(request):
    user = request.user
    return render(request, 'finance/reimbursement.html')

@login_required
def general_user(request):
    user = request.user
    return render(request, 'finance/general_user.html')