from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet, InterviewerViewSet, AvailabilityViewSet, ScheduleInterviewViewSet

router = DefaultRouter()  # Initialize the default router for automatic URL routing of viewsets

# Register the CandidateViewSet with the router at the 'candidates/' URL endpoint
router.register(r'candidates', CandidateViewSet)

# Register the InterviewerViewSet with the router at the 'interviewers/' URL endpoint
router.register(r'interviewers', InterviewerViewSet)

# Register the AvailabilityViewSet with the router at the 'availability/' URL endpoint
router.register(r'availability', AvailabilityViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # custom URL pattern for scheduling an interview between a candidate and an interviewer
    path('schedule/<int:candidate_id>/<int:interviewer_id>/',
        ScheduleInterviewViewSet.as_view({'get': 'list'}), 
        name='schedule_interview'),
]