from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Entry, Exit
from .forms import ProductForm, EntryForm, ExitForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'inventory/product_detail.html', {'product': product})


def entry_list(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    entries = Entry.objects.filter(product_id=product)
    return render(request, 'inventory/entry_list.html', {'product': product, 'entries': entries})


def exit_list(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    exits = Exit.objects.filter(product_id=product)
    return render(request, 'inventory/exit_list.html', {'product': product, 'exits': exits})


def add_entry(request, entry_id):  # TODO: hacer bien
    product = Entry.objects.get(pk=entry_id)
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            # entry.product_id = product
            entry.save()
            return redirect('entry_list', product_id=entry_id)
    else:
        form = EntryForm(instance=product)
    return render(request, 'inventory/add_entry.html', {'form': form, 'product': product})


def add_exit(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ExitForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.product_id = product
            entry.save()
            return redirect('exit_list', product_id=product_id)
    else:
        form = EntryForm(instance=product)
    return render(request, 'inventory/add_exit.html', {'form': form, 'product': product})


def add_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory/product_detail', product_id=product_id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/add_product.html', {'form': form, 'product': product})
