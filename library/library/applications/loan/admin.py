from django.contrib import admin

from .models import Loan, Reader


class ReaderAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'last_name', 'nationality', 'age')
    list_filter = ('nationality',)
    search_fields = ('id', 'name', 'last_name', 'nationality', 'age')
    ordering = ('id',)
    
class LoanAdmin(admin.ModelAdmin):

    list_display = ('id', 'loan_date', 'return_date', 'returned', 'book', 'reader')
    list_filter = ('book',)
    search_fields = ('id', 'loan_date', 'return_date', 'returned', 'book', 'reader')
    date_hierarchy = 'loan_date'
    ordering = ('id',)



admin.site.register(Loan, LoanAdmin)
admin.site.register(Reader, ReaderAdmin)


