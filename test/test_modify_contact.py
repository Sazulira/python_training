from model.data import Contact

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Misha", middlename="MIO", lastname="Ivanov", nickname="MIOBN", title="MR",
                                        company="Comp", address="Moscow", home="8495", mobile="8911", work="8812",
                                        fax="84951", email="er", email2="qw", email3="yu", homepage="rewti", bday="14",
                                        bmonth="November", byear="1986", aday="18", amonth="November", ayear="1996",
                                        address2="SPb", phone2="Nevskiy", notes="none"))
        app.contact.submit_creation_new_contact()
    app.contact.modify_first_contact()
