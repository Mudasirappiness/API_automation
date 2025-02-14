import requests
import pytest
import logging

logger = logging.getLogger(__name__)

# data set
data = {

	"idea_id": "M++hxO8yTfawbum8Ox8rgw=="

}


def test_create_idea(stage_client, caplog):
	with caplog.at_level(logging.INFO):

		"""Passing the endpoint"""
		try:
			logging.info("Passing the end point")
			url = f"{stage_client.base_url}/api/admin/idea/idea-detail/"
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

			logging.info("Validating the details")
			response_json = response.json()
			print("This is", response_json)
			assert response.json().get("title") == 'Api testing update'
			assert response.json().get('description') == "Api automation update"
			logging.info("Successfully done - Testcase 1.5 is passed")

		except AssertionError as e:
			logging.error(f"Assertion error occurred: {e}")
			raise


