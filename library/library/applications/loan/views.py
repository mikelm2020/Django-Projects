from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from .models import Loan
from .forms import LoanForm, MultipleLoanForm


class LoanRegister(FormView):
    template_name = "loan/add_loan.html"
    form_class = LoanForm
    success_url = "."

    def form_valid(self, form):

        # Loan.objects.create(
        #     reader=form.cleaned_data["reader"],
        #     book=form.cleaned_data["book"],
        #     loan_date=date.today(),
        #     returned=False,
        # )

        loan = Loan(
            reader=form.cleaned_data["reader"],
            book=form.cleaned_data["book"],
            loan_date=date.today(),
            returned=False,
        )
        loan.save()

        book = form.cleaned_data["book"]
        book.stock = book.stock - 1
        book.save()

        return super(LoanRegister, self).form_valid(form)


class LoanAdd(FormView):
    template_name = "loan/add_loan.html"
    form_class = LoanForm
    success_url = "."

    def form_valid(self, form):

        var_object, created = Loan.objects.get_or_create(
            reader=form.cleaned_data["reader"],
            book=form.cleaned_data["book"],
            returned=False,
            defaults={"loan_date": date.today()},
        )

        if created:
            return super(LoanAdd, self).form_valid(form)
        else:
            return HttpResponseRedirect("/")


class MultipleAddLoan(FormView):
    template_name = "loan/multiple_add_loan.html"
    form_class = MultipleLoanForm
    success_url = "."

    def form_valid(self, form):
        loans = []
        for book in form.cleaned_data["books"]:
            loan = Loan(
                reader=form.cleaned_data["reader"],
                book=book,
                loan_date=date.today(),
                returned=False,
            )
            loans.append(loan)
        Loan.objects.bulk_create(loans)

        return super(MultipleAddLoan, self).form_valid(form)
