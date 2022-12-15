from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Note

# Create your views here.
def index(request):
    return render(request, "mainapp/index.html", {'title': 'Index', 'pages': ['notes', 'status']})


def status(request):
    return render(request, "mainapp/status.html", {'title': 'Status', 'start_time': start_time})


def notes(request):
    return render(request, "mainapp/notes.html", {'title': 'Notes', 'notes': Note.objects.all().order_by('-id')})


def note(request, note_id):
    note = Note.objects.get(pk=note_id)
    return render(request, 'mainapp/note.html', {'note': note})


def create_note(request):
    note = Note(title=request.POST['note_title'], text=request.POST['note_text'])
    note.save()
    return HttpResponseRedirect(reverse('note', args=(note.id,)))


start_time = timezone.now()
