from django.shortcuts import render
from django.http import JsonResponse
from .scenarios import SCENARIOS
import random


def social_engineering_simulator(request):
    if request.method == 'POST':
        scenario_id = int(request.POST.get('scenario_id'))
        selected_option = int(request.POST.get('selected_option'))

        scenario = SCENARIOS[scenario_id]
        is_correct = scenario['options'][selected_option]['is_correct']
        explanation = scenario['explanation']

        return JsonResponse({
            'is_correct': is_correct,
            'explanation': explanation
        })

    # Get a random scenario for initial load
    scenario = random.choice(SCENARIOS)
    scenario_id = SCENARIOS.index(scenario)

    return render(request, 'social_engineering/templates/social_engineering_simulator.html', {
        'scenario': scenario,
        'scenario_id': scenario_id
    })