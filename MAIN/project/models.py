from django.db import models

class Part(models.Model):
    partkey = models.AutoField(db_column='partKey', primary_key=True)
    department = models.CharField(max_length=20)
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'part'


class User(models.Model):
    personkey = models.AutoField(db_column='personKey', primary_key=True)
    fk_partkey = models.ForeignKey(Part, models.DO_NOTHING, db_column='FK_partKey', blank=True, null=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'