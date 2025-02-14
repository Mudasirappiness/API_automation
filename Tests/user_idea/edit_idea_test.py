import requests
import pytest
import logging

logger = logging.getLogger(__name__)

# data set
data = {
	"image_urls": [
		{
			"url": "https://bw-production.s3.ap-south-1.amazonaws.com/Images/ideas/f2dfe339ce4eae9a.webp",
			"is_cover_image": True,
			"id": 993
		}
	],
	"title": "Api testing",
	"location": "Salem, Tamil Nadu",
	"category": 80,
	"description": "Api automation",
	"other_information": None,
	"video_urls": [],
	"tagged_products": [],
	"tagged_services": [],
	"tagged_entire_project": [],
	"id" : "j4gSIf0oS0mby8jpYpXPcw==",
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


