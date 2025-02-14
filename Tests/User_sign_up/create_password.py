import logging
import requests

data_set = {
	"user_id": "J3XywQHHiqVBZAtoTb+tGQ==",
	"password": "zXoib+1GDycf3u4EW7IyeA==",
	"request_type": 2,
	"user_type": 1,
}


def test_create_password(stage_client_new_user, caplog):
	with caplog.at_level(logging.INFO):
		try:

			logging.info("Passing the end point")
			url = f"{stage_client_new_user.base_url}/api/user/create-password-with-user-type/"
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
