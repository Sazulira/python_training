# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.open_home_page_for_groups()
    app.group.create(Group(name="group1", header="new group", footer="new group040519"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
    app.open_home_page_for_groups()
    app.session.logout()
