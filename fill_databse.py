from job_finder.models import Vacancy, Company, Specialty
from data import jobs, companies, specialties

companies_dictionary = dict()

for company in companies:
    tmp = Company(
                    id=company["id"],
                    name=company["title"],
                    location=company["location"],
                    logo=company["logo"],
                    description=company["description"],
                    employee_count=company["employee_count"],
                )
    tmp.save()
    companies_dictionary[company["id"]] = tmp
print(companies_dictionary)

specialties_dictionary = dict()

for specialty in specialties:
    tmp = Specialty(
                    code=specialty["code"],
                    title=specialty["title"],
                    )
    tmp.save()
    specialties_dictionary[specialty["code"]] = tmp

print(specialties_dictionary)

for job in jobs:
    tmp = Vacancy(
                    id=job["id"],
                    title=job["title"],
                    specialty=specialties_dictionary[job["specialty"]],
                    company=companies_dictionary[job["company"]],
                    skills=job["skills"],
                    description=job["description"],
                    salary_min=job["salary_from"],
                    salary_max=job["salary_to"],
                    published_at=job["posted"],
                )
    tmp.save()
    print(tmp)
