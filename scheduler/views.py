from rest_framework import viewsets
from rest_framework.response import Response
from .models import Candidate, Interviewer, Availability
from .serializers import CandidateSerializer, InterviewerSerializer, AvailabilitySerializer
from datetime import timedelta

class CandidateViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Candidate instances.
    
    - Provides standard CRUD operations (Create, Retrieve, Update, Delete).
    - Uses the Candidate model and CandidateSerializer to perform operations on the `Candidate` data.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class InterviewerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Interviewer instances.
    
    - Provides standard CRUD operations (Create, Retrieve, Update, Delete).
    - Uses the Interviewer model and InterviewerSerializer to perform operations on the `Interviewer` data.
    """
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer

class AvailabilityViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Availability instances.
    
    - Provides standard CRUD operations (Create, Retrieve, Update, Delete).
    - Uses the Availability model and AvailabilitySerializer to perform operations on the `Availability` data.
    """
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

class ScheduleInterviewViewSet(viewsets.ViewSet):
    """
    A custom viewset for scheduling interview time slots between a candidate and an interviewer.

    - Retrieves the availability of both candidate and interviewer based on their IDs.
    - Identifies overlapping time slots of at least one hour between candidate and interviewer availabilities.
    - Returns a list of available 1-hour time slots in the format [(start_time, end_time), ...].

    Methods:
        list(self, request, candidate_id, interviewer_id):
            Retrieves available interview time slots for a specified candidate and interviewer.
    """
    def list(self, request, candidate_id, interviewer_id):
        """
        Lists available 1-hour time slots where a candidate and interviewer can schedule an interview.

        - Filters the Availability model to retrieve availability records for both the candidate and interviewer.
        - Finds overlapping time between candidate and interviewer availabilities and divides them into 1-hour slots.
        
        Args:
            request: The HTTP request object.
            candidate_id (int): ID of the candidate.
            interviewer_id (int): ID of the interviewer.
        
        Returns:
            Response: A list of tuples containing start and end times of available 1-hour interview slots.
        """
        candidate_availabilities = Availability.objects.filter(candidate_id=candidate_id)
        interviewer_availabilities = Availability.objects.filter(interviewer_id=interviewer_id)

        available_slots = []

        for candidate in candidate_availabilities:
            for interviewer in interviewer_availabilities:
                start = max(candidate.start_time, interviewer.start_time)
                end = min(candidate.end_time, interviewer.end_time)
                while start < end:
                    available_slots.append((start.strftime("%Y-%m-%d %H:%M:%S"), (start + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")))
                    start += timedelta(hours=1)

        return Response(available_slots)
