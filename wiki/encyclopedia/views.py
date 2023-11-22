from django.shortcuts import render, redirect
from markdown2 import markdown as md
from django.shortcuts import render, redirect
from django.http import Http404
from django import forms
from django.core.exceptions import ValidationError
from gettext import gettext as _
from random import choice as random_choice
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    cap_name = util.get_capitalized_title(name)

    if not cap_name:
        raise Http404("not found")

    if name != cap_name:
        return redirect(title, cap_name)

    markdown = util.get_entry(name)

    entry = {
        "title": name,
        "html": md(markdown)
    }
    return render(request, "encyclopedia/title.html", {
        "entry": entry
    })