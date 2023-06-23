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
    pass #hi


def view_apps_by_status():
    pass
