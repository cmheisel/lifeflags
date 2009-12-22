from django.shortcuts import render_to_response, get_object_or_404

from lifeflags.flags.models import Flag

def show(request, slug):
    f = get_object_or_404(Flag, slug=slug)
    context = { 'flag': f }
    return render_to_response('flags/flag_detail.html', context)
