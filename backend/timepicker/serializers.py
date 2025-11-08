from rest_framework import serializers
from .models import Course, CalendarSlot, StudentPick

class StudentPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPick
        fields = ['id', 'name', 'phone', 'created_at']

class CalendarSlotSerializer(serializers.ModelSerializer):
    # include nested student picks
    student_picks = StudentPickSerializer(many=True, read_only=True)

    class Meta:
        model = CalendarSlot
        fields = ['id', 'day', 'time', 'status', 'count', 'student_picks']

class CourseSerializer(serializers.ModelSerializer):
    calendar_slots = CalendarSlotSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'created_at', 'updated_at', 'calendar_slots']
