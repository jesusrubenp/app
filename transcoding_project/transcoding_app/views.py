from django.shortcuts import render

# transcoding_app/views.py

from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guarda el video en la base de datos
            return redirect('video_list')  # Redirige a la lista de videos (puedes crear esta vista más tarde)
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

