from app import app
from models import db, Company, Contact, JobApplication

if __name__ == "__main__":
    with app.app_context():
        print("Is there a job status you want to update? (Y/n) ")
