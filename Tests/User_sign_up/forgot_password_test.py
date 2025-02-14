import requests
import pytest
import logging

# data set
data = {
    "email_id": "DWwWwef7MnsPKvSMDLjf74aVlOxSmnSR2uo3jk0G3NY="
}


def test_create_idea(stage_client, caplog):
	with caplog.at_level(logging.INFO):

		"""Passing the endpoint"""
		try:
			logging.info("Passing the end point")
			url = f"{stage_client.base_url}/api/user/forgot-password/"
			logging.info("Successfully done - Testcase 1.1 is passed")

			logging.info("Passing the required data to create the idea")
			response = stage_client.post(url, json=data)
			logging.info("Successfully done - Testcase 1.2 is passed")

			logging.info("Validating the status code")
			assert response.status_code == 200
			logging.info("Successfully done - Testcase 1.3 is passed")

			logging.info("Validating the Method ")
			assert response.request.method == 'POST', "HTTP method should be Post"
			logging.info("Successfully done - Testcase 1.4 is passed")

			response_json = response.json()
			print("Response JSON:", response_json)

			logging.info("Validating the reason")
			assert response.json().get('status') == 'OTP sent successfully'
			logging.info("Successfully done - Testcase 1.5 is passed")

		except AssertionError as e:
			logging.error(f"Assertion error occurred: {e}")
			raise

