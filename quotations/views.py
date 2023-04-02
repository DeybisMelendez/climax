# from .forms import QuoteForm, ItemFormset
from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuoteForm, ItemFormset
# from django.forms import formset_factory
from .models import Quote
from django.db.models import Q


def quote_detail(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    items = quote.item_set.all()
    return render(request, 'quote_detail.html', {'quote': quote, 'items': items})


def quote_create(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        formset = ItemFormset(request.POST)

        if form.is_valid() and formset.is_valid():
            quote = form.save()

            for form in formset:
                if form.is_valid():
                    item = form.save(commit=False)
                    item.quote = quote
                    item.save()

            return redirect('quote_detail', pk=quote.pk)

    else:
        form = QuoteForm()
        formset = ItemFormset()

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'quote_create.html', context)


def quote_update(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    form = QuoteForm(request.POST or None, instance=quote)
    formset = ItemFormset(request.POST or None, instance=quote)
    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():

            form.save()
            formset.save()
            return redirect('quote_detail', pk=quote.pk)
        else:
            if form.errors:
                print("form:", form.errors)
            if formset.errors:
                print("formset:", formset.errors)
    else:
        formset = ItemFormset(instance=quote)

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'quote_update.html', context)


def quote_delete(request, pk):
    quote = get_object_or_404(Quote, pk=pk)

    if request.method == 'POST':
        quote.delete()
        return redirect('quote_search')

    context = {'quote': quote}
    return render(request, 'quote_delete.html', context)


def quote_search(request):
    search_query = request.GET.get('q')

    if search_query:

        quotes = Quote.objects.filter(
            Q(number__icontains=search_query) |
            Q(customer__name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(item__description__icontains=search_query)
        ).distinct()
    else:
        quotes = Quote.objects.all()

    context = {'quotes': quotes, 'search_query': search_query}
    return render(request, 'quote_search.html', context)
