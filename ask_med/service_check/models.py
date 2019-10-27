from django.db import models

class InsuranceCompany(models.Model):
    polis_ltd_sk = models.CharField(max_length=50)
    polis_ltd_id = models.CharField(max_length=50)
    polis_ltd_type = models.CharField(max_length=10)
    polis_ltd_date_end = models.CharField(max_length=50)
    polis_ltd_tel = models.CharField(max_length=50)

    def __str__(self):
        return self.polis_ltd_sk #+ '' + self.polis_ltd_id + '' + self.polis_ltd_type + '' + self.polis_ltd_date_end + '' + self.polis_ltd_tel
    

class Services(models.Model):
    polis_ltd_outservice = models.TextField(max_length=200)
    polis_ltd_inclusion = models.CharField(max_length=50)

    def __str__(self):
        return self.polis_ltd_outservice + '' + self.polis_ltd_inclusion