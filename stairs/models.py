import datetime
from django.db import models

class Programmer(models.Model):
    name = models.TextField()

    def get_count_paired_with(self, programmer_paired_with):
        return Pairing.objects.filter(programmerOne=self, programmerTwo=programmer_paired_with).count()

    def add_pairing_with(self, programmer_paired_with):
        if self.id < programmer_paired_with.id:
            Pairing(programmerOne=self, programmerTwo=programmer_paired_with).save()
        else:
            Pairing(programmerOne=programmer_paired_with, programmerTwo=self).save()


class Pairing(models.Model):
    programmerOne = models.ForeignKey(Programmer, related_name='one')
    programmerTwo = models.ForeignKey(Programmer, related_name='two')
    date = models.DateField(default=datetime.date.today)