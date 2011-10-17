from django.db import models

class Programmers(models.Model):
    name = models.TextField()


class Pairing(models.Model):
    programmerOne = models.ForeignKey(Programmers, related_name='one')
    programmerTwo = models.ForeignKey(Programmers, related_name='two')
    count = models.IntegerField(default=0)