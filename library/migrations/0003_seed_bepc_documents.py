# Migration pour ajouter les sujets BEPC

from django.db import migrations

def seed_bepc_documents(apps, schema_editor):
    Document = apps.get_model('library', 'Document')

    BEPC_SUBJECTS = [
        {
            'title': 'BEPC 2024 — Mathématiques',
            'subject': 'Mathématiques',
            'class_level': '3e',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2023 — Mathématiques',
            'subject': 'Mathématiques',
            'class_level': '3e',
            'pdf_url': 'https://www.africau.edu/images/default/sample.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2024 — Français',
            'subject': 'Français',
            'class_level': '3e',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 10,
        },
        {
            'title': 'BEPC 2023 — Français',
            'subject': 'Français',
            'class_level': '3e',
            'pdf_url': 'https://www.africau.edu/images/default/sample.pdf',
            'price': 10,
        },
        {
            'title': 'BEPC 2024 — Anglais',
            'subject': 'Anglais',
            'class_level': '3e',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 10,
        },
        {
            'title': 'BEPC 2024 — Physique-Chimie',
            'subject': 'Physique-Chimie',
            'class_level': '3e',
            'pdf_url': 'https://www.africau.edu/images/default/sample.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2023 — Physique-Chimie',
            'subject': 'Physique-Chimie',
            'class_level': '3e',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2024 — SVT',
            'subject': 'Sciences de la Vie et de la Terre',
            'class_level': '3e',
            'pdf_url': 'https://www.africau.edu/images/default/sample.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2024 — Histoire-Géographie',
            'subject': 'Histoire-Géographie',
            'class_level': '3e',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 10,
        },
        {
            'title': 'BEPC 2024 — Informatique',
            'subject': 'Informatique',
            'class_level': '3e',
            'pdf_url': 'https://www.africau.edu/images/default/sample.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2023 — Informatique',
            'subject': 'Informatique',
            'class_level': '3e',
            'pdf_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
            'price': 15,
        },
        {
            'title': 'BEPC 2024 — Éducation Civique',
            'subject': 'Éducation Civique',
            'class_level': '3e',
            'pdf_url': 'https://www.africau.edu/images/default/sample.pdf',
            'price': 10,
        },
    ]

    for bepc_subject in BEPC_SUBJECTS:
        Document.objects.get_or_create(
            title=bepc_subject['title'],
            subject=bepc_subject['subject'],
            class_level=bepc_subject['class_level'],
            pdf_url=bepc_subject['pdf_url'],
            price=bepc_subject['price'],
            doc_type='bepc'
        )

class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_seed_documents'),
    ]

    operations = [
        migrations.RunPython(seed_bepc_documents),
    ]