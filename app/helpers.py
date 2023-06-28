from models import db, Company, Contact, JobApplication
from datetime import datetime, timedelta
import subprocess
import schedule
import time


def view_companies(companies):
    print("-" * 48)
    print(f'| {"ID":<3} | {"Company Name":<15} | {"Location":<20} |')
    print("-" * 48)
    for company in companies:
        company_id_spaces = 3 - len(str(company.id))
        company_name_spaces = 15 - len(company.name)
        company_location_spaces = 20 - len(company.location)
        print(
            f'| {company.id}{" " * company_id_spaces} | {company.name}{" " * company_name_spaces} | {company.location}{" " * company_location_spaces} |'
        )
    print("-" * 48)


def view_contacts(contacts):
    print("-" * 90)
    print(
        f'| {"ID":<3} | {"Contact Name":<22} | {"Email":<30} | {"Phone Number":<22} |'
    )
    print("-" * 90)
    for contact in contacts:
        contact_id_spaces = 3 - len(str(contact.id))
        contact_name_spaces = 22 - len(contact.name)
        contact_email_spaces = 30 - len(contact.email)
        contact_phone_spaces = 22 - len(contact.phone_number)
        print(
            f'| {contact.id}{" " * contact_id_spaces} | {contact.name}{" " * contact_name_spaces} | {contact.email}{" " * contact_email_spaces} | {contact.phone_number}{" " * contact_phone_spaces} |'
        )
    print("-" * 90)


def view_apps(applications, companies, contacts):
    print("-" * 131)
    print(
        f'| {"ID":<3} | {"Job Title":<45} | {"Applied Date":<12} | {"Status":<20} | {"Company":<15} | {"Contact":<17} |'
    )
    print("-" * 131)
    for application in applications:
        id_spaces = 3 - len(str(application.id))
        title_spaces = 45 - len(application.job_title)
        date_spaces = 12 - len(application.application_date)
        status_spaces = 20 - len(application.status)
        company_name = application.company.name
        company_spaces = 15 - len(company_name)
        contact_name = application.contact.name
        contact_spaces = 17 - len(contact_name)
        print(
            f'| {application.id}{" " * id_spaces} | {application.job_title}{" " * title_spaces} | {application.application_date}{" " * date_spaces} | {application.status}{" " * status_spaces} | {company_name}{" " * company_spaces} | {contact_name}{" " * contact_spaces} |'
        )
    print("-" * 131)
    print("")
    view_choice = input(
        "    To view the list of companies, type '1'\n"
        "    To view the list of contacts, type '2'\n"
        "    To go back to the main menu, press any other key\n"
    )
    if view_choice == "1":
        view_companies(companies)
    elif view_choice == "2":
        view_contacts(contacts)


def add_company():
    company_name = input("Add company name: ")
    company_location = input("Add company location: ")

    new_company = Company(name=company_name, location=company_location)

    db.session.add(new_company)
    db.session.commit()
    return new_company.id


def add_contact():
    contact_name = input("Add contact name: ")
    contact_email = input("Add contact email: ")
    contact_phone = input("Add contact phone number with dashes: ")

    new_contact = Contact(
        name=contact_name, email=contact_email, phone_number=contact_phone
    )

    db.session.add(new_contact)
    db.session.commit()
    return new_contact.id


def add_app():
    new_company_id = add_company()
    new_contact_id = add_contact()

    title_input = input("Add job title: ")
    date_input = input("Add date of submitting application: ")
    status_input = input(
        'Add status of application - please type "Applied," "Interview Scheduled," "Offer Received," or "Rejected": '
    )

    new_application = JobApplication(
        job_title=title_input,
        application_date=date_input,
        status=status_input,
        company_id=new_company_id,
        contact_id=new_contact_id,
    )

    db.session.add(new_application)
    db.session.commit()

    db.session.add(new_application)
    db.session.commit()
    print("")
    print("You've successfully added a new job application!")
    print("")


def view_app(applications):
    print("-" * 131)
    print(
        f'| {"ID":<3} | {"Job Title":<45} | {"Applied Date":<12} | {"Status":<20} | {"Company":<15} | {"Contact":<17} |'
    )
    print("-" * 131)
    for application in applications:
        id_spaces = 3 - len(str(application.id))
        title_spaces = 45 - len(application.job_title)
        date_spaces = 12 - len(application.application_date)
        status_spaces = 20 - len(application.status)
        company_name = application.company.name
        company_spaces = 15 - len(company_name)
        contact_name = application.contact.name
        contact_spaces = 17 - len(contact_name)
        print(
            f'| {application.id}{" " * id_spaces} | {application.job_title}{" " * title_spaces} | {application.application_date}{" " * date_spaces} | {application.status}{" " * status_spaces} | {company_name}{" " * company_spaces} | {contact_name}{" " * contact_spaces} |'
        )
    print("-" * 131)


