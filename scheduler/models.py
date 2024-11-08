from django.db import models


# Model representing a candidate in the system

class Candidate(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model representing an interviewer in the system

class Interviewer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model representing availability time slots for candidates and interviewers

class Availability(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, blank=True)
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.candidate or self.interviewer} - {self.start_time} to {self.end_time}"
