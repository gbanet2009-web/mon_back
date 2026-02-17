from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Course, Exercise, BacSubject

class Command(BaseCommand):
    help = 'Populates the database with initial data for testing the API.'

    def handle(self, *args, **options):
        User = get_user_model()

        self.stdout.write(self.style.SUCCESS('Deleting existing data...'))
        User.objects.filter(is_superuser=False).delete()
        Course.objects.all().delete()
        Exercise.objects.all().delete()
        BacSubject.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating default user...'))
        user, created = User.objects.get_or_create(username='testuser', email='test@example.com')
        if created:
            user.set_password('testpassword')
            user.full_name = 'Test User'
            user.class_id = '3e'
            user.credits = 100
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))
        else:
            self.stdout.write(self.style.WARNING(f'User {user.username} already exists.'))
            user.set_password('testpassword')
            user.full_name = 'Test User'
            user.class_id = '3e'
            user.credits = 100
            user.save()


        self.stdout.write(self.style.SUCCESS('Creating courses...'))
        courses_data = [
            {'subject': 'Math', 'title': 'Cours de Maths 1', 'pdf_url': 'https://www.africau.edu/images/default/sample.pdf', 'class_id': '3e'},
            {'subject': 'Physique', 'title': 'Cours de Physique 1', 'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf', 'class_id': '3e'},
            {'subject': 'Chimie', 'title': 'Cours de Chimie 1', 'pdf_url': 'https://www.africau.edu/images/default/sample.pdf', 'class_id': '3e'},
            {'subject': 'Histoire', 'title': "Cours d'Histoire 1", 'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf', 'class_id': '2nde'},
            {'subject': 'Géo', 'title': 'Cours de Géo 1', 'pdf_url': 'https://www.africau.edu/images/default/sample.pdf', 'class_id': '2nde'},
        ]
        for data in courses_data:
            Course.objects.get_or_create(**data)
        self.stdout.write(self.style.SUCCESS(f'Created {len(courses_data)} courses.'))

        self.stdout.write(self.style.SUCCESS('Creating exercises...'))
        exercises_data = [
            {'subject': 'Math', 'title': 'Exo Maths 1', 'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf', 'class_id': '3e'},
            {'subject': 'Physique', 'title': 'Exo Physique 1', 'pdf_url': 'https://www.africau.edu/images/default/sample.pdf', 'class_id': '3e'},
            {'subject': 'Chimie', 'title': 'Exo Chimie 1', 'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf', 'class_id': '3e'},
            {'subject': 'Histoire', 'title': 'Exo Histoire 1', 'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf', 'class_id': '2nde'},
            {'subject': 'Géo', 'title': 'Exo Géo 1', 'pdf_url': 'https://www.africau.edu/images/default/sample.pdf', 'class_id': '2nde'},
        ]
        for data in exercises_data:
            Exercise.objects.get_or_create(**data)
        self.stdout.write(self.style.SUCCESS(f'Created {len(exercises_data)} exercises.'))

        self.stdout.write(self.style.SUCCESS('Creating bac subjects...'))
        bac_subjects_data = [
            {'subject': 'Français', 'title': 'Sujet Bac 2023 - Français', 'pdf_url': 'https://www.africau.edu/images/default/sample.pdf'},
            {'subject': 'Mathématiques', 'title': 'Sujet Bac 2022 - Mathématiques', 'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'},
        ]
        for data in bac_subjects_data:
            BacSubject.objects.get_or_create(**data)
        self.stdout.write(self.style.SUCCESS(f'Created {len(bac_subjects_data)} bac subjects.'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))