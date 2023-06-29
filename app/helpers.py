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
    print("-" * 79)
    print(
        f'| {"ID":<3} | {"Contact Name":<19} | {"Email":<30} | {"Phone Number":<14} |'
    )
    print("-" * 79)
    for contact in contacts:
        contact_id_spaces = 3 - len(str(contact.id))
        contact_name_spaces = 19 - len(contact.name)
        contact_email_spaces = 30 - len(contact.email)
        contact_phone_spaces = 14 - len(contact.phone_number)
        print(
            f'| {contact.id}{" " * contact_id_spaces} | {contact.name}{" " * contact_name_spaces} | {contact.email}{" " * contact_email_spaces} | {contact.phone_number}{" " * contact_phone_spaces} |'
        )
    print("-" * 79)


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
        "    To go back to the main menu, press any other key (ie. 'Enter')\n"
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

    title_input = input("Add job title of the position you're applying for: ")
    date_input = input("Add date of submitting application in MM/DD/YYYY format: ")
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
    print("\033[32m\033[1mYou've successfully added a new job application to your list!\033[0m")
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
    updated_status = input("What is the updated status? Please type 'Applied,' 'Interview Scheduled,' 'Offer Received,' or 'Rejected': ")
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
        input("In how many days would you like to be reminded? Enter the number: ")
    )
    user_email = input("Enter your email address to receive notification: ")
    reminder_message = input("Enter the reminder message: ")
    today = datetime.today().date()
    remind_date = today + timedelta(days=when)
    remind_datetime_str = remind_date.strftime("%Y-%m-%d") + " 00:00"
    remind_datetime = datetime.strptime(remind_datetime_str, "%Y-%m-%d %H:%M")
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

            subject = f"Reminder about the {application.job_title} Application"
            body = f"Regarding {application.job_title} at {application.company.name}.\nHere's your message: {reminder_message}.\nGood luck!"

            # Comment this out and uncomment the testing codes

            schedule.every().day.at(remind_datetime.strftime("%H:%M")).do(
                schedule_task, user_email, subject, body
            ).tag(remind_datetime_str)

            # For testing purposes

            # now = datetime.now()
            # scheduled_time = now + timedelta(seconds=10)
            # schedule.every().day.at(scheduled_time.strftime("%H:%M")).do(
            #     schedule_task, user_email, subject, body
            # )

            while True:
                schedule.run_pending()
                time.sleep(1)


def print_error():
    print("Invalid option - please see the main menu below")