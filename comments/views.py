from django.shortcuts import render, get_object_or_404

from comments.models import Comment

def comment_thread(request, id):
    obj = get_object_or_404(Comment, id=id)
    context = {
        "obj": obj,
    }
    return render(request, "comment_thread.html", context)