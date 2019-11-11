from django.db import models

class BRoast(models.Model):
    boast_or_roast = models.BooleanField()
    content = models.CharField(max_length=280)
    upboats = models.IntegerField(default=0)
    downrowts = models.IntegerField(default=0)
    time_submit = models.DateTimeField(auto_now_add=True)