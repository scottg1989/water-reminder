from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    joined_date = models.DateTimeField('date joined')

    def __str__(self):
        return self.user_name


class Container(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    volume = models.IntegerField(default=0)
    image_type = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ' - ' + str(self.volume) + 'ml'


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    volume = models.IntegerField(default=0)
    logged_at = models.DateTimeField()
