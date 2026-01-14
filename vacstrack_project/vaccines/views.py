from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import VaccineLog
from .forms import VaccineLogForm


@login_required
def dashboard(request):
    vaccines = VaccineLog.objects.filter(user=request.user).order_by('-date_administered')
    context = {'vaccines': vaccines}
    return render(request, 'vaccines/dashboard.html', context)


@login_required
def vaccine_list(request):
    return redirect('dashboard')  # I will create a separate list later.


@login_required
def vaccine_create(request):
    if request.method == 'POST':
        form = VaccineLogForm(request.POST)
        if form.is_valid():
            vaccine = form.save(commit=False)
            vaccine.user = request.user
            vaccine.save()
            return redirect('dashboard')
    else:
        form = VaccineLogForm()
    return render(request, 'vaccines/vaccine_form.html', {'form': form})
