
import os
import subprocess
from django.conf import settings
from .models import Video
from django.shortcuts import render, get_object_or_404 
# transcoding_app/views.py

from django.shortcuts import render, redirect
from .forms import VideoForm


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()  # Guarda el video en la base de datos

            # Definir rutas de entrada y salida
            input_path = video.file.path  # Ruta del video original
            output_filename = f"{os.path.splitext(video.file.name)[0]}_transcoded.mp4"
            output_path = os.path.join(settings.MEDIA_ROOT, 'transcoded', output_filename)

            # Asegurarse de que el directorio de salida exista
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            # Llamar a la función de transcodificación
            transcode_video(input_path, output_path)

            # Guardar el archivo transcodificado en el modelo Video
            video.transcoded_file.name = f'transcoded/{output_filename}'
            video.save()

            return redirect('video_list')  # Redirige a la lista de videos (asume que existe una vista para esto)
    else:
       
        form = VideoForm()
    return render(request, 'transcoding_app/upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()  # Obtener todos los videos de la base de datos
    return render(request, 'transcoding_app/video_list.html', {'videos': videos})


def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)  # Obtener el video por su ID
    return render(request, 'transcoding_app/video_detail.html', {'video': video})

def home(request):
    return render(request, 'transcoding_app/home.html')



def transcode_video(input_path, output_path):
    command = [
        'ffmpeg',
        '-i', input_path,        # Archivo de entrada
        '-codec:v', 'libx264',   # Codec de video
        '-preset', 'fast',       # Velocidad de compresión
        '-crf', '22',            # Factor de calidad (menor número es mejor calidad)
        '-codec:a', 'aac',       # Codec de audio
        '-b:a', '128k',          # Tasa de bits de audio
        '-y',                    # Sobrescribir el archivo de salida sin preguntar
        output_path              # Archivo de salida
    ]
    subprocess.run(command, check=True)



