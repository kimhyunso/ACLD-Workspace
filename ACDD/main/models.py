from django.db import models

class Agent(models.Model):
    agent_no = models.IntegerField(primary_key=True)
    status = models.IntegerField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'agent'



class Dection(models.Model):
    dect_no = models.AutoField(primary_key=True)
    emp_no = models.ForeignKey('Employee', models.DO_NOTHING, db_column='emp_no')
    cam_path = models.CharField(db_column='CAM_path', max_length=300)  # Field name made lowercase.
    screen_path = models.CharField(max_length=300)
    detectiontype = models.IntegerField()
    status = models.IntegerField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dection'


class Department(models.Model):
    depmt_no = models.AutoField(primary_key=True)
    depmt_name = models.CharField(max_length=20)
    landline = models.IntegerField()
    location = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'department'


class Employee(models.Model):
    emp_no = models.CharField(primary_key=True, max_length=20)
    depmt_no = models.ForeignKey(Department, models.DO_NOTHING, db_column='depmt_no')
    emp_name = models.CharField(max_length=10)
    emp_img_path = models.TextField()
    phone_no = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    rank = models.IntegerField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employee'


class Identify(models.Model):
    ident_no = models.AutoField(primary_key=True)
    emp_no = models.ForeignKey(Employee, models.DO_NOTHING, db_column='emp_no')
    agent_no = models.ForeignKey(Agent, models.DO_NOTHING, db_column='agent_no')
    ip = models.CharField(db_column='IP', max_length=100)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'identify'


class Report(models.Model):
    report_no = models.AutoField(primary_key=True)
    dect_no = models.ForeignKey(Dection, models.DO_NOTHING, db_column='dect_no')
    content = models.TextField()
    status = models.IntegerField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'report'