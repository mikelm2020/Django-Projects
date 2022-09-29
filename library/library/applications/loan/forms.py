from django import forms

from applications.book.models import Book
from .models import Loan


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ["reader", "book"]


class MultipleLoanForm(forms.ModelForm):

    books = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Loan
        fields = ["reader"]

    def __init__(self, *args, **kwargs):
        super(MultipleLoanForm, self).__init__(*args, **kwargs)
        self.fields['books'].queryset = Book.objects.all()
