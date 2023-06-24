from app import app
from models import db, Company, Contact, JobApplication
from faker import Faker

fake = Faker()

if __name__ == "__main__":
    with app.app_context():
        Company.query.delete()
        JobApplication.query.delete()
        Contact.query.delete()

        companies = [
            Company(
                name="Amazon",
                location="Arlington, VA",
            ),
            Company(
                name="Netflix",
                location="Remote",
            ),
            Company(
                name="Google",
                location="Washington, DC",
            ),
        ]

        db.session.add_all(companies)

        contacts = []

        for _ in range(3):
            fake_contact = Contact(
                name=fake.name(), email=fake.email(), phone_number=fake.phone_number()
            )
            contacts.append(fake_contact)

        db.session.add_all(contacts)

        job_applications = [
            JobApplication(
                job_title="Software Development Engineer",
                application_date="6/27/2023",
                status="Applied",
                company_id=1,
                contact_id=1,
            ),
            JobApplication(
                job_title="Software Engineer",
                application_date="5/27/2023",
                status="Interview Scheduled",
                company_id=2,
                contact_id=2,
            ),
            JobApplication(
                job_title="Systems Development Engineer, Google Cloud",
                application_date="6/27/2023",
                status="Applied",
                company_id=3,
                contact_id=3,
            ),
        ]

        db.session.add_all(job_applications)
        db.session.commit()
