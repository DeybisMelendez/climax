from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import QuoteForm, ItemFormset
from .models import Quote
from django.db.models import Q
# PDF GENERATION
from django_weasyprint import WeasyTemplateResponseMixin
from django.views.generic.base import TemplateView


def quote_detail(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    items = quote.item_set.all()
    return render(request, 'quote/detail.html', {'quote': quote, 'items': items})


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
            print("---------- ERROR ----------")
            print("form", form.errors)
            print("formset", formset.errors)

    else:
        form = QuoteForm()
        formset = ItemFormset()

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'quote/update.html', context)


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
    return render(request, 'quote/update.html', context)


def quote_search(request):
    search_query = request.GET.get('q')
    page_number = request.GET.get('p')

    if search_query:

        quotes = Quote.objects.filter(
            Q(number__icontains=search_query) |
            Q(customer__name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(item__description__icontains=search_query)
        ).distinct()
    else:
        quotes = Quote.objects.all().order_by('-number')
    items_per_page = 10  # Número de cotizaciones por página, cambiar por la opción en settings

    paginator = Paginator(quotes, items_per_page)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {
        'quotes': page,
        'search_query': search_query,
    }
    # context = {'quotes': quotes, 'search_query': search_query}
    return render(request, 'quote/search.html', context)


def quote_delete(request, pk):
    quote = get_object_or_404(Quote, pk=pk)

    if request.method == 'POST':
        quote.delete()
        return redirect('quote_search')

    context = {'quote': quote}
    return render(request, 'quote/delete.html', context)


class QuotePDFView(WeasyTemplateResponseMixin, TemplateView):
    model = Quote
    template_name = 'quote/pdf.html'
    pdf_attachment = False

    def get_object(self):
        return get_object_or_404(self.model, pk=self.kwargs.get('pk'))

    def get_pdf_kwargs(self):
        # Agregar opciones de página
        return {
            # 'stylesheets': [settings.STATIC_ROOT + 'css/pdf_styles.css'],
            'presentational_hints': True,
            'page-size': 'Letter',
            'margin-top': '1cm',
            'margin-right': '1cm',
            'margin-bottom': '1cm',
            'margin-left': '1cm',
        }

    def get_pdf_filename(self):
        return f'quote_{self.get_object().pk}.pdf'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quote = self.get_object()
        items = quote.item_set.all()
        context['quote'] = quote
        context["items"] = items
        return context
