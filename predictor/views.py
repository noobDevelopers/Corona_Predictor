from django.shortcuts import render
from .forms import PredictorForm
from .case_predictor import case_predictor,death_predictor,cured_predictor
# Create your views here.
def home(request):
    
    if request.method == "POST":
        predictor_form = PredictorForm(data=request.POST)
        if predictor_form.is_valid():
            text = ''
            to_predict = predictor_form.cleaned_data['to_predict']
            date = predictor_form.cleaned_data['date']
            if to_predict == 'cases':
                text = case_predictor(date)
            elif to_predict == 'deaths':
                text = death_predictor(date)
            else:
                text = cured_predictor(date)

            return render(request, 'predictor/predicted.html',{'text':text})
           
    else:
        predictor_form = PredictorForm()

    return render(request, 'predictor/predict.html', {'predictor_form': predictor_form})
