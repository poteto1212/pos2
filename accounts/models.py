from django.db import models
from django.contrib.auth.models import AbstractUser#Userモデルを全て継承している
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFill

class CustomUser(AbstractUser):#abstrctouserではユーザー情報のみ。CustomUserではこれに加えて各種機能
    #プロフィール投稿機能
    description=models.TextField(verbose_name='プロフィール',null=True,blank=True)
    #画像投稿機能#多重継承でファイルに繋がっている。
    photo=models.ImageField(verbose_name='写真',blank=True,null=True,upload_to='images/')
    #photoカラムからサムネ画像生成。画素やサイズといった各種設定を自動で行ってくれる関数
    thumunail=ImageSpecField(source='photo',processors=[ResizeToFill(256,256)],#画像のサイズ指定
    format='JPEG',option{'quality':60})#画質指定
    
    class Mata:#付加情報
        verbose_name_plual='CustomUser'
# Create your models here.
