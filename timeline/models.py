from django.db import models
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFill,ResizeToFit

#投稿作成に必要な情報は投稿ID　投稿ユーザーID　　本文や写真　投稿日時
class Post(models.Model):
    #投稿内容と投稿者アカウント情報の紐づけ
    author=models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    text=models.TextField(verbose_name='本文')
    photo=models.ImageField(verbose_name='写真',blank=True,null=True,upload_to='images/')
    #photoカラムから投稿画像を生成する
    post_photo=ImageSpecField(source='photo',processors=[ResizeToFit(1080,1080)],format='JPEG',options={'quality':60})
    created_at=models.DateTimeField(auto_now_add=True,blank=True)
    
    
    #「ほめる」をしてくれたユーザー情報の取得する関数(配列として返す)
    def get_like(self):
        likes=Like.objects.filter(post=self)
        return [like.user for like in likes]#for文の内包表記[繰り返す式　for 変数　in オブジェクト]
    # Create your models here.

#「ほめる」をする為に必要な情報はほめる側のユーザーIDと投稿ID
class Like(models.Model):
    user=models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    post=models.ForeignKey('Post',on_delete=models.CASCADE)#
    
    class Meta:
        unique_together=('user','post')
    