from models import db, Company, Contact, JobApplication


def view_apps(applications):
    print("-" * 116)
    print(
        f'| {"ID":<3} | {"Job Title":<50} | {"Application Date":<20} | {"Status":<30} |'
    )
    print("-" * 116)
    for application in applications:
        id_spaces = 3 - len(str(application.id))
        title_spaces = 50 - len(application.job_title)
        date_spaces = 20 - len(application.application_date)
        status_spaces = 30 - len(application.status)
        print(
            f'| {application.id}{" " * id_spaces} | {application.job_title}{" " * title_spaces} | {application.application_date}{" " * date_spaces} | {application.status}{" " * status_spaces} |'
        )
    print("-" * 116)


def add_app():
    pass


def update_app(applications):
    view_apps(applications)
    selected_app = input("What is the ID of the job application you want to update? ")
    updated_status = input("What is the updated status? ")
    for application in applications:
        if application.id == int(selected_app):
            application.status = updated_status.title()
    db.session.commit()
    print("Updated Applications:")
    print("-" * 116)
    print(
        f'| {"ID":<3} | {"Job Title":<50} | {"Application Date":<20} | {"Status":<30} |'
    )
    print("-" * 116)
    for application in applications:
        id_spaces = 3 - len(str(application.id))
        title_spaces = 50 - len(application.job_title)
        date_spaces = 20 - len(application.application_date)
        status_spaces = 30 - len(application.status)
        if application.id == selected_app:
            print(
                f'\033[1m| {application.id}{" " * id_spaces} | {application.job_title}{" " * title_spaces} | {application.application_date}{" " * date_spaces} | {application.status}{" " * status_spaces} |\033[0m'
            )
        else:
            print(
                f'| {application.id}{" " * id_spaces} | {application.job_title}{" " * title_spaces} | {application.application_date}{" " * date_spaces} | {application.status}{" " * status_spaces} |'
            )
    print("-" * 116)


def view_apps_by_status():
    pass


def print_error():
    print("Please choose one of the following options:")
    input(
        "    Type 'v' to view all of your current job applications\n"
        "    Type 'a' to add a new job application\n"
        "    Type 'u' if you want to update a job application status\n"
        "    Type 's' to view your applications based on application status\n"
        "    Typoe 'x' to exit\n"
    )
