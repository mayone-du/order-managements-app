from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

ORDERED_SERVICES_LIST = (
  "LINEスタンプ", "LINEスタンプ"
),(
  "LINE絵文字", "LINE絵文字"
),(
  "イラスト", "イラスト"
),(
  "アイコン", "アイコン"
),(
  "キャラクター", "キャラクター"
),(
  "名刺", "名刺"
),(
  "その他", "その他"
)

ORDERED_MEDIA_LIST = (
  "ホームページ", "ホームページ"
),(
  "ココナラ", "ココナラ"
),(
  "SNS", "SNS"
),(
  "直接", "直接"
),(
  "その他", "その他"
)

PERSONAL_OR_CORPORATE = (
  "個人", "個人",
),(
  "法人", "法人"
)

class OrderManagementsModel(models.Model):
  ordered_services = models.CharField(max_length=100, choices=ORDERED_SERVICES_LIST)
  ordered_services_memo = models.TextField(max_length=1000, null=True, blank=True)
  thumbnail = models.ImageField(upload_to="", null=True, blank=True)
  ordered_media = models.CharField(max_length=100, choices=ORDERED_MEDIA_LIST)
  personal_or_corporate = models.CharField(max_length=50, choices=PERSONAL_OR_CORPORATE)
  option = models.TextField(max_length=500, null=True, blank=True)
  order_date = models.DateTimeField(null=True, blank=True)
  delivery_date = models.DateTimeField(null=True, blank=True)
  order_price = models.IntegerField(default=0, null=True, blank=True)
  sales_amount = models.IntegerField(default=0, null=True, blank=True)
  create_user = models.CharField(max_length=50, default="")
  review_count = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
  review_text = models.TextField(max_length=1000, null=True, blank=True)

  def __str__(self):
    return str(self.pk) + ":" + self.create_user