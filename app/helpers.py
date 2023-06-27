from models import db, Company, Contact, JobApplication


def view_apps(applications):
    print("-" * 129)
    print(
        f'| {"ID":<3} | {"Job Title":<45} | {"Applied Date":<12} | {"Status":<20} | {"Company":<15} | {"Contact":<15} |'
    )
    print("-" * 129)
    for application in applications:
        id_spaces = 3 - len(str(application.id))
        title_spaces = 45 - len(application.job_title)
        date_spaces = 12 - len(application.application_date)
        status_spaces = 20 - len(application.status)
        company_name = application.company.name
        company_spaces = 15 - len(company_name)
        contact_name = application.contact.name
        contact_spaces = 15 - len(contact_name)
        print(
            f'| {application.id}{" " * id_spaces} | {application.job_title}{" " * title_spaces} | {application.application_date}{" " * date_spaces} | {application.status}{" " * status_spaces} | {company_name}{" " * company_spaces} | {contact_name}{" " * contact_spaces} |'
        )
    print("-" * 129)


def add_app():
    title_input = input("Add job title: ")
    date_input = input("Add date of submitting application: ")
    status_input = input(
        'Add status of application - please type "Applied," "Interview Scheduled," "Offer Received," or "Rejected": '
    )


def update_app(applications):
    view_apps(applications)
    selected_app = input("What is the ID of the job application you want to update? ")
    updated_status = input("What is the updated status? ")
    for application in applications:
        if application.id == int(selected_app):
            application.status = updated_status.title()
    db.session.commit()
    print("Updated Applications:")
    print("-" * 129)
    print(
        f'| {"ID":<3} | {"Job Title":<45} | {"Applied Date":<12} | {"Status":<20} | {"Company":<15} | {"Contact":<15} |'
    )
    print("-" * 129)
    for application in applications:
        id_spaces = 3 - len(str(application.id))
        title_spaces = 45 - len(application.job_title)
        date_spaces = 12 - len(application.application_date)
        status_spaces = 20 - len(application.status)
        company_name = application.company.name
        company_spaces = 15 - len(company_name)
        contact_name = application.contact.name
        contact_spaces = 15 - len(contact_name)
        if application.id == int(selected_app):
            print(
                f'\033[31m\033[1m| {application.id}{" " * id_spaces} | {application.job_title}{" " * title_spaces} | {application.application_date}{" " * date_spaces} | {application.status}{" " * status_spaces} | {company_name}{" " * company_spaces} | {contact_name}{" " * contact_spaces} |\033[0m'
            )
        else:
            print(
                f'| {application.id}{" " * id_spaces} | {application.job_title}{" " * title_spaces} | {application.application_date}{" " * date_spaces} | {application.status}{" " * status_spaces} | {company_name}{" " * company_spaces} | {contact_name}{" " * contact_spaces} |'
            )
    print("-" * 129)


def view_apps_by_status():
    pass


def delete_app(applications):
    view_apps(applications)
    print(" ")
    print("Updated Applications:")
    unwanted_app_id = input("Enter the ID of the job application you want to delete: ")
    for app in applications:
        if app.id == int(unwanted_app_id):
            db.session.delete(app)
            print("Application has been deleted!")
    db.session.commit()
    view_apps(applications)


def print_error():
    print("Please choose one of the following options:")
    input(
        "    Type 'v' to view all of your current job applications\n"
        "    Type 'a' to add a new job application\n"
        "    Type 'u' if you want to update a job application status\n"
        "    Type 's' to view your applications based on application status\n"
        "    Typoe 'x' to exit\n"
    )
