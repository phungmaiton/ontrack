from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    website = db.Column(db.String)
    industry = db.Column(db.String)
    location = db.Column(db.String)

    contacts = db.relationship(
        "Contact",
        secondary="job_applications",
        back_populates="companies",
    )

    def __repr__(self):
        return f"<Company {self.name}"


class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.String)

    companies = db.relationship(
        "Company",
        secondary="job_applications",
        back_populates="contacts",
    )

    def __repr__(self):
        return f"<Contact {self.name}"


class JobApplication(db.Model):
    __tablename__ = "job_applications"

    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String)
    application_date = db.Column(db.String)
    status = db.Column(db.String)

    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    contact_id = db.Column(db.Integer, db.ForeignKey("contacts.id"))

    def __repr__(self):
        return f"<Job Application {self.job_title}"


# Flask db revision --autogenerate -m "message if you want"
# Flask db upgrade : run if a new column is added
