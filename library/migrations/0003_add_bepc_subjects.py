# Generated migration to add BEPC subjects

from django.db import migrations

def add_bepc_subjects(apps, schema_editor):
    Document = apps.get_model('library', 'Document')

    BEPC_SUBJECTS = [
        {
            'title': 'BEPC 2024 — Mathématiques',
            'subject': 'Mathématiques',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2023 — Mathématiques',
            'subject': 'Mathématiques',
            'pdf_url': 'https://www.africau.edu/images/default/sample.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2024 — Physique-Chimie',
            'subject': 'Physique-Chimie',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2023 — Physique-Chimie',
            'subject': 'Physique-Chimie',
            'pdf_url': 'https://www.africau.edu/images/default/sample.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2024 — SVT',
            'subject': 'Sciences de la Vie et de la Terre',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2024 — Français',
            'subject': 'Français',
            'pdf_url': 'https://www.africau.edu/images/default/sample.pdf',
            'price': 10,
        },
        {
            'title': 'BEPC 2023 — Français',
            'subject': 'Français',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 10,
        },
        {
            'title': 'BEPC 2024 — Anglais',
            'subject': 'Anglais',
            'pdf_url': 'https://www.africau.edu/images/default/sample.pdf',
            'price': 10,
        },
        {
            'title': 'BEPC 2024 — Histoire-Géographie',
            'subject': 'Histoire-Géographie',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 10,
        },
        {
            'title': 'BEPC 2023 — Histoire-Géographie',
            'subject': 'Histoire-Géographie',
            'pdf_url': 'https://www.africau.edu/images/default/sample.pdf',
            'price': 10,
        },
        {
            'title': 'BEPC 2024 — Éducation Civique',
            'subject': 'Éducation Civique',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 10,
        },
    ]

    for bepc_subject in BEPC_SUBJECTS:
        Document.objects.get_or_create(
            title=bepc_subject['title'],
            subject=bepc_subject['subject'],
            class_level='3e',
            pdf_url=bepc_subject['pdf_url'],
            price=bepc_subject['price'],
            doc_type='bepc'
        )

class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_seed_documents'),
    ]

    operations = [
        migrations.RunPython(add_bepc_subjects),
    ]