from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.staticfiles.urls import static
from .import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('',include('timeline.urls')),
    path('admin/', admin.site.urls),
   #https://github.com/pennersr/django-allauth/blob/master/allauth/account/urls.pyに渡されている。
    path('accounts/email',RedirectView.as_view(pattern_name="timeline:index")),#RedirectViewはpattern_name変数をreverse関数に渡し,そこからurlを生成している.ここではtimelineアプリにurlを合わせる
    path('accounts/inactive',RedirectView.as_view(pattern_name="timeline:index")),#テンプレートはpostなので
    path('accounts/pathword/change/',RedirectView.as_view(pattern_name="timeline:index")),
    path('accounts/confirm-email/',RedirectView.as_view(pattern_name="timeline:index")),
    re_path('accounts/cofirm-email/[^/]+/',RedirectView.as_view(pattern_name="timeline:index"),kwargs=None),
    path('accounts/',include('allauth.urls')),
]

#include→引数のurl.pyに処理を任せる

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#投稿画像ディレクトリをurlで紐づけ
#path以外をurlpatternsに直接組み込むと正常に動作しない
#原因はstatic関数の仕様によるもの