from django.db import models
from bills import models as bill_models

# Create your models here.


class Event(models.Model):
    event_id = models.AutoField(db_column='eventId', primary_key=True)
    title = models.CharField(max_length=200)
    desciption = models.TextField(null=True)
    start_date = models.DateTimeField(
        db_column='startDate', default='2020-11-30')
    end_date = models.DateTimeField(db_column='endDate', default='2020-11-30')
    user_id = models.ForeignKey(
        bill_models.Users, db_column='userId', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reversed('cal:event-details', args=(self.event_id))

    @property
    def get_html_url(self):
        url = reversed('cal:event-details', args=(self.event_id))
        return f'<a href="{url}"> {self.title} </a>'
