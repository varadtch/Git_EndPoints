from django.db import models


class Userdatabase(models.Model):
    id = models.CharField("Emp_ID", max_length=5, primary_key=True)
    username = models.CharField("Username", max_length=10)
    email = models.EmailField("Email")
    profession = models.CharField("Profession", max_length=25)
    city = models.CharField("City", max_length=15)
    state = models.CharField("State", max_length=15)

    def __str__(self):
        return "%s" %self.id
