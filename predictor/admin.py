from django.contrib import admin
from .models import Predictor

@admin.register(Predictor)
class PredictorAdmin(admin.ModelAdmin):
    list_display = ('date','to_predict')
# Register your models here.
