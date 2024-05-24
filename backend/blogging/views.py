from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from blogging.models import Post

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join([f"\t{arg}" for arg in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join([f"\t{key}: {val}" for key, val in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by("-published_date")
    context = {"posts": posts}
    return render(request, "blogging/list.html", context)

def detail_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        # display post if it is published
        if post.published_date:
            context = {"post": post}
            return render(request, "blogging/detail.html", context)
    # post doesn't exist
    except Post.DoesNotExist:
        raise Http404
    # found a post, but it is not published
    raise Http404