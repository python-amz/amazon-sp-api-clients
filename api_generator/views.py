"""
This file is only used for type hint.
With this file, PyCharm can recognize the correct path of api.html and the context ``data`` .
"""
from pathlib import Path

from django.shortcuts import render

from api_generator.generator import Generator


def generate(request, file: Path):
    return render(request, 'api.html', {'data': Generator(file)})
