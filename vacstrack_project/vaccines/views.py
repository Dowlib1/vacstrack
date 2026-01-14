from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import VaccineLog
from .forms import VaccineLogForm
from django.contrib import messages

@login_required
def dashboard(request):
    user = request.user
    today = timezone.now().date()
    upcoming = VaccineLog.objects.filter(user=user, next_due_date__isnull=False, next_due_date__gte=today).order_by('next_due_date')[:10]
    recent = VaccineLog.objects.filter(user=user).order_by('-date_administered')[:5]
    return render(request, 'vaccines/dashboard.html', {'upcoming': upcoming, 'recent': recent})

@login_required
def vaccine_list(request):
    qs = VaccineLog.objects.filter(user=request.user).order_by('-date_administered')
    return render(request, 'vaccines/vaccine_list.html', {'vaccines': qs})

@login_required
def vaccine_create(request):
    if request.method == 'POST':
        form = VaccineLogForm(request.POST)
        if form.is_valid():
            v = form.save(commit=False)
            v.user = request.user
            v.save()
            messages.success(request, "Vaccine log added.")
            return redirect('vaccines:list')
    else:
        form = VaccineLogForm()
    return render(request, 'vaccines/vaccine_form.html', {'form': form})

@login_required
def vaccine_update(request, pk):
    v = get_object_or_404(VaccineLog, pk=pk, user=request.user)
    if request.method == 'POST':
        form = VaccineLogForm(request.POST, instance=v)
        if form.is_valid():
            form.save()
            messages.success(request, "Vaccine log updated.")
            return redirect('vaccines:list')
    else:
        form = VaccineLogForm(instance=v)
    return render(request, 'vaccines/vaccine_form.html', {'form': form, 'object': v})

@login_required
def vaccine_delete(request, pk):
    v = get_object_or_404(VaccineLog, pk=pk, user=request.user)
    if request.method == 'POST':
        v.delete()
        messages.success(request, "Vaccine log deleted.")
        return redirect('vaccines:list')
    return render(request, 'vaccines/vaccine_confirm_delete.html', {'object': v})
