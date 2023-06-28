from app import app
from models import db, Company, Contact, JobApplication
from helpers import (
    view_apps,
    add_app,
    view_apps_by_status,
    update_app,
    print_error,
    delete_app,
)

if __name__ == "__main__":
    with app.app_context():
        print(
            """\033[32m 
  /$$$$$$  /$$   /$$       /$$$$$$$$ /$$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$
 /$$__  $$| $$$ | $$      |__  $$__/| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/
| $$  \ $$| $$$$| $$         | $$   | $$  \ $$| $$  \ $$| $$  \__/| $$ /$$/ 
| $$  | $$| $$ $$ $$         | $$   | $$$$$$$/| $$$$$$$$| $$      | $$$$$/  
| $$  | $$| $$  $$$$         | $$   | $$__  $$| $$__  $$| $$      | $$  $$  
| $$  | $$| $$\  $$$         | $$   | $$  \ $$| $$  | $$| $$    $$| $$\  $$ 
|  $$$$$$/| $$ \  $$         | $$   | $$  | $$| $$  | $$|  $$$$$$/| $$ \  $$
 \______/ |__/  \__/         |__/   |__/  |__/|__/  |__/ \______/ |__/  \__/
\033[0m"""
        )
        print("Hello, welcome to OnTrack - your personal job application manager!")
        print(" ")
        applications = db.session.query(JobApplication)

        exit_loop = False
        while exit_loop == False:
            choice = input(
                "Select your option:\n"
                "    Type 'v' to view all of your current job applications\n"
                "    Type 'a' to add a new job application\n"
                "    Type 'u' if you want to update a job application status\n"
                "    Type 's' to view your applications based on application status\n"
                "    Type 'd' if you want to delete an application\n"
                "    Type 'x' to exit\n"
            )
            if choice.lower() == "v":
                view_apps(applications)
            elif choice.lower() == "a":
                add_app()
            elif choice.lower() == "u":
                update_app(applications)
            elif choice.lower() == "s":
                view_apps_by_status()
            elif choice.lower() == "d":
                delete_app(applications)
            elif choice.lower() == "x":
                print("*****")
                print(
                    "Thank you for using OnTrack - helping you stay on track with your job search!"
                )
                print("*****")
                exit_loop = True
            else:
                print_error()
