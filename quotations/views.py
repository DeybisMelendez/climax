from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuoteForm, ItemFormset, ItemForm
from django.forms import formset_factory
from .models import Quote


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quote_list.html', {'quotes': quotes})


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
