from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Reviews


# class ReviewsForm(forms.ModelForm):
#     class Meta:
#         model = Reviews
#         fields = ['full_name', 'review_title', 'review_body', 'review_image', 'rating']

#     def clean_rating(self):
#         rating = self.cleaned_data['rating']
#         if rating < 0 or rating > 5:
#             raise forms.ValidationError("Rating must be between 0 and 5.")
#         return rating

