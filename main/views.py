from django.shortcuts import render,redirect,get_object_or_404
from .models import bookmarkModel
from .forms import bookmarkForm

# Create your views here.

def mainhome(request):
    bookmarks = bookmarkModel.objects.all()

    return render (request, 'mainhome.html', {'bookmarks' : bookmarks})

def create(request):
    if request.method == 'POST':
        inputForm = bookmarkForm(request.POST)
        if inputForm.is_valid():
            bookmark = bookmarkModel()
            bookmark.site_name = inputForm.cleaned_data['site_name']
            bookmark.site_url = inputForm.cleaned_data['site_url']
            bookmark.save()
            return redirect ('mainhome')
    
    else:
        newForm = bookmarkForm()
        return render(request, 'new.html', {'newForm' : newForm})

def edit(request, bookmark_id):
    editForm = get_object_or_404(bookmarkModel, pk =bookmark_id)

    if request.method == 'POST':
        inputForm = bookmarkForm(request.POST, instance = editForm)
        if inputForm.is_valid():
            inputForm.save()
            return redirect ('mainhome')
    
    else:
        newForm = bookmarkForm(instance = editForm)
        return render (request, 'edit.html', {'newForm' : newForm})

def delete(request, bookmark_id):
    deleteForm = get_object_or_404(bookmarkModel , pk = bookmark_id)
    deleteForm.delete()
    return redirect ('mainhome')