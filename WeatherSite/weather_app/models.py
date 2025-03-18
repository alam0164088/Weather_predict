from django.db import models

class WeatherRequest(models.Model):
    location = models.CharField(max_length=100)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location