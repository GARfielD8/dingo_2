from turtle import update
from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import BookingForm
from .models import Category, FoodModel, WorkersModels,Feedback
from django.urls import reverse_lazy
from .forms import RegForm

class IndexView(CreateView):
    form_class = BookingForm
    template_name = 'index.html'

    def get_queryset(self):
        return FoodModel.objects.order_by('-updated_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["catry"] = Category.objects.all()
        context['chef'] = WorkersModels.objects.all()
        context['food'] = FoodModel.objects.all()
        context["exfood"] = FoodModel.objects.filter(is_exclusive=True)[3::-1]
        context['feedback'] = Feedback.objects.all()
        return context


class FoodDetailView(DetailView):
    model = FoodModel
    template_name = 'about-food.html'
    context_object_name = 'food'

class RegView(CreateView):
    template_name = 'registration.html'
    form_class = RegForm
    success_url = reverse_lazy('reg')

