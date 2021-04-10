from django import forms
from .models import CustomUser

class ProfileForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)#自動的に値を代入したインスタンスを生成する処理
        
        for field in self.fields.values(): #モデルの入力項目を全て対象に・・・(fields.value)
            field.widget.attrs['class']='form-countrol'#bootstrapのform-countrolクラスを継承させる
            
    class Meta:
        model=CustomUser
        fields=('username','description','photo')
        help_texts={
            'username':None,#自動で挿入される説明文を無くす
        }