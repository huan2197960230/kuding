from django.db import models


class Student(models.Model):
    s_id = models.CharField(max_length=36, primary_key=True)
    s_account = models.CharField(max_length=32,unique=True, verbose_name="账号")
    s_password = models.CharField(max_length=32, verbose_name="密码")
    s_name = models.CharField(max_length=32, verbose_name="姓名", db_index=True)
    s_sex = models.BooleanField(verbose_name="性别")
    s_state = models.BooleanField(verbose_name="状态")
    s_create_time = models.DurationField(verbose_name="创建时间")
    s_grade = models.CharField(max_length=32 ,verbose_name="年级",null=True,blank=True)
    s_head_image = models.ImageField(verbose_name="头像",null=True,blank=True)
    s_remark = models.CharField(max_length=255, verbose_name="备注",null=True,blank=True)
    s_email = models.EmailField(max_length=32, verbose_name="邮箱",null=True,blank=True)

    class Meta:
        verbose_name_plural = '学生表'

    def __str__(self):
        return self.s_name

class Teacher(models.Model):
    t_id = models.CharField(max_length=36, primary_key=True)
    t_account = models.CharField(max_length=32,unique=True, verbose_name="账号")
    t_password = models.CharField(max_length=32, verbose_name="密码")
    t_name = models.CharField(max_length=100, verbose_name="姓名",db_index=True)
    t_age = models.IntegerField(verbose_name="年龄",null=True,blank=True)
    t_sex = models.BooleanField(verbose_name="性别")
    t_state = models.BooleanField(verbose_name="状态")
    t_create_time = models.DurationField(verbose_name="创建时间")
    t_degree = models.CharField(max_length=32 ,verbose_name="学位",null=True,blank=True)
    t_detail = models.CharField(max_length=255, verbose_name="简介",null=True,blank=True)
    t_head_image = models.ImageField(verbose_name="头像",null=True,blank=True)
    t_remark = models.CharField(max_length=255, verbose_name="备注",null=True,blank=True)

    class Meta:
        verbose_name_plural = '老师表'

    def __str__(self):
        return self.t_name

class Course(models.Model):
    c_id = models.CharField(max_length=36, primary_key=True)
    c_name = models.CharField(max_length=64, verbose_name="课程名称",db_index=True)
    c_create_time = models.DurationField(verbose_name="创建时间")
    c_detail = models.CharField(max_length=255, verbose_name="课程介绍",null=True,blank=True)
    c_count = models.IntegerField(verbose_name="课程总数")
    c_remark = models.CharField(max_length=255, verbose_name="备注",null=True,blank=True)

    class Meta:
        verbose_name_plural = '课程表'

    def __str__(self):
        return self.c_name

class Detail(models.Model):
    d_id = models.CharField(max_length=36, primary_key=True)
    d_name = models.CharField(max_length=64, verbose_name="节课程名称",db_index=True)
    d_number = models.IntegerField(verbose_name="课程第几章")
    d_time_length = models.IntegerField(verbose_name="课程时长")
    d_detail = models.CharField(max_length=255, verbose_name="简介",null=True,blank=True)
    d_create_time = models.DurationField(verbose_name="该科提出创造时间",null=True,blank=True)
    d_cid = models.ForeignKey(to="Course",to_field="c_id",on_delete=models.SET_NULL,blank=True, null=True)
    d_remark = models.CharField(max_length=255, verbose_name="备注", null=True, blank=True)
    class Meta:
        verbose_name_plural = '每门课的详情表'

    def __str__(self):
        return self.d_name

class Evaluate(models.Model):
    e_id = models.CharField(max_length=36, primary_key=True)
    e_ttos_evaluate = models.CharField(max_length=255, verbose_name="老师对学生评价",blank=True, null=True)
    e_stot_evaluate = models.CharField(max_length=255, verbose_name="学生对老师评价",blank=True, null=True)
    e_ttos_score = models.IntegerField(verbose_name="老师对学生的打分",blank=True, null=True)
    e_stot_score = models.IntegerField(verbose_name="学生对老师的打分",blank=True, null=True)
    e_remark = models.CharField(max_length=255, verbose_name="备注",blank=True, null=True)
    e_create_time = models.DurationField( verbose_name="创建时间")
    e_sid = models.ForeignKey(to="Student", to_field="s_id",on_delete=models.SET_NULL,blank=True, null=True)
    e_tid = models.ForeignKey(to="Teacher", to_field="t_id",on_delete=models.SET_NULL,blank=True, null=True)
    e_did = models.ForeignKey(to="Detail", to_field="d_id",on_delete=models.SET_NULL,blank=True, null=True)

    class Meta:
        verbose_name_plural = '评价表'


class Grant(models.Model):
    g_id = models.CharField(max_length=36, primary_key=True)
    g_sid = models.ForeignKey(to="Student", to_field="s_id",on_delete=models.SET_NULL,blank=True, null=True)
    g_tid = models.ForeignKey(to="Teacher", to_field="t_id",on_delete=models.SET_NULL,blank=True, null=True)
    g_did = models.ForeignKey(to="Detail", to_field="d_id",on_delete=models.SET_NULL,blank=True, null=True)
    g_record = models.CharField(max_length=12 ,verbose_name="状态")
    g_time = models.DurationField(verbose_name="时间")
    g_url = models.CharField(max_length=255, verbose_name="网址")
    g_remark = models.CharField(max_length=255, verbose_name="备注")

    class Meta:
        verbose_name_plural = '授课进度表'