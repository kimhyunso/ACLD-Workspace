from django.db import models


class Agent(models.Model):
    agent_no = models.AutoField(primary_key=True)
    mac_address_fk = models.ForeignKey('Employee', models.DO_NOTHING, db_column='MAC_Address_FK')  # Field name made lowercase.
    log_no_fk = models.ForeignKey('Log', models.DO_NOTHING, db_column='log_no_FK')  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agent'


class Department(models.Model):
    part_no_pk = models.AutoField(db_column='part_no_PK', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=10)
    position = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'department'


class Employee(models.Model):
    mac_address_pk = models.CharField(db_column='MAC_Address_PK', primary_key=True, max_length=20)  # Field name made lowercase.
    part_no_fk = models.ForeignKey(Department, models.DO_NOTHING, db_column='part_no_FK')  # Field name made lowercase.
    name = models.CharField(max_length=10)
    employee_img_path = models.TextField()
    phone_number = models.IntegerField()
    position = models.CharField(max_length=10)
    rank = models.IntegerField()
    join_day = models.DateTimeField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employee'


class Log(models.Model):
    log_no_pk = models.AutoField(db_column='log_no_PK', primary_key=True)  # Field name made lowercase.
    camimage_path = models.TextField(db_column='CAMimage_path')  # Field name made lowercase.
    screenshot_path = models.TextField()
    detectiontype = models.IntegerField()
    status = models.IntegerField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log'


class Report(models.Model):
    report_no_pk = models.AutoField(db_column='report_no_PK', primary_key=True)  # Field name made lowercase.
    log_no_fk = models.ForeignKey(Log, models.DO_NOTHING, db_column='log_no_FK')  # Field name made lowercase.
    content = models.TextField()
    status = models.IntegerField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'report'