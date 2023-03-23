from django import forms
from .models import Review

# class ReviewFrom(forms.Form):
    # user_name = forms.CharField(label="Your Name", max_length=50, error_messages={
    #     "required": "The field is empty, You must input Your Name",
    #     "max_length": "You input very long Name",
    # })
    # feedback = forms.CharField(max_length=200, widget=forms.Textarea, label='Your Feedback')
    # rating =forms.IntegerField(max_value=10, min_value=1, label='Your Rating')

class ReviewFrom(forms.ModelForm):    
    class Meta:
        model = Review
        fields ='__all__'
        labels = {
            'user_name' : 'Your Name',
            'text_review' : 'Your Feedback',
            'rating' : 'Rating',
        }
        error_massage = {
            'user_name':{
              "required": "The field is empty, You must input Your Name",
              "max_length": "You input very long Name",
            },
            
        }
