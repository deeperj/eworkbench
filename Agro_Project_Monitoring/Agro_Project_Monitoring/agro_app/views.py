from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import CertificationValidity, ProgramPerformance, Weather, AgroDocument, Farm, Certificate
from .forms import CertificationValidityForm, ProgramPerformanceForm, WeatherForm, AgroDocumentForm, FarmForm, CertificateForm


class CertificationValidityListView(ListView):
    model = CertificationValidity


class CertificationValidityCreateView(CreateView):
    model = CertificationValidity
    form_class = CertificationValidityForm


class CertificationValidityDetailView(DetailView):
    model = CertificationValidity


class CertificationValidityUpdateView(UpdateView):
    model = CertificationValidity
    form_class = CertificationValidityForm


class ProgramPerformanceListView(ListView):
    model = ProgramPerformance


class ProgramPerformanceCreateView(CreateView):
    model = ProgramPerformance
    form_class = ProgramPerformanceForm


class ProgramPerformanceDetailView(DetailView):
    model = ProgramPerformance


class ProgramPerformanceUpdateView(UpdateView):
    model = ProgramPerformance
    form_class = ProgramPerformanceForm


class WeatherListView(ListView):
    model = Weather


class WeatherCreateView(CreateView):
    model = Weather
    form_class = WeatherForm


class WeatherDetailView(DetailView):
    model = Weather


class WeatherUpdateView(UpdateView):
    model = Weather
    form_class = WeatherForm


class AgroDocumentListView(ListView):
    model = AgroDocument


class AgroDocumentCreateView(CreateView):
    model = AgroDocument
    form_class = AgroDocumentForm


class AgroDocumentDetailView(DetailView):
    model = AgroDocument


class AgroDocumentUpdateView(UpdateView):
    model = AgroDocument
    form_class = AgroDocumentForm


class FarmListView(ListView):
    model = Farm


class FarmCreateView(CreateView):
    model = Farm
    form_class = FarmForm


class FarmDetailView(DetailView):
    model = Farm


class FarmUpdateView(UpdateView):
    model = Farm
    form_class = FarmForm


class CertificateListView(ListView):
    model = Certificate


class CertificateCreateView(CreateView):
    model = Certificate
    form_class = CertificateForm


class CertificateDetailView(DetailView):
    model = Certificate


class CertificateUpdateView(UpdateView):
    model = Certificate
    form_class = CertificateForm

