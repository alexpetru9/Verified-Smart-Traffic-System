from datetime import datetime
from django.utils import timezone
from .models import Intersection
from .services import set_intersection_phase

def simulation_tick_job():
    # Retrieve ALL intersections from the database
    intersections = Intersection.objects.all() 
    
    for intersection in intersections:
        if not intersection.active_plan:
            continue # Skip if no active plan assigned

        plan = intersection.active_plan
        now = timezone.now()
        
        # Calculate how long the light has been in the current state
        time_in_phase = (now - intersection.last_phase_change).total_seconds()

        current_phase = intersection.current_phase
        next_phase = current_phase 

        # --- TRANSITION LOGIC (State Machine) ---
        if current_phase == 'NS_GREEN':
            if time_in_phase >= plan.green_duration:
                next_phase = 'NS_YELLOW'
        elif current_phase == 'NS_YELLOW':
            if time_in_phase >= plan.yellow_duration:
                next_phase = 'ALL_RED'
        elif current_phase == 'EW_GREEN':
            if time_in_phase >= plan.green_duration:
                next_phase = 'EW_YELLOW'
        elif current_phase == 'EW_YELLOW':
            if time_in_phase >= plan.yellow_duration:
                next_phase = 'ALL_RED'
        elif current_phase == 'ALL_RED':
            if time_in_phase >= 2: # Minimal safety buffer
                if intersection.previous_phase == 'NS_YELLOW':
                    next_phase = 'EW_GREEN'
                else:
                    next_phase = 'NS_GREEN'

        # If a change is needed, trigger the verified transition
        if next_phase != current_phase:
            # This call is intercepted by K Framework verification
            set_intersection_phase(intersection, next_phase)