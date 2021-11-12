from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):

    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        seconds = visit.get_duration().total_seconds()
        formated_duration = f"{seconds // 3600} h {(seconds % 3600) // 60} min"
        non_closed_visits.append(
            {
                    'who_entered': visit.passcard,
                    'entered_at': visit.entered_at,
                    'duration': formated_duration
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
