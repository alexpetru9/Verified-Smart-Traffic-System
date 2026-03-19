from django.utils import timezone
from .verification import ensure_safe_transition

@ensure_safe_transition
def set_intersection_phase(intersection, new_phase):
    print(f"Change: {intersection.name} -> {new_phase}")
    intersection.previous_phase = intersection.current_phase
    intersection.current_phase = new_phase
    intersection.last_phase_change = timezone.now()
    intersection.save(update_fields=['current_phase', 'previous_phase', 'last_phase_change'])