import requests
import pytest
import logging


# data set
data = {
	"filters": [
		{
			"field": "is_active",
			"value": True
		},
		{
			"field": "status",
			"value": 1
		}
	],
	"sort": {
		"field": "created_at",
		"order": "DESC"
	},
	"values": [
		"id",
		"id_user",
		"id_admin_user"
	],
	"page": 1,
	"list_per_page": 10
}


def test_create_idea(stage_client, caplog):
	with caplog.at_level(logging.INFO):

		"""Passing the endpoint"""
		try:
			logging.info("Passing the end point")
			url = f"{stage_client.base_url}api/admin/idea/idea-list/"
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
			assert "results" in response_json
			assert isinstance(response_json['results'], list), "'results' should be a list"
			for item in response_json['results']:
				assert 'id', 'id_admin_user_name' in item
				assert item['id'], item['id_admin_user_name'] is not None

		except AssertionError as e:
			logging.error(f"Assertion error occurred: {e}")
			raise
