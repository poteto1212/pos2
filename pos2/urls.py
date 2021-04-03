from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from .import settings

urlpatterns = [
    path('',include('timeline.urls')),
    path('admin/', admin.site.urls),
]

#include→引数のurl.pyに処理を任せる

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#投稿画像ディレクトリをurlで紐づけ
#path以外をurlpatternsに直接組み込むと正常に動作しない
#原因はstatic関数の仕様によるもの