from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin#accessmixinineクラスを継承し、ログインユーザーのみが使用できるようにする機能を持つ
from django.views import generic
from .forms import ProfileForm
from django.contrib.messages.views import SuccessMessageMixin#フォーム成功時の処理を継承


# Create your views here.
class ProfileEdit(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView):
    model=CustomUser
    form_class=ProfileForm
    template_name='account/edit.html'
    sucess_url="/accounts/edit/"#更新したら自己遷移
    sucess_message='プロフィールを更新しました。'
    
    def __init__(self):
        return self.request.user #request.user→現在ログインしているユーザーの情報(def__nit__(self)で自動取得)

edit=ProfileEdit.as_view()