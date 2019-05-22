
def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.open_home_page_for_groups()
    app.group.modify_first_group()
    app.session.logout()