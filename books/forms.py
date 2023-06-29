from django import forms

from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "last_name", "age", "birth_date", "nationality"]


class BookForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'data'}))

    class Meta:
        model = Book
        fields = ["title", "author", "publication_date", "description"]
