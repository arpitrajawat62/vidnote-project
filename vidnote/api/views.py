from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import VideoSerializer, NoteSerializer
from core.models import Video, Note

# Create your views here.


class VideoListCreateView(generics.ListCreateAPIView):
    """List all videos or create a new video"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a specific video"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoNotesView(generics.ListAPIView):
    """Get all notes for a specific video"""
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        video_id = self.kwargs['pk']
        return Note.objects.filter(video_id=video_id)


class NoteListCreateView(generics.ListCreateAPIView):
    """List all notes or create a new note"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a specific note"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
