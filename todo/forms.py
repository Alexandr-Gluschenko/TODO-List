from django import forms
from django.utils import formats
from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    created_at = forms.DateTimeField(
        label="Created",
        disabled=True,
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                'readonly': True,
            }
        )
    )



    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'deadline': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                    'autocomplete': 'off',
                }
            ),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['created_at'].initial = formats.date_format(
                self.instance.created_at,
                "F d, Y, g:i a"
            )
        else:
            self.fields.pop('created_at')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }