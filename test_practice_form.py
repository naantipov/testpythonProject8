from selene import browser, have, be, by
import os

def test_registration_form():
    browser.open('/')
    browser.element('#main-header').should(have.text('Practice Form'))

    browser.element('#firstName').should(be.blank).type('ANDREY')
    browser.element('#lastName').should(be.blank).type('ANTIPOV')
    browser.element('#userEmail').should(be.blank).type('sgsdgedsf@fdfds.com')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type('3213123132')
    browser.element('#dateOfBirthInput').click()
    browser.element('#react-datepicker__month-select').click().element(
        by.text('February')).click()
    browser.element('#react-datepicker__year-select').click().element(
        by.text('1990')).click()
    browser.element('#react-datepicker__day--004').click()
    browser.element('#subjectsInput').type('football').press_enter()
    browser.element('#hobbies-checkbox-1').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(
        'pictures/kot-kartinka.jpeg'))
    browser.element('#currentAddress').type('voronezh 18-26, ZIP 394038')
    browser.element('#react-select-3-input').type('NRC').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()

    browser.element('#modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('#table').should(have.text(
        'ANDREY ANTIPOV' and
        'sgsdgedsf@fdfds.com' and
        'Male' and
        '3213123132' and
        '4 february, 1990' and
        'English' and
        'kot-kartinka.jpeg' and
        'voronezh 18-26, ZIP 394038' and
        'NRC Delhi'
    ))
    browser.element('#closeLargeModal').press_enter()
