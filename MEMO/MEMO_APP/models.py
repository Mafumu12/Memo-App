from django.db import models
from django.contrib.auth.models import User

# Define the models for the app

# Create a class named 'TASK' that inherits from 'models.Model'
class TASK(models.Model):
    # Define a field 'title' as a character field with a maximum length of 200 characters
    title = models.CharField(max_length=200)
    
    # Define a field 'description' as a text field to store longer text
    description = models.TextField()
    
    # Define a field 'status' as a boolean field with a default value of 'False'
    status = models.BooleanField(default=False)
    
    # Define a field 'owner' as a foreign key to the 'User' model, specifying behavior on user deletion
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Define a field 'created' as a date and time field that updates automatically when saved
    created = models.DateTimeField(auto_now=True)

    # Define a method '__str__' to provide a human-readable string representation of the model
    def __str__(self):
        return self.title
