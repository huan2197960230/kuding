# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WebCourse(models.Model):
    c_id = models.CharField(primary_key=True, max_length=36)
    c_name = models.CharField(max_length=64)
    c_create_time = models.BigIntegerField()
    c_detail = models.CharField(max_length=255, blank=True, null=True)
    c_count = models.IntegerField()
    c_remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_course'
        verbose_name = "课程"
        verbose_name_plural = verbose_name


class WebDetail(models.Model):
    d_id = models.CharField(primary_key=True, max_length=36)
    d_name = models.CharField(max_length=64)
    d_number = models.IntegerField()
    d_time_length = models.IntegerField()
    d_detail = models.CharField(max_length=255, blank=True, null=True)
    d_create_time = models.BigIntegerField(blank=True, null=True)
    d_remark = models.CharField(max_length=255, blank=True, null=True)
    d_cid = models.ForeignKey(WebCourse, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_detail'
        verbose_name = "课程详情"
        verbose_name_plural = verbose_name


class WebEvaluate(models.Model):
    e_id = models.CharField(primary_key=True, max_length=36)
    e_ttos_evaluate = models.CharField(max_length=255, blank=True, null=True)
    e_stot_evaluate = models.CharField(max_length=255, blank=True, null=True)
    e_ttos_score = models.IntegerField(blank=True, null=True)
    e_stot_score = models.IntegerField(blank=True, null=True)
    e_remark = models.CharField(max_length=255, blank=True, null=True)
    e_create_time = models.BigIntegerField()
    e_did = models.ForeignKey(WebDetail, models.DO_NOTHING, blank=True, null=True)
    e_sid = models.ForeignKey('WebStudent', models.DO_NOTHING, blank=True, null=True)
    e_tid = models.ForeignKey('WebTeacher', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_evaluate'
        verbose_name = "评价"
        verbose_name_plural = verbose_name


class WebGrant(models.Model):
    g_id = models.CharField(primary_key=True, max_length=36)
    g_record = models.CharField(max_length=12)
    g_time = models.BigIntegerField()
    g_url = models.CharField(max_length=255)
    g_remark = models.CharField(max_length=255)
    g_did = models.ForeignKey(WebDetail, models.DO_NOTHING, blank=True, null=True)
    g_sid = models.ForeignKey('WebStudent', models.DO_NOTHING, blank=True, null=True)
    g_tid = models.ForeignKey('WebTeacher', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_grant'
        verbose_name = "进度"
        verbose_name_plural = verbose_name


class WebStudent(models.Model):
    s_id = models.CharField(primary_key=True, max_length=36)
    s_account = models.CharField(unique=True, max_length=32)
    s_password = models.CharField(max_length=32)
    s_name = models.CharField(max_length=32)
    s_sex = models.IntegerField()
    s_state = models.IntegerField()
    s_create_time = models.BigIntegerField()
    s_grade = models.CharField(max_length=32, blank=True, null=True)
    s_head_image = models.CharField(max_length=100, blank=True, null=True)
    s_remark = models.CharField(max_length=255, blank=True, null=True)
    s_email = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_student'
        verbose_name = "学生"
        verbose_name_plural = verbose_name


class WebTeacher(models.Model):
    t_id = models.CharField(primary_key=True, max_length=36)
    t_account = models.CharField(unique=True, max_length=32)
    t_password = models.CharField(max_length=32)
    t_name = models.CharField(max_length=100)
    t_age = models.IntegerField(blank=True, null=True)
    t_sex = models.IntegerField()
    t_state = models.IntegerField()
    t_create_time = models.BigIntegerField()
    t_degree = models.CharField(max_length=32, blank=True, null=True)
    t_detail = models.CharField(max_length=255, blank=True, null=True)
    t_head_image = models.CharField(max_length=100, blank=True, null=True)
    t_remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_teacher'
        verbose_name = "教师"
        verbose_name_plural = verbose_name
