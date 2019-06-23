# -*- coding: utf-8 -*-
from model.data import Contact

def test_add_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Misha", middlename="MIO", lastname="Ivanov", nickname="MIOBN", title="MR",
                                        company="Comp", address="Moscow", home="8495", mobile="8911", work="8812",
                                        fax="84951", email="er", email2="qw", email3="yu", homepage="rewti", bday="14",
                                        bmonth="November", byear="1986", aday="18", amonth="November", ayear="1996",
                                        address2="SPb", phone2="Nevskiy", notes="none")
    app.contact.fill_form_name(contact)
    app.contact.submit_creation_new_contact()
    new_contacts = app.contact.get_contact_list()
    app.open_home_page()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


   # app.contact.open_add_new_contact_page()
