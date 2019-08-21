from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    article_uuid = forms.CharField(widget=forms.HiddenInput)
    name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Your Name", "class": "comment-add-name-field"}
        ),
    )
    body = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "comment-add-body-field",
                "placeholder": "Whatchu' tryna' say.",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ["article_uuid", "name", "body"]

    # Testing name validation
    # def clean_name(self, *arg, **kwargs):
    #     instance = self.instance
    #     name = self.cleaned_data.get("name")
    #     queryset = Comment.objects.filter(name__iexact=name)
    #     if instance is not None:
    #         queryset = queryset.exclude(pk=instance.pk)
    #         if queryset.exists():
    #             raise forms.ValidationError("That name has been used.")
    #         return name

