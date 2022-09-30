from base.functions import *


def test_subject_validation():
    # gives chrome time to load
    driver.implicitly_wait(3)
    set_order_field("112233")
    set_email("test@gmail.com")
    upload_file(image_path)
    set_message("this is a test")
    submit_form()

    # getting test evidence
    screenshot_path = "D:\\gbh project\\screenshots\\subject_validation_test.png"
    driver.get_screenshot_as_file(screenshot_path)

    # comparing error message result
    expected_result = "Please select a subject from the list provided."
    actual_result = get_warning_message()
    assert expected_result == actual_result

    driver.close()
