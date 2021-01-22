import math
from django.db import models
from django.core import validators
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


def check_age(value):
    f, i = math.modf(value)
    if not (f == 0.0 or f == 0.5) or value > 8:
        raise ValidationError('0.5 刻み、8 以下で入力してください(0, 0.5, 1, 1.5...8)')


class Item(models.Model):

    NAME_CHOICES = (
        ('01山崎', '01山崎'),
        ('02青柳', '02青柳'),
        ('04小田島', '04小田島'),
        ('05桑島', '05桑島'),
        ('07高橋', '07高橋'),
        ('08吉田', '08吉田'),
        ('09関', '09関'),
        ('11小林', '11小林'),
        ('12井上', '12井上'),
        ('13高村', '13高村'),
        ('14太田', '14太田'),
        ('17八鍬', '17八鍬'),
        ('19福本', '19福本'),
        ('21井田', '21井田'),
        ('22山口', '22山口'),
        ('25服部', '25服部'),
        ('26亀井', '26亀井'),
        ('28小島', '28小島'),
        ('29渡邉', '29渡邉'),
        ('30藤澤', '30藤澤'),
        ('31岩井', '31岩井'),
        ('32門脇', '32門脇'),
        ('33小林', '33小林'),
        ('35佐々木', '35佐々木'),
        ('36吉田', '36吉田'),
        ('37松崎', '37松崎'),
        ('38木村', '38木村'),
        ('39田中', '39田中'),
    )

    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric are allowed.')

    name = models.CharField(
        verbose_name='名前',
        choices=NAME_CHOICES,
        max_length=20,
    )

    takuhaikenpin = models.IntegerField(
        verbose_name='宅配検品(@400)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                  validators.MaxValueValidator(300)]
    )

    sonotakenpin = models.IntegerField(
        verbose_name='その他検品(@200)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(999)]
    )

    nyuukosyouhinka = models.IntegerField(
        verbose_name='入庫商品化(@200)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(999)]
    )

    shiiresyouhinka = models.IntegerField(
        verbose_name='仕入商品化(@100)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(5000)]
    )

    cleaning = models.IntegerField(
        verbose_name='クリーニング(@50)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(5000)]
    )

    dataerase = models.IntegerField(
        verbose_name='データイレース(@50)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(999)]
    )

    shiirePC = models.IntegerField(
        verbose_name='仕入PC(@1000)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(999)]
    )

    SIMlockkaijo = models.IntegerField(
        verbose_name='SIMロック解除(@200)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(999)]
    )

    tsutaya = models.DecimalField(
        verbose_name='TSUTAYA関連(h) ※0.5h刻みで入力',
        # blank=True,
        null=True,
        max_digits=5,
        decimal_places=1,
        default=0,
        validators=[check_age]
    )

    takuhaikaikon = models.DecimalField(
        verbose_name='宅配開梱(h) ※0.5h刻みで入力',
        # blank=True,
        null=True,
        max_digits=5,
        decimal_places=1,
        default=0,
        validators=[check_age]
    )

    picking = models.DecimalField(
        verbose_name='搬出・ﾋﾟｯｷﾝｸﾞ・ゴミ分別(h) ※0.5h刻みで入力',
        # blank=True,
        null=True,
        max_digits=5,
        decimal_places=1,
        default=0,
        validators=[check_age]
    )

    datanyuuryoku = models.DecimalField(
        verbose_name='データ入力・画像登録(h) ※0.5h刻みで入力',
        # blank=True,
        null=True,
        max_digits=5,
        decimal_places=1,
        default=0,
        validators=[check_age]
    )

    soukin = models.DecimalField(
        verbose_name='送金関連業務(h) ※0.5h刻みで入力',
        # blank=True,
        null=True,
        max_digits=5,
        decimal_places=1,
        default=0,
        validators=[check_age]
    )

    hensou = models.DecimalField(
        verbose_name='返送関連業務(h) ※0.5h刻みで入力',
        # blank=True,
        null=True,
        max_digits=5,
        decimal_places=1,
        default=0,
        validators=[check_age]
    )

    lanksatei = models.DecimalField(
        verbose_name='ランク査定(h) ※0.5h刻みで入力',
        # blank=True,
        null=True,
        max_digits=5,
        decimal_places=1,
        default=0,
        validators=[check_age]
    )

    # sex = models.IntegerField(
    #     verbose_name='性別',
    #     choices=SEX_CHOICES,
    #     default=1
    # )

    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        verbose_name='登録日',
        # auto_now_add=True
        default=timezone.now
    )

    tmp = models.BooleanField(
        verbose_name='一時保存(本登録時はチェックを外してください)',
        default=True,
        # editable=False,
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '日報'
        verbose_name_plural = '日報'
