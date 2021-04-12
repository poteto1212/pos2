from django.shortcuts import render
from django.views import generic
from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
# Create your views here.

class IndexView(generic.TemplateView):
    template_name="index.html"
    paginate_by=10 #10ページ表示する。
    def get_queryset(self):
        posts=Post.objects.orders_by('-created_at')
        return posts


index=IndexView.as_view()

class CreateView(LoginRequiredMixin,generic.CreateView):
    form_class=PostForm
    sucess_url=reverse_lazy('timeline:index')#urls.pyのindex変数→index.htmlの表示が可能
    
    #form_vaild関数に外部キー指定機能及びメッセージ表示機能を追加する。
    def form_vaild(self,form):#form_vaild()postされた際、validationがOKだった場合に呼び出される関数。保存処理や、後処理、リダイレクト先を設定するために利用します
        form.instance.auther_id=self.request.user_id#form指定カラムの外部キー(ユーザー情報)=rwquestのid情報
        messages.sucess(self.request,'投稿が完了しました')
        return super(CreateView,self).form_vaild(form)
        
    def form_invalid(self,form):#投稿失敗時の処理
        messages.warning(self.request,'投稿が失敗しました')
        return redirect('timeline:index')
        
create=CreateView.as_view()
        
