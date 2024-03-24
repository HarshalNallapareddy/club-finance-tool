from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic


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
    user = request.user
    clubs = user.clubs.all()
    context = {
        'user': user,
        'clubs': clubs
    }
    return render(request, 'finance/general_user.html', context=context)

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

def reimbursement(request):
    user = request.user
    return render(request, 'finance/reimbursement.html')

def institution(request):
    user = request.user
    return render(request, 'finance/institution.html')