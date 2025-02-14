import logging
import requests

data_set = {
	"first_name": "Pranav Traders",
	"profile_image_url": None,
	"user_id_type": 1,
	"user_id_number": "ABCDE1234F",
	"user_id_image_url": "https://buildingworld-dev.s3.ap-south-1.amazonaws.com/Images/users/profile_pic/a8432dc0328326d6.webp",
	"whatsapp_number": None,
	"dob": None,
	"gender": None,
	"city": "Salem, Tamil Nadu",
	"address": None
}


def test_update_profile(stage_client_new_user, caplog):
	with caplog.at_level(logging.INFO):
		try:

			logging.info("Passing the end point")
			url = f"{stage_client_new_user.base_url}/api/user/update-profile/"
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
