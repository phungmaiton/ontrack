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

def add_company():
    company_name = input('Add company name: ')
    company_location = input('Add company location: ')

    new_company = Company (
        name = company_name,
        location = company_location
    )

    db.session.add(new_company)
    db.session.commit()
    return new_company.id

def add_contact():
    contact_name = input('Add contact name: ')
    contact_email = input('Add contact email: ')
    contact_phone = input('Add contact phone number with dashes: ')

    new_contact = Contact (
        name = contact_name,
        email = contact_email,
        phone_number = contact_phone
    )

    db.session.add(new_contact)
    db.session.commit()
    return new_contact.id

def add_app():
    new_company_id = add_company()
    new_contact_id = add_contact()
    title_input = input('Add job title: ')
    date_input = input('Add date of submitting application: ')
    status_input = input('Add status of application - please type "Applied," "Interview Scheduled," "Offer Received," or "Rejected": ')


    new_application = JobApplication (
        job_title = title_input,
        application_date = date_input,
        status = status_input,
        company_id = new_company_id,
        contact_id = new_contact_id
    )

    db.session.add(new_application)
    db.session.commit()


def view_apps_by_status():
    pass
