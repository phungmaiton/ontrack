from app import app
from models import db, Company, Contact, JobApplication
# from faker import Faker

# fake = Faker()

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
            Company(
                name="Apple",
                location="Remote",
            ),
            Company(
                name="Twitter",
                location="New York, NY",
            ),
        ]

        db.session.add_all(companies)

        contacts = [
            Contact(
                name="Jessica Lee",
                email="jlee@amazon.com",
                phone_number="559-563-8901",
            ),
            Contact(
                name="Steve Lawrence",
                email="steve_lawrence@netflix.com",
                phone_number="714-332-6985",
            ),
            Contact(
                name="Brandi Wright",
                email="brandiwright@google.com",
                phone_number="887-293-6451",
            ),
            Contact(
                name="Rebecca Howard",
                email="r_howard@apple.com",
                phone_number="216-345-0193",
            ),
            Contact(
                name="Ashley Jimenez",
                email="ashleyjiminez@twitter.com",
                phone_number="522-738-9914",
            ),
        ]

        db.session.add_all(contacts)

        job_applications = [
            JobApplication(
                job_title="Software Development Engineer",
                application_date="06/27/2023",
                status="Applied",
                company_id=1,
                contact_id=1,
            ),
            JobApplication(
                job_title="Software Engineer",
                application_date="05/27/2023",
                status="Interview Scheduled",
                company_id=2,
                contact_id=2,
            ),
            JobApplication(
                job_title="Systems Development Engineer, Google Cloud",
                application_date="06/27/2023",
                status="Applied",
                company_id=3,
                contact_id=3,
            ),
            JobApplication(
                job_title="Full Stack Developer",
                application_date="06/27/2023",
                status="Rejected",
                company_id=4,
                contact_id=4,
            ),
            JobApplication(
                job_title="Android Engineer, Subscription/Commerce",
                application_date="06/27/2023",
                status="Applied",
                company_id=5,
                contact_id=5,
            ),
        ]

        db.session.add_all(job_applications)
        db.session.commit()
