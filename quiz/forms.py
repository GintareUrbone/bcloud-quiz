from django import forms
from django.forms.widgets import RadioSelect, Textarea, CheckboxSelectMultiple


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(label='radio', choices=choice_list,
                                                   widget=RadioSelect(attrs={'id': 'value'}))


class EssayForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(label='text',
            widget=Textarea(attrs={'style': 'width:100%'}))


class MultiChoiceForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(MultiChoiceForm, self).__init__(*args, **kwargs)
	choice_list = [x for x in question.get_answers_list()]
	print choice_list
        self.fields["answers"] = forms.MultipleChoiceField(choices=choice_list, label='checkbox',
                                                   widget=CheckboxSelectMultiple)
