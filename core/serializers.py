from rest_framework import serializers
from .models import Intersection
from django.utils import timezone 

class IntersectionSerializer(serializers.ModelSerializer):
    active_plan_name = serializers.CharField(source='active_plan.name', read_only=True)
    time_remaining = serializers.SerializerMethodField()

    class Meta:
        model = Intersection
        fields = ['id', 'name', 'current_phase', 'active_plan_name', 'time_remaining']

    def get_time_remaining(self, obj):
        if not obj.active_plan:
            return 0 

        total_duration = 0
        plan = obj.active_plan
        phase = obj.current_phase

        if phase == 'NS_GREEN':
            total_duration = plan.green_duration
        elif phase == 'NS_YELLOW':
            total_duration = plan.yellow_duration
        elif phase == 'EW_GREEN':
            total_duration = plan.green_duration
        elif phase == 'EW_YELLOW':
            total_duration = plan.yellow_duration
        elif phase == 'ALL_RED':
            total_duration = 2 

        elapsed_seconds = (timezone.now() - obj.last_phase_change).total_seconds()
        return max(0, round(total_duration - elapsed_seconds))