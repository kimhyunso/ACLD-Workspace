from django.db import models


class Cam(models.Model):
    cam_pk = models.AutoField(db_column='cam_PK', primary_key=True)  # Field name made lowercase.
    ip_fk = models.ForeignKey('Pcinfo', models.DO_NOTHING, db_column='IP_FK')  # Field name made lowercase.
    camimagepath = models.CharField(db_column='CAMimagePATH', max_length=100)  # Field name made lowercase.
    screentshortpath = models.CharField(db_column='ScreentShortPATH', max_length=100)  # Field name made lowercase.
    detectiontype = models.CharField(db_column='DetectionType', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cam'


class Employee(models.Model):
    employee_pk = models.AutoField(db_column='employee_PK', primary_key=True)  # Field name made lowercase.
    ip_fk = models.ForeignKey('Pcinfo', models.DO_NOTHING, db_column='IP_FK')  # Field name made lowercase.
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'employee'


class Pcinfo(models.Model):
    ip_pk = models.CharField(db_column='IP_PK', primary_key=True, max_length=100)  # Field name made lowercase.
    pcinfo = models.CharField(db_column='PCInfo', max_length=50)  # Field name made lowercase.   
    userinfo = models.CharField(db_column='UserInfo', max_length=50)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=50)  # Field name made lowercase.
    dateinfo = models.DateTimeField(db_column='DateInfo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pcinfo'


class Report(models.Model):
    ip_fk = models.ForeignKey(Pcinfo, models.DO_NOTHING, db_column='IP_FK')  # Field name made lowercase.
    content = models.CharField(max_length=10000)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'report'