#Project
about ....
## Playwright automation with python
Test project to show
 * features of MS Playwright on Python
 * automation project structure using pytest
Tools:
 * [Playwright](https://playwright.dev/)
 * [Pytest](https://playwright.dev/)
 * PyCharm

## Install guide

1. Install python
2. Install PyCharm
3. Install python dependencies pip3 install -r requirements.txt
4. Make sure playwright version 1.8+ installed

## Project structure

* conftest.py file contains main fixtures of work
* Page objects stored in page_object folder
* Tests stored in tests folder
* Settings are spread between:
  * pytest.ini
  * settings.py

## Run guide
1. Create file secure.json for logins and passwords. Structure:
{
  "login": "login",
  "password": "password"
}
2. Install software to test Test-Me
3. Run Test-Me (check guide in it's repo)
4. Run test using command pytest

## Useful links
- https://playwright.dev/
- https://github.com/microsoft/playwright-python