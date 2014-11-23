from django.db import models

class MyBook(models.Model):
    book_name = models.CharField(max_length=200)
    book_url = models.URLField()
    read_date = models.DateField(blank=True,null=True)
    book_isbn = models.CharField(max_length=50)

    def __unicode__(self):
        return self.book_name

class MyMovie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_url = models.URLField()
    watch_date = models.DateField(blank=True,null=True)

    def __unicode__(self):
        return self.movie_name


