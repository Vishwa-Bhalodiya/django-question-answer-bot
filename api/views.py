import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.files.storage import default_storage
from .rag import load_file, split_text, ask_question

# Temporary storage for uploaded documents (in-memory dictionary)
# Key: session_key, Value: list of text chunks
DOC_STORE = {}

class UploadDocument(APIView):
    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        # Save uploaded file
        file_path = default_storage.save(file.name, file)
        full_path = os.path.join(settings.MEDIA_ROOT, file_path)

        try:
            # Load file and split into text chunks
            text_chunks = load_file(full_path)          # returns plain text
            chunks = split_text(text_chunks)            # returns list of strings

            # Store chunks in memory using session key
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            DOC_STORE[session_key] = chunks

            return Response({"message": "File uploaded and processed successfully"})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AskQuestion(APIView):
    def post(self, request):
        question = request.data.get("question")
        session_key = request.session.session_key

        if not question:
            return Response({"error": "No question provided"}, status=status.HTTP_400_BAD_REQUEST)
        if not session_key or session_key not in DOC_STORE:
            return Response({"error": "No documents uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        chunks = DOC_STORE[session_key]

        try:
            # Ask question using plain text chunks
            answer = ask_question(chunks, question)
            return Response({"answer": answer})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
