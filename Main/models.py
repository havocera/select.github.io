from django.db import models

# Create your models here.
class Area(models.Model):
    '''
    座位分区
    '''
    name = models.CharField(max_length = 50,verbose_name = '分区名')
    set_count = models.IntegerField(default=10, verbose_name='座位数')
    class Meta:
        verbose_name = "座位分区"

        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name


class Set(models.Model):
    area = models.ForeignKey(Area,verbose_name = '所在区',on_delete = models.CASCADE)
    set_no = models.CharField(max_length = 20,verbose_name = '座位号')
    status = models.BooleanField(verbose_name= '预定状态')
    user = models.CharField(max_length = 50,verbose_name = '预定人',blank = True)
    mobile = models.IntegerField(verbose_name='手机号')
    price = models.IntegerField(verbose_name='价格',default=100)
    start_day = models.DateField(verbose_name= '开始时间',blank = False)
    end_day = models.DateField(verbose_name= '结束时间',blank = False)
    counts = models.IntegerField(verbose_name= '预订次数',default= 0)
    order =models.IntegerField(default=0,verbose_name='优先级')
    class Meta:
        verbose_name= '座位管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return  "{}区-{}号".format(self.area, self.set_no)


