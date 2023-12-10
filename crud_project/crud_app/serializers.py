from rest_framework import serializers
from .models import Candidatedirectory,Eventdetails,Persona

from .models import Candidatedirectory, Eventdetails, Jobrequisition, Persona, Screeningmode, Gender, Maritalstatus, Employeedirectory, City, Experiencelevel, Educationlevel, Educationqualification, Educationspecialization, Source, Sourcetype, Reasonforchange

# Serializers for related models

class EventdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventdetails
        fields = ['event']

class JobrequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobrequisition
        fields = ['job_position']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['persona']

class ScreeningmodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screeningmode
        fields = ['screening_mode']

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['gender']

class MaritalstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maritalstatus
        fields = ['marital_status']

class EmployeedirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeedirectory
        fields = ['referred_by']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city']

class ExperiencelevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencelevel
        fields = ['experience_level']

class EducationlevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educationlevel
        fields = ['education_level']

class EducationqualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educationqualification
        fields = ['education_qualification']

class EducationspecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educationspecialization
        fields = ['education_specialization']

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['education_institution','source']

class SourcetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sourcetype
        fields = ['source_type']

class ReasonforchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reasonforchange
        fields = ['reason_for_change']


class CandidatedirectorySerializer(serializers.ModelSerializer):
    # event = EventdetailsSerializer()
    event = serializers.CharField(source='event.event', read_only=True)
    job_position = serializers.CharField(source='job_position.job_position', read_only=True)
    persona = serializers.CharField(source='persona.persona', read_only=True)
    screening_mode = serializers.CharField(source='screening_mode.screening_mode', read_only=True)
    gender = serializers.CharField(source='gender.gender', read_only=True)
    marital_status = serializers.CharField(source='marital_status.marital_status', read_only=True)
    referred_by = serializers.CharField(source='referred_by.referred_by', read_only=True)
    city = serializers.CharField(source='city.city', read_only=True)
    experience_level = serializers.CharField(source='experience_level.experience_level', read_only=True)
    education_level = serializers.CharField(source='education_level.education_level', read_only=True)
    education_qualification = serializers.CharField(source='education_qualification.education_qualification', read_only=True)
    education_specialization = serializers.CharField(source='education_specialization.education_specialization', read_only=True)
    education_institution = serializers.CharField(source='education_institution.education_institution', read_only=True)
    source = serializers.CharField(source='source.source', read_only=True)
    source_type = serializers.CharField(source='source_type.source_type', read_only=True)
    reason_for_change = serializers.CharField(source='reason_for_change.reason_for_change', read_only=True)


    class Meta:
        model = Candidatedirectory
        fields = '__all__'



class Candidatedirectory_serializer(serializers.ModelSerializer):
    event = EventdetailsSerializer()
    class Meta:
        model=Candidatedirectory
        fields='__all__'

class Candidatedirectory_serial(serializers.ModelSerializer):
    class Meta:
        model=Candidatedirectory
        fields='__all__'

    
