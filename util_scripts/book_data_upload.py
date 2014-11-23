import json
from dateutil.parser import parse

from kmadswebsite.models import MyBook


def save_book_data(book_data_fname):
    book_data = []
    with open(book_data_fname, 'r') as f:
        book_data = json.load(f)

    for book in book_data:
        #print book
        if book['date_finished']:
            finished_time_parsed = parse(book['date_finished'])
        else:
            finished_time_parsed = None

        b = MyBook(book_name=book['title'], book_url=book['amazon_link'], 
                        read_date=finished_time_parsed, book_isbn=book['isbn'])
        b.save()
        print "saved book %s" % b


