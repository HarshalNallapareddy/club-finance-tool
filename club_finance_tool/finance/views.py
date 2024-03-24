from django.shortcuts import render

# Create your views here.
def general_user_view(request):
    user = request.user
    clubs = user.clubs.all()
    context = {
        'user': user,
        'clubs': clubs
    }
    return render(request, 'finance/general_user.html', context=context)

def member_view(request):
    user = request.user
    #TODO: add list of members in the club
    #TODO: show list of executives
    #TODO: show due payment status
    #TODO: send back reuqest for reimbursement
    return render(request, 'finance/member.html')

def manager_view(request):
    user = request.user
    return render(request, 'finance/manager.html')

def institution_view(request):
    user = request.user
    return render(request, 'finance/institution.html')

def user_payment(request):
    user = request.user
    return render(request, 'finance/payment.html')

def reimbursement(request):
    user = request.user
    return render(request, 'finance/reimbursement.html')

def institution(request):
    user = request.user
    return render(request, 'finance/institution.html')