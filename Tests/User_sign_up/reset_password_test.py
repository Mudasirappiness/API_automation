import logging
import requests

data_set = {
	"old_password": "zXoib+1GDycf3u4EW7IyeA==",
	"new_password": "1U4l2M/vIt9PDFbcbUScNQ=="
}


def test_create_password(stage_client_new_user, caplog):
	with caplog.at_level(logging.INFO):
		try:

			logging.info("Passing the end point")
			url = f"{stage_client_new_user.base_url}/api/user/reset-password/"
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

			response = response.json()
			print(response)

		# logging.info("Validating the reason")
		# assert response.reason == 'OK'
		# logging.info("Successfully done - Testcase 1.4 is done")

		except AssertionError as e:
			logging.error(f"Assertion error occurred:{e}")
			raise
