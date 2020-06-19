from django import forms
from .models import Predictor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit,Fieldset,Div,Field,HTML
from crispy_forms.bootstrap import FormActions,TabHolder,Tab,AppendedText
from datetime import datetime
class PredictorForm(forms.ModelForm):
    class Meta:
        model = Predictor
        fields = ('date','to_predict')
    def __init__(self, *args, **kwargs):
        super(PredictorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'predict-form'
        self.helper.layout = Layout(
                Div(
        
            
            
            Div(Div(HTML('<p style="color: red;"><strong>**Date format = dd/mm/yy**</strong></p>')),style='text-align: center'),
            Div(Div('date',style='display: inline-block'),style='text-align: center'),
            Div(Div('to_predict',style='display: inline-block'),style='text-align: center'),

            FormActions(
            Div(Div(Submit('save', 'Predict',css_class="btn-success"),style='display: inline-block;margin-top:50px;padding:10px;margin-left:10px;'),style='text-align: center'),
                Div(Div(HTML('*Note->The model is based on data from <a href="https://www.kaggle.com">kaggle</a> and does not guarantee for accurate prediction'),style='display: inline-block'),style='text-align: center')
            )
            ,style="margin: 12px;"),
            
        
        )
    def clean_date(self):
      
        date = self.cleaned_data.get('date')
        flag = 0
        try:
           
            d = datetime.strptime(date, '%d/%m/%y')
        except:
            flag = 1
        if flag == 1:
         
            raise forms.ValidationError("Date format doesnot match")
        return date

        