from django.db import models


class Employs(models.Model):
    sex_choice = (
        (0, r'男'),
        (1, r'女'),
    )
    position_type = (
        (0, r'经理'),
        (1, r'组长'),
        (2, r'员工'),
    )
    employ_id = models.CharField(max_length=12)
    job = models.CharField(max_length=12)
    name = models.CharField(max_length=20)
    sex = models.IntegerField(choices=sex_choice)
    position = models.IntegerField(choices=position_type, verbose_name="职位")

    def __str__(self):
        return '%s %s' % (self.employ_id, self.name)

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'
        ordering = ['id']


class Leave(models.Model):
    employ_id = models.ForeignKey(Employs, verbose_name="员工号")
    reason = models.TextField()
    date = models.DateTimeField()
    days = models.IntegerField(verbose_name="天数")
    money = models.FloatField(verbose_name="扣款")

    def __str__(self):
        return str(self.money)

    class Meta:
        verbose_name = '请假'
        verbose_name_plural = '请假'
        ordering = ['id']


class Prize(models.Model):
    employ_id = models.ForeignKey(Employs, verbose_name="员工号")
    reason = models.TextField()
    date = models.DateTimeField(null=True, blank=True)
    money = models.FloatField(verbose_name="奖金")

    class Meta:
        verbose_name = '奖金'
        verbose_name_plural = '奖金'
        ordering = ['id']


class Punish(models.Model):
    employ_id = models.ForeignKey(Employs, verbose_name="员工号")
    reason = models.TextField()
    date = models.DateTimeField()
    money = models.FloatField(verbose_name="扣款")

    class Meta:
        verbose_name = '扣款'
        verbose_name_plural = '扣款'
        ordering = ['id']


class Type(models.Model):
    type_choice = (
        ('银行卡', '银行卡'),
        ('现金', '现金'),
        ('支票', '支票'),
    )
    employ_id = models.ForeignKey(Employs, verbose_name="员工号")
    pay_type = models.CharField(max_length=20,choices=type_choice, verbose_name='付款类型')
    car_number = models.CharField(max_length=40,verbose_name="卡号", null=True, blank=True)

    def __str__(self):
        return str(self.pay_type)

    class Meta:
        verbose_name = '付款类型'
        verbose_name_plural = '付款类型'
        ordering = ['id']


class Salary(models.Model):
    employ_id = models.ForeignKey(Employs, verbose_name="员工号")
    pay_type = models.ForeignKey(Type)
    base_salary = models.FloatField(verbose_name='基本工资')
    date = models.DateTimeField(verbose_name='发款日期')
    total_punish = models.FloatField(verbose_name='总扣款')
    total_prize = models.FloatField(verbose_name='总奖金')
    total_salary = models.FloatField(verbose_name='应得工资')

    def __str__(self):
        return str(self.total_prize)

    class Meta:
        verbose_name = '工资表'
        verbose_name_plural = '工资表'
        ordering = ['id']
