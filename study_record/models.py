from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
  """
  データ定義クラス
  """
  
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL, 
    on_delete=models.CASCADE,
    verbose_name='登録者',
    )
  
  category = models.CharField( # カテゴリ
    verbose_name='カテゴリ',
    max_length=200,
    blank=True,
    )
  
  item = models.CharField( # 勉強項目
    verbose_name='勉強項目',
    max_length=200,
    blank=True,
    )
  
  start_time = models.IntegerField(
    verbose_name='勉強開始時間',
    null=True,
    ) # 勉強開始時間
  
  end_time = models.IntegerField(
    verbose_name='勉強終了時間',
    null=True,
    ) # 勉強終了時間
  
  study_length = models.IntegerField(
    verbose_name='勉強時間の長さ',
    null=True,
    ) # 勉強時間の長さ
  
  study_date = models.DateField(
    verbose_name='勉強日',
    null=True,
  )
  
  text = models.TextField( # メモ
    verbose_name='メモ',
    blank=True,
    null=True,
    )
  
  created_date = models.DateTimeField(default=timezone.now)
  
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
      self.published_date = timezone.now()
      self.save()

  def __str__(self):
      return "{}({}-{}/{})".format(self.item,self.start_time,self.end_time,self.study_date)
