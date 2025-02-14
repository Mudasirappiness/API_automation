import requests
import pytest
import logging


# data set
data = {
	"image_urls": [
		{
			"url": "https://buildingworld-dev.s3.ap-south-1.amazonaws.com/Images/ideas/85d5b0b4ed3b23aa.webp",
			"is_cover_image": True,
			"id": 993
		}
	],
	"title": "Api testing update",
	"location": "Salem, Tamil Nadu",
	"category": 80,
	"description": "Api automation update",
	"other_information": None,
	"video_urls": [],
	"tagged_products": [],
	"tagged_services": [],
	"tagged_entire_project": [],
	"id": "M++hxO8yTfawbum8Ox8rgw==",
	"deleted_media_ids": []
}


def test_create_idea(stage_client, caplog):
	with caplog.at_level(logging.INFO):

		"""Passing the endpoint"""
		try:
			logging.info("Passing the end point")
			url = f"{stage_client.base_url}/api/admin/idea/create-edit-idea/"
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

			logging.info("Validating the reason")
			assert response.json().get('message') == 'Updated successfully'
			logging.info("Successfully done - Testcase 1.4 is passed")

		except AssertionError as e:
			logging.error(f"Assertion error occurred: {e}")
			raise


