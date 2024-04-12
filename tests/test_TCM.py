
def test_new_tc(desktop_app_auth):
    desktop_app_auth.navigate_to('Create new test')
    test_name = 'jambo'
    desktop_app_auth.create_test(test_name, 'elephant')
    desktop_app_auth.navigate_to('Test Cases')
    desktop_app_auth.test_cases.check_test_exists(test_name)
    desktop_app_auth.test_cases.delete_test_by_name(test_name)


def test_new_tc_digits_name(desktop_app_auth):
    desktop_app_auth.navigate_to('Create new test')
    test_name = '1234'
    desktop_app_auth.create_test(test_name, 'elephant')
    desktop_app_auth.navigate_to('Test Cases')
    desktop_app_auth.test_cases.check_test_exists(test_name)
    desktop_app_auth.test_cases.delete_test_by_name(test_name)
