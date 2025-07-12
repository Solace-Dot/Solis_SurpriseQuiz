from django.db import models

class Project(models.Model):

    name = models.CharField(max_length=200, help_text="Name of the project")
    description = models.TextField(help_text="Detailed description of the project")
    link = models.URLField(blank=True, null=True, help_text="Optional link to the live project or repository")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when the project was added")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):

        return self.name

