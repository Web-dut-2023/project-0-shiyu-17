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


def search(request):
    query = request.GET['q']
    if not query:
        return redirect(index)

    cap_query = util.get_capitalized_title(query)
    if cap_query:
        return redirect(title, name=cap_query)

    return render(request, "encyclopedia/search.html", {
        "matches": [name for name in util.list_entries() if query.lower() in name.lower()],
        "query": query
    })


def random(request):
    return redirect(title, name=random_choice(util.list_entries()))


def new(request):
    if request.method == 'POST':
        name = request.POST.get('title')
        body = request.POST.get('body')

        if not name:
            error_message = "Title cannot be empty."
            return render(request, "encyclopedia/new.html", {
                "error_message": error_message,
                "title": name,
                "body": body
            })

        if util.get_entry(name):
            error_message = "An entry with this title already exists. Choose a different title."
            return render(request, "encyclopedia/new.html", {
                "error_message": error_message,
                "title": name,
                "body": body
            })

        util.save_entry(name, body)
        return redirect('title', name) # Redirect to the newly created entry

    return render(request, "encyclopedia/new.html")


def edit(request, name):
    cap_name = util.get_capitalized_title(name)

    if not cap_name:
        raise Http404("404 not found")

    if name != cap_name:
        return redirect(edit, cap_name)

    if request.method == 'POST':
        body = request.POST.get('body')

        # Save the edited entry
        util.save_entry(name, body)

        # Redirect back to the edited entry
        return redirect('title', name=name)

    # GET request
    markdown = util.get_entry(name)

    return render(request, "encyclopedia/edit.html", {
        "title": name,
        "body": markdown
    })
