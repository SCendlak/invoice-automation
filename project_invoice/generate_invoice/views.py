import os
from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Contact, Invoice
from .forms import ContactForm, InvoiceForm, UploadBaseInvoiceForm
from .helpers.pdf import PdfToExcel
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


class ContactListView(generic.ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'contact_list.html'

    def get_context_data(self, **kwargs):
        context = super(ContactListView, self).get_context_data(**kwargs)
        return context


class ContactDetailView(generic.TemplateView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'contact_detail.html'


@login_required
def index(request):
    context = {
        'current_url': request.path,
        'current_user': request.user
    }
    return render(request, 'base_generic.html', context=context)


@login_required
def upload_pdf(request):
    if request.method == 'POST':
        form = UploadBaseInvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the PDF
            temp_pdf_path = handle_uploaded_file(request.FILES['file'])
            pdf_processor = PdfToExcel()
            text = pdf_processor.extract_text_from_pdf(temp_pdf_path)
            table_dict = pdf_processor.create_general_table(text)
            request.session['table_dict'] = table_dict
            return redirect('invoice:show_results')
    else:
        form = UploadBaseInvoiceForm()
    return render(request, 'upload_pdf.html', {'form': form, 'current_user': request.user})


@login_required
def show_results(request):
    if request.method == 'POST':

        form = InvoiceForm(request.POST, request.FILES)
        print(form.data)

        if form.is_valid():
            table = request.session['table_dict']['table']
            temp_excel_path = os.path.join(settings.MEDIA_ROOT)
            pdf_processor = PdfToExcel()
            form.cleaned_data['username'] = request.user.username
            today = datetime.today()
            invoices = Invoice.objects.all()
            today_invoices = invoices is not None and invoices.filter(created_at__day=today.day,
                                                                      created_at__month=today.month,
                                                                      created_at__year=today.year)
            file_name = pdf_processor.create_workbook(index=len(today_invoices)+1,
                                                      table=table,
                                                      path_excel=str(temp_excel_path),
                                                      data=form.cleaned_data)
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            if os.path.exists(file_path):
                Invoice(title=file_name, index=len(today_invoices)+1).save()
                return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
            else:
                return HttpResponseRedirect(redirect('invoice:index'))
    else:
        form = InvoiceForm()
    context = {'form': form, 'pdf_data': request.session['table_dict'], 'current_user': request.user}

    return render(request, 'generate.html', context=context)


def handle_uploaded_file(f):
    fs = FileSystemStorage()
    filename = fs.save(f.name, f)
    return fs.path(filename)


@login_required
def contacts(request):
    context = {
        'contacts': Contact.objects.all(),
        'current_url': request.path,
        'current_user': request.user
    }
    return render(request, 'contact_list.html', context)


@login_required
def contact_detail_view(request, name):
    contact = get_object_or_404(Contact, name=name)
    return render(request, 'contact_detail.html', context={'contact': contact, 'current_user': request.user})


@login_required
def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("contacts"))
        else:
            messages.error(request, "Please correct the error below.")

    else:
        form = ContactForm()

    context = {
        'form': form,
        'current_url': request.path,
        'current_user': request.user
    }

    return render(request, 'add_contact.html', context=context)
