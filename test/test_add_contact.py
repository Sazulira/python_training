# -*- coding: utf-8 -*-
import pytest
from model.data import Contact
from fixture.Apps import Apps

@pytest.fixture
def app(request):
    fixture = Apps()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_add_new_contact_page()
    app.fill_form_name( Contact(firstname="Misha", middlename="MIO", lastname="Ivanov", nickname="MIOBN", title="MR",
                                        company="Comp", address="Moscow", home="8495", mobile="8911", work="8812",
                                        fax="84951", email="er", email2="qw", email3="yu", homepage="rewti", bday="14",
                                        bmonth="November", byear="1986", aday="18", amonth="November", ayear="1996",
                                        address2="SPb", phone2="Nevskiy", notes="none"))
    app.submit_creation_new_contact()
    app.logout()