# -*- coding: utf-8 -*-
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from .models import Helper
from .forms import HelperForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'helper_list'

    def get_queryset(self):
        return Helper.objects.all()[:5]


def helper_new(request):
    if request.method == "POST":
        form = HelperForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('polls:helper_detail', kwargs={'helper_id': post.pk}))
    else:
        form = HelperForm()
    return render(request, 'polls/register_helper.html', {'form': form})


def helper_detail(request, helper_id):
    p = get_object_or_404(Helper, pk=helper_id)
    return HttpResponse(f'{p.first_name} {p.last_name}')

# class DetailView(generic.DetailView):
#     model = Poll
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Poll
#     template_name = 'polls/results.html'
#
#
# def vote(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the poll voting form.
#         return render(request, 'polls/detail.html', {
#             'poll': p,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
