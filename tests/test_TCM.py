from pytest import mark

ddt = {
    'argnames': 'name, description',
    'argvalues': [
    ('jambo', 'elephant'),
    ('1234', 'digits') ],
    'ids': ['general test', 'test with digits']

}

@mark.parametrize(**ddt)
def test_new_tc(desktop_app_auth, name, description):
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to('Test Cases')
    desktop_app_auth.test_cases.check_test_exists(name)
    desktop_app_auth.test_cases.delete_test_by_name(name)

