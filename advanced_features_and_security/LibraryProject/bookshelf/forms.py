from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Book title", "required": True}),
            "author": forms.TextInput(attrs={"placeholder": "Author name", "required": True}),
            "publication_year": forms.NumberInput(attrs={"placeholder": "YYYY", "required": True}),
        }

    def clean_publication_year(self):
        year = self.cleaned_data.get("publication_year")
        if year is None:
            raise forms.ValidationError("Publication year is required.")
        if year < 0 or year > 9999:
            raise forms.ValidationError("Please enter a valid year.")
        return year

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
