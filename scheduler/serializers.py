from rest_framework import serializers
from .models import Candidate, Interviewer, Availability


# Serializer for the Candidate model 

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


# Serializer for the Interviewer model 

class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = '__all__'


# Serializer for the Availability model

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'