from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):

    def format_duration(seconds):
        formated_duration = f"{seconds // 3600} h {(seconds % 3600) // 60} min"
        return formated_duration


    def get_visit_information():
        visit_template = {
            'who_entered': '',
            'entered_at': '',
            'duration': '',
            'suspicious': ''
        }
        visit_template['duration'] = format_duration(seconds)
        visit_template['entered_at'] = visit.entered_at
        visit_template['who_entered'] = visit.passcard
        visit_template['suspicious'] = visit.is_visit_long()
        return visit_template

    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        seconds = visit.get_duration().total_seconds()
        non_closed_visit = get_visit_information()
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
