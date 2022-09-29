def update_book_stock(sender, instance, **kwargs):
    instance.book.stock = instance.book.stock + 1
    instance.book.save()