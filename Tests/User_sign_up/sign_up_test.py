import requests
import selenium
import logging


data = {
    "sign_up_method": 1,
    "mobile_number": "7893387467"   #user id = 2Kaf2XDHnf/s0upMP0iNRQ=="
                                    #phone_number = 830G7Ed6WnqRkJyGSBTnYg==
}


def test_sign_up_with_number(stage_client,caplog):
    with caplog.at_level(logging.INFO):
        try:
            logging.info("Passing end point")
            url = f"{stage_client.base_url}api/user/sign-up/"
            logging.info("Successfully done - Testcase 1.1 is passed")

            logging.info("Sign up with the number")
            response = stage_client.post(url, json=data)
            logging.info("Successfully done - Testcase 1.2 is passed")

            logging.info("Validating the status code")
            assert response.status_code == 200
            logging.info("Successfully done - Testcase 1.3 is passed")

            logging.info("Validating the Method ")
            assert response.request.method == 'POST', "HTTP method should be Post"
            logging.info("Successfully done - Testcase 1.4 is passed")

        except AssertionError as e:
            logging.error(f"Assertion error occurred: {e}")
            raise





