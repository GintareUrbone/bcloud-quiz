from django import forms
from django.contrib import admin
from common.models import Feedback


class FeedbackForm(forms.ModelForm):
  class Meta:
    model = Feedback
    widgets = {
      'feedback_text': forms.Textarea,
    }

class FeedbackAdmin(admin.ModelAdmin):

    form = FeedbackForm

    list_display = ('user', 'feedback_text', )
    list_filter = ('user', )
    search_fields = ('user', )


admin.site.register(Feedback, FeedbackAdmin)
