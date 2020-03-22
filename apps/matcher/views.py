# -*- coding: utf-8 -*-
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Helper, Inquiry, Hospital
from .forms import HelperForm, InquiryForm
from .tasks import match_indiviual, send_mail_inquiry, send_mail_participant


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'helper_list'

    def get_queryset(self):
        return Helper.objects.all()[:5]


@csrf_exempt
def helper_new(request):
    if request.method == "POST":
        form = HelperForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            # trying to match the helper to an inquiry
            matched_inquiry = match_indiviual(Inquiry.objects.all(), post)
            print("SENDING MAIL")
            send_mail_participant(post, matched_inquiry)
            print("SENT MAIL")
            return HttpResponseRedirect(reverse('matcher:helper_detail', kwargs={'helper_id': post.pk}))
    else:
        form = HelperForm()
    return render(request, 'polls/register_helper.html', {'form': form})


def helper_detail(request, helper_id):
    person = get_object_or_404(Helper, pk=helper_id)
    return render(request, 'polls/register_success.html', context={
        'name': f'Liebe(r) {person.first_name} {person.last_name},',
        'message': f'vielen Dank für dein Engagment!\nWir haben eine E-Mail an {person.e_mail} gesendet, in der Du genauere Informationen über das weitere Vorgehen erhälst.',
        'button_style': 'style="background-color:#9AC082;border-color:#9AC082;color:#030202"'
    })


@csrf_exempt
def institution_new(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            print("SENDING MAIL")
            send_mail_inquiry(post)
            print("SENT MAIL")
            return HttpResponseRedirect(reverse('matcher:institution_detail', kwargs={'inquiry_id': post.pk}))
    else:
        form = InquiryForm()
    return render(request, 'polls/register_institution.html', {'form': form})


def institution_detail(request, inquiry_id):
    hospital = get_object_or_404(Hospital, pk=inquiry_id)
    return render(request, 'polls/register_success.html', context={
        'name': f'Sehr geeherter Herr / sehr geehrte Frau {hospital.last_name_contact},',
        'message': f'vielen Dank für Ihre Anfrage. Wir haben eine E-Mail an {hospital.e_mail} gesendet, in der Sie weitere Informationen über das weitere Vorgehen erhalten.',
        'button_style': 'style="background-color:#C88797;border-color:#C88797;color:#030202"'
    })

# class DetailView(generic.DetailView):
#     model = Poll
#     template_name = 'matcher/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Poll
#     template_name = 'matcher/results.html'
#
#
# def vote(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the poll voting form.
#         return render(request, 'matcher/detail.html', {
#             'poll': p,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('matcher:results', args=(p.id,)))
