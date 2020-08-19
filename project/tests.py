from django.test import TestCase
from project.models import Project
# Create your tests here.


class ProjectTestCase(TestCase):

    def setUp(self):
        Project.objects.create(name="Project_alpha_1")
        Project.objects.create(name="Project_alpha_2")
        Project.objects.create(name="Project_beta_1")
        Project.objects.create(name="Project_beta_2")

    def test_project(self):
        project_alpha_1 = Project.objects.get(name="Project_alpha_1")
        project_alpha_2 = Project.objects.get(name="Project_alpha_2")
        project_beta_1 = Project.objects.get(name="Project_beta_1")
        project_beta_2 = Project.objects.get(name="Project_beta_2")
