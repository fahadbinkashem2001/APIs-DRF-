from rest_framework import serializers
from .models import Task,Author,Book,University,Student

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed']

    def validate_title(self, title):
        if len(title.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return title

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'email','books']


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(many=True,queryset=Author.objects.all(),slug_field='name')
    class Meta:
        model = Book
        fields = ['id','title','authors','published_date']

    def validate_title(self, title):
        if len(title.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return title

class StudentSerializer(serializers.ModelSerializer):
    university = serializers.SlugRelatedField(queryset = University.objects.all(),slug_field="name")
    class Meta:
        model = Student
        fields = ["id","name","cgpa","department","university"]

    def validate_cgpa(self,cgpa):
        if cgpa<0 or cgpa>4:
            raise serializers.ValidationError("CGPA must be in between 0 to 4.")
        return cgpa

class UniversitySerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = University
        fields = ["id","name","address","students"]


