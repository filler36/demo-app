from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Note

# Create your views here.
def index(request):
    return render(request, "mainapp/index.html", {'title': 'Index', 'pages': ['notes', 'status']})


def status(request):
    return render(request, "mainapp/status.html", {'title': 'Status', 'start_time': start_time})


def notes(request):
    return render(request, "mainapp/notes.html", {'title': 'Notes', 'notes': Note.objects.all()})


def note(request, note_id):
    note = Note.objects.get(pk=note_id)
    return render(request, 'mainapp/note.html', {'note': note})


start_time = timezone.now()
