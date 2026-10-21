import os
import django
from datetime import time

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "dental_clinic.settings"
)

django.setup()

from my_project.models import Doctor, Doctor_work


# أيام الدوام الأسبوعية
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

new_work = []

# جلب الدكاترة الذين لا يملكون سجلات دوام لهذه الأيام
for doctor in Doctor.objects.all().iterator():

    existing_days = set(
        Doctor_work.objects.filter(
            doctor=doctor,
            date__isnull=True
        ).values_list("day", flat=True)
    )

    for day in days:
        if day not in existing_days:
            new_work.append(
                Doctor_work(
                    doctor=doctor,
                    day=day,
                    start_work=time(9, 0),
                    end_work=time(17, 0),
                    date=None
                )
            )

# إضافة سجلات الدوام دفعة واحدة
if new_work:
    Doctor_work.objects.bulk_create(
        new_work,
        batch_size=1000
    )

print(f"تمت إضافة {len(new_work)} سجل دوام جديد.")

print(
    "إجمالي سجلات الدوام:",
    Doctor_work.objects.count()
)