from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category
from .forms import NoteForm, CategoryForm

def note_list(request):
    category_id = request.GET.get('category')
    if category_id:
        notes = Note.objects.filter(category_id=category_id)
    else:
        notes = Note.objects.all()
    categories = Category.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes, 'categories': categories})

def note_detail(request, pk):
    from markdown2 import markdown
    note = get_object_or_404(Note, pk=pk)
    note_html = markdown(note.content)  # Only if markdown2 is installed
    return render(request, 'notes/note_detail.html', {'note': note, 'note_html': note_html})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = CategoryForm()
    return render(request, 'notes/category_form.html', {'form': form})