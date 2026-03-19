from .models import Intersection, TrafficPlan
from .serializers import IntersectionSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_intersection_state(request):
    try:
        intersections = Intersection.objects.all()
        serializer = IntersectionSerializer(intersections, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

def dashboard_view(request):
    return render(request, 'core/index.html')

# This is the NEW function for individual control
@api_view(['POST'])
def set_intersection_plan(request):
    try:
        # Receive the intersection ID and the Plan Name
        intersection_id = request.data.get('intersection_id')
        plan_name = request.data.get('plan_name')
        
        # Find the specific plan and intersection
        plan = TrafficPlan.objects.get(name=plan_name)
        intersection = Intersection.objects.get(id=intersection_id)
        
        # Apply the plan ONLY to this intersection
        intersection.active_plan = plan
        intersection.save()
            
        return Response({"success": True})
    except Exception as e:
        return Response({"error": str(e)}, status=500)