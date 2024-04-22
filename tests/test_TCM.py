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

def test_testcase_does_not_exist(desktop_app_auth):
    desktop_app_auth.navigate_to('Test Cases')
    desktop_app_auth.test_cases.check_test_does_not_exists('fnasfknawknfaw')

def test_git1():
    assert True