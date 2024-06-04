# hottrack/views.py

import json
# from imaplib import Literal
from urllib.request import urlopen
import pandas as pd
from typing import Literal
from io import BytesIO
from django.db.models import QuerySet, Q
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from hottrack.utils.cover import make_cover_image
from hottrack.models import Song


def index(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("query", "").strip()

    song_qs: QuerySet[Song] = Song.objects.all()

    if query:
        song_qs = song_qs.filter(
            Q(name__icontains=query)
            | Q(artist_name__icontains=query)
            | Q(album_name__icontains=query)
        )

    return render(
        request=request,
        template_name="hottrack/index.html",
        context={
            "song_list": song_qs,
            "query": query,
        },
    )

def export(request, format: Literal["csv", "xlsx"]):
    song_qs: QuerySet = Song.objects.all()
    print(f"song_qs.values() : {song_qs.values()}")
    df = pd.DataFrame(data=song_qs.values())

    print(f"df:{df}")

    # 메모리 파일 객체
    export_file = BytesIO()

    if format == 'csv':
        content_type = 'text/csv'
        filename = 'hottrack.csv'
        df.to_csv(export_file, index=False, encoding='utf-8-sig')

    elif format == 'xlsx':
        content_type = 'application/vnd.ms-excel'
        filename = 'hottrack.xlsx'
        df.to_excel(export_file, index=False)
    else:
        return HttpResponseBadRequest(f"Invalid format : {format}")

    print(f"export_file:{export_file}")

    response = HttpResponse(content=export_file.getvalue(), content_type=content_type)
    response["Content-Disposition"] = f'attachment; filename="{filename}"'


    return response








def cover_png(request, pk):
    # 최대값 512, 기본값 256
    canvas_size = min(512, int(request.GET.get("size", 256)))

    song = get_object_or_404(Song, pk=pk)

    cover_image = make_cover_image(
        song.cover_url, song.artist_name, canvas_size=canvas_size
    )

    # param fp : filename (str), pathlib.Path object or file object
    # image.save("image.png")
    response = HttpResponse(content_type="image/png")
    cover_image.save(response, format="png")

    return response



