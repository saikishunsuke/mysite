from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Summary

# Create your views here.
class IndexSummaryView(ListView):
    template_name = 'board/index_summary.html'
    context_object_name = 'summaries'
    model = Summary

index = IndexSummaryView.as_view()
