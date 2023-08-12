from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Video, Subtitle
from .serializers import VideoSerializer, SubtitleSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class SubtitleViewSet(viewsets.ModelViewSet):
    queryset = Subtitle.objects.all()
    serializer_class = SubtitleSerializer

    def create(self, request, *args, **kwargs):
        video_id = request.data.get('video')
        timestamp = float(request.data.get('timestamp'))
        subtitle_text = request.data.get('subtitle_text')

        video = get_object_or_404(Video, id=video_id)
        subtitle = Subtitle(video=video, timestamp=timestamp, subtitle_text=subtitle_text)
        subtitle.save()

        serializer = SubtitleSerializer(subtitle)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        video_id = request.query_params.get('video')
        subtitles = Subtitle.objects.filter(video__id=video_id)
        serializer = SubtitleSerializer(subtitles, many=True)
        return Response(serializer.data)
