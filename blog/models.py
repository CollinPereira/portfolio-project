from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        sum=self.body[:100]
        return sum

    def pub_date_pretty(self):
        date=self.pub_date.strftime("%d %B, %Y")
        return date    