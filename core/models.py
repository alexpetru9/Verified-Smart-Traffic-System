from django.db import models

class TrafficPlan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    green_duration = models.PositiveIntegerField(help_text="Green duration (seconds)")
    yellow_duration = models.PositiveIntegerField(default=3)

    def __str__(self):
        return self.name

class Intersection(models.Model):
    PHASE_CHOICES = [
        ('NS_GREEN', 'North-South Green'),
        ('NS_YELLOW', 'North-South Yellow'),
        ('EW_GREEN', 'East-West Green'),
        ('EW_YELLOW', 'East-West Yellow'),
        ('ALL_RED', 'All Red'),
    ]
    
    name = models.CharField(max_length=100)
    current_phase = models.CharField(max_length=10, choices=PHASE_CHOICES, default='ALL_RED')
    previous_phase = models.CharField(max_length=10, choices=PHASE_CHOICES, default='EW_YELLOW')
    active_plan = models.ForeignKey(TrafficPlan, null=True, blank=True, on_delete=models.SET_NULL)
    last_phase_change = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.current_phase})"