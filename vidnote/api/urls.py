from django.urls import path
from .views import VideoListCreateView, NoteListCreateView, VideoDetailView, NoteDetailView, VideoNotesView

urlpatterns = [
    # Video endpoints
    path("videos/", VideoListCreateView.as_view(), name="video-list-create"),
    path("videos/<int:pk>/", VideoDetailView.as_view(), name="video-detail"),
    path("videos/<int:pk>/notes/", VideoNotesView.as_view(), name="video-notes"),
    
    # Note endpoints
    path("notes/", NoteListCreateView.as_view(), name="note-list-create"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
]
