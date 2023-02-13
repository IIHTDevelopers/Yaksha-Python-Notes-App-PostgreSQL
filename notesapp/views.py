from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notesapp.serializers import NotesSerializer
from notesapp.models import NotesModel

class NotesCRUDView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self,request,pk,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self,request,pk,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
