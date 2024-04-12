from playwright.sync_api import Page, expect
class TestCases:
    def __init__(self, page: Page):
        self.page = page

    def check_test_exists(self, test_name: str):
        tc = self.page.get_by_role("row", name=test_name)
        expect(tc).to_be_visible()

    def delete_test_by_name(self, test_name: str):
        self.page.get_by_role("row", name=test_name).get_by_role("button").nth(3).click()
