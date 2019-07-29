from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
class NewBlog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    writer = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]