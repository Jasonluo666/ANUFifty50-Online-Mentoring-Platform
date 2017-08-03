from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone
from .models import Post, Mentor, Mentee, Training


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ModelWithFileField(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('list')
    else:
        form = UploadFileForm()
    return render(request, 'list.html', {'form': form})
