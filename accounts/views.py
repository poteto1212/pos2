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
    sucess_url="/accounts/edit/"#更新したら自己遷移(form_classからのデータを持ってる)
    sucess_message='プロフィールを更新しました。'
    
    def get_object(self):
        return self.request.user#request.user→現在ログインしているユーザーの情報(def__nit__(self)で自動取得)

edit=ProfileEdit.as_view()

class ProfileDetail(LoginRequiredMixin,generic.DetailView):
    model=CustomUser
    template_name='account/detail.html'
    
detail=ProfileDetail.as_view()

class CreateView(LogunRequreMixin,geneic.CreateView):
    form_class=PostForm
    sucess_url=rverse_lazy('timeline:index')
    
    #form_vaild関数に外部キー指定機能及びメッセージ表示機能を追加する。
    def form_vaild(self.form):#form_vaild()postされた際、validationがOKだった場合に呼び出される関数。保存処理や、後処理、リダイレクト先を設定するために利用します
        form.instance.auther_id=self.request.user_id#form指定カラムの外部キー(ユーザー情報)=rwquestのid情報
        messages.sucess(self.request,'投稿が完了しました')
        return super(CreateView,self).form_vaild(form)
        
    def 