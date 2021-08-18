from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)            # 發布會標題
    limit = models.IntegerField()                      # 限制人數
    status = models.BooleanField()                     # 狀態
    address = models.CharField(max_length=200)         # 地址
    start_time = models.DateTimeField('events time')   # 發布會時間
    create_time = models.DateTimeField(auto_now=True)  # 創建時間（自動獲取當前時間）

    def __str__(self):
        return self.name

class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # 關聯發布會id
    realname = models.CharField(max_length=64)  # 姓名
    phone = models.CharField(max_length=16)     # 手機號
    email = models.EmailField()                 # email
    sign = models.BooleanField()                # 簽到狀態
    create_time = models.DateTimeField(auto_now=True)  # 創建時間（自動獲取當前時間）

    class Meta:
        unique_together = ('phone', 'event')
        ordering = ['-id']

    def __str__(self):
        return self.realname