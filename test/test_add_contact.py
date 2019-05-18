# -*- coding: utf-8 -*-
from model.data import Contact

def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_add_new_contact_page()
    app.contact.fill_form_name(Contact(firstname="Misha", middlename="MIO", lastname="Ivanov", nickname="MIOBN", title="MR",
                                        company="Comp", address="Moscow", home="8495", mobile="8911", work="8812",
                                        fax="84951", email="er", email2="qw", email3="yu", homepage="rewti", bday="14",
                                        bmonth="November", byear="1986", aday="18", amonth="November", ayear="1996",
                                        address2="SPb", phone2="Nevskiy", notes="none"))
    app.contact.submit_creation_new_contact()
    app.session.logout()

