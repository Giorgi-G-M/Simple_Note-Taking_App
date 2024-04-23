from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.
def home(request):
    notes = Note.objects.all().order_by('-date_created')
    return render(request, 'home.html', {'notes': notes})

def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'note_detail.html', {'note': note})

def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form})

def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form, 'note': note})

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('home')