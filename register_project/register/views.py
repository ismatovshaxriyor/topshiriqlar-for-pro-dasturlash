from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Person

# Create your views here.
def main(request):
    form = CustomerForm(request.POST)
    if form.is_valid() and request.POST:
        form.save()
        return redirect("customers-list")
    ctx = {
        "form": form
    }
    return render(request, "index.html", ctx)

def customers_list(request):
    customers = Person.objects.all()
    ctx = {
        "customers": customers
    }
    return render(request, "table.html", ctx)