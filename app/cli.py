from app import app
from models import db, Company, Contact, JobApplication
from helpers import view_apps, add_app, view_apps_by_status

if __name__ == "__main__":
    with app.app_context():
        print("*****")
        print("Hello, welcome to OnTrack - your personal job application manager!")
        print("*****")

        applications = db.session.query(JobApplication)

        choice = input(
            f'Type "v" to view all of your current job applications, type "a" to add a new job application, or type "s" to view your applications based on application status: '
        )
        if choice.lower() == "v":
            view_apps(applications)
        # elif choice.lower() == "a":
        #     add_app()
        # elif choice.lower() == "s":
        #     view_apps_by_status()
        # else:
        #     print(
        #         'Please try again! Type "v" to view all of your current job applications, type "a" to add a new job application, or type "s" to view your applications based on application status: '
        #     )
