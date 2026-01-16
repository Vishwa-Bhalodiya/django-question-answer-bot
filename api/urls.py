from django.urls import path
from .views import UploadDocument, AskQuestion

urlpatterns = [
    path("upload/", UploadDocument.as_view(), name="upload"),
    path("ask/", AskQuestion.as_view(), name="ask-question")
    
]
