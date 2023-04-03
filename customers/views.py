from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from .forms import CustomerForm


def customer_search(request):
    customers = Customer.objects.all()
    context = {"customers": customers}
    return render(request, 'customer/search.html', context)


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {'customer': customer}
    return render(request, 'customer/detail.html', context)


def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_search")
    form = CustomerForm()
    context = {"form": form}
    return render(request, "customer/create.html", context)


def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_search')

    context = {'customer': customer}
    return render(request, 'customer/delete.html', context)
