from django import forms

class RegisterForm(forms.Form):
    Reg_id= forms.IntegerField()
    Name= forms.CharField(label='Name',max_length=30)
    choices_fields = [('ECE','Electronics'),('CSE','Computers'),('MECH','mechanics'),('EEE','Electrics')]
    Branch=forms.MultipleChoiceField(label='Branch',choices=choices_fields)

class LoginForm(forms.Form):
    Name= forms.CharField(label='Name',max_length=30)
    Password =forms.CharField(label='password',max_length=30,widget=forms.PasswordInput)
