from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from .forms import CustomerForm
from django.db.models import Q


def customer_search(request):
    search_query = request.GET.get('q')

    if search_query:

        customers = Customer.objects.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(ruc__icontains=search_query) |
            Q(phone__icontains=search_query)
        ).distinct()
    else:
        customers = Customer.objects.all()
    context = {"customers": customers}
    return render(request, 'customer/search.html', context)


def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_search")
    form = CustomerForm()
    context = {"form": form}
    return render(request, "customer/update.html", context)


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('customer_search', pk=customer.pk)
        else:
            if form.errors:
                print("form:", form.errors)
    context = {
        'form': form,
    }
    return render(request, 'customer/update.html', context)


def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_search')

    context = {'customer': customer}
    return render(request, 'customer/delete.html', context)
