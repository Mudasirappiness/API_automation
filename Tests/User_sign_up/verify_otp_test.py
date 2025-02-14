import logging

import pytest
import requests

data_set = {
	"verify_method": 2,
	"verify_method_type": 1,
	"mobile_number": "PDcBtcSvkL+md1L1oeS/jw==",
	"user_id": "J3XywQHHiqVBZAtoTb+tGQ==",
	"otp": "8IjC2JZTjnisk/VEKGg1Vg=="
}


def test_verify_otp(stage_client_new_user, caplog):
	with caplog.at_level(logging.INFO):
		try:

			logging.info("Passing the end point")
			url = f"{stage_client_new_user.base_url}api/user/verify-otp/"
			logging.info("Successfully done - Testcase 1.1 is passed")

			logging.info("Verifying the OTP")
			response = stage_client_new_user.post(url, json=data_set)
			logging.info("Successfully done - Testcase 1.2 is passed")

			logging.info("Validating the status code")
			assert response.status_code == 200
			logging.info("Successfully done - Testcase 1.3 is done")

			logging.info("Validating the method")
			assert response.request.method == 'POST'
			logging.info("Successfully done - Testcase 1.4 is passed")

			logging.info("Validating the reason")
			assert response.reason == 'OK'
			logging.info("Successfully done - Testcase 1.4 is done")

		except AssertionError as e:
			logging.error(f"Assertion error occurred:{e}")
			raise
