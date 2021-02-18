from django import forms
from django.forms import ModelForm
from django.utils import timezone

from .models import CollegeProject


MONTH_CHOICES = [
    (1, 'Januari'), 
    (2, 'Februari'),
    (3, 'Maret'),
    (4, 'April'),
    (5, 'Mei'),
    (6, 'Juni'),
    (7, 'Juli'),
    (8, 'Agustus'),
    (9, 'September'),
    (10, 'Oktober'),
    (11, 'November'),
    (12, 'Desember'),
]

class CollegeProjectForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['target_month'].widget = forms.Select(choices=MONTH_CHOICES)
                
        now_year = timezone.now().date().year
        next_5_years = now_year + 5
        self.fields['target_year'].widget = forms.Select(choices=[(year, year) for year in range(now_year, next_5_years)])
        
        self.fields['project_idea'].widget.attrs = {'rows': 5}
       
    class Meta:
        model = CollegeProject
        fields = (
            'target_month',
            'target_year',
            'project_type',
            'project_idea',
        )
        labels = {
            'target_month': 'Bulan',
            'target_year': 'Tahun',
            'project_type': 'Tipe Aplikasi yang Ingin Dikembangkan',
            'project_idea': 'Ceritakan Tentang Ide atau Tema yang Sudah Kamu Pikirkan',
        }
        help_texts = {
            'project_idea': 'Bila belum ada ide atau tema, boleh dikosongi',
        }