def update_app(applications):
    view_app(applications)
    selected_app = input("What is the ID of the job application you want to update? ")
    updated_status = input("What is the updated status? ")
    for application in applications:
        if application.id == int(selected_app):
            application.status = updated_status.title()
    db.session.commit()
    print("Updated Applications:")
    print("-" * 131)
    print(
        f'| {"ID":<3} | {"Job Title":<45} | {"Applied Date":<12} | {"Status":<20} | {"Company":<15} | {"Contact":<17} |'
    )
    print("-" * 131)
    for application in applications:
        id_spaces = 3 - len(str(application.id))
        title_spaces = 45 - len(application.job_title)
        date_spaces = 12 - len(application.application_date)
        status_spaces = 20 - len(application.status)
        company_name = application.company.name
        company_spaces = 15 - len(company_name)
        contact_name = application.contact.name
        contact_spaces = 17 - len(contact_name)
        if application.id == int(selected_app):
            print(
                f'\033[31m\033[1m| {application.id}{" " * id_spaces} | {application.job_title}{" " * title_spaces} | {application.application_date}{" " * date_spaces} | {application.status}{" " * status_spaces} | {company_name}{" " * company_spaces} | {contact_name}{" " * contact_spaces} |\033[0m'
            )
        else:
            print(
                f'| {application.id}{" " * id_spaces} | {application.job_title}{" " * title_spaces} | {application.application_date}{" " * date_spaces} | {application.status}{" " * status_spaces} | {company_name}{" " * company_spaces} | {contact_name}{" " * contact_spaces} |'
            )
    print("-" * 131)


def view_apps_by_status():
    pass


def delete_app(applications):
    view_app(applications)
    print(" ")
    print("Updated Applications:")
    unwanted_app_id = input("Enter the ID of the job application you want to delete: ")
    for app in applications:
        if app.id == int(unwanted_app_id):
            db.session.delete(app)
            print("Application has been deleted!")
    db.session.commit()
    view_app(applications)


def send_mail(user_email, subject, body):
    command_args = ["pmail", user_email, subject, body]
    try:
        subprocess.run(command_args, check=True)
        print("Email sent successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending email: {e}")


def schedule_task(user_email, subject, body):
    send_mail(user_email, subject, body)


def reminder(applications):
    view_app(applications)
    app_id = input("Enter the ID of the application for this reminder: ")
    when = int(
        input("In how many days would you like to be reminded? Just enter the number: ")
    )
    user_email = input("Enter the email address to receive notification: ")
    reminder_message = input("Enter the reminder message: ")
    today = datetime.today().date()
    remind_date = today + timedelta(days=when)
    remind_datetime_str = remind_date.strftime("%Y-%m-%d")
    print(
        f"You will be reminded on \033[1;32m{remind_datetime_str} at 00:00\033[0m about the following job application:"
    )

    for application in applications:
        if application.id == int(app_id):
            print("-" * 131)
            print(
                f'| {"ID":<3} | {"Job Title":<45} | {"Applied Date":<12} | {"Status":<20} | {"Company":<15} | {"Contact":<17} |'
            )
            print("-" * 131)
            id_spaces = 3 - len(str(application.id))
            title_spaces = 45 - len(application.job_title)
            date_spaces = 12 - len(application.application_date)
            status_spaces = 20 - len(application.status)
            company_name = application.company.name
            company_spaces = 15 - len(company_name)
            contact_name = application.contact.name
            contact_spaces = 17 - len(contact_name)
            print(
                f'| {application.id}{" " * id_spaces} | {application.job_title}{" " * title_spaces} | {application.application_date}{" " * date_spaces} | {application.status}{" " * status_spaces} | {company_name}{" " * company_spaces} | {contact_name}{" " * contact_spaces} |'
            )
            print("-" * 131)

            subject = f"Reminder about {application.job_title}"
            body = f"Regarding {application.job_title} at {application.company.name}.\nHere's your message: {reminder_message}.\nGood luck!"
            schedule.every().day.at("00:00").do(
                schedule_task, user_email, subject, body
            ).tag(remind_datetime_str)


def print_error():
    print("Please choose one of the following options:")
    input(
        "    Type 'v' to view all of your current job applications\n"
        "    Type 'a' to add a new job application\n"
        "    Type 'u' if you want to update a job application status\n"
        "    Type 's' to view your applications based on application status\n"
        "    Type 'r' if you want to to set a reminder\n"
        "    Type 'd' if you want to delete an application\n"
        "    Type 'x' to exit\n"
    )
