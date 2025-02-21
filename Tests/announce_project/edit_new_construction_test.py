import logging

"""Data set"""

data ={
    "project_name": "Abdulah",
    "location": 470760,
    "construction_type": "3",
    "build_up_area": 9383,
    "project_type": "new construction",
    "prefered_brands": [],
    "time_line": 3,
    "description": "salem",
    "estimated_cost": "Less than 10 crore",
    "services_required": [],
    "build_unit_type": "Sq.ft",
    "allow_call_whatsapp": True,
    "image_urls": [
        {
            "id": 506,
            "url": "https://buildingworld-dev.s3.ap-south-1.amazonaws.com/Images/products/f4b490474344b7ec.webp"
        }
    ],
    "announce_your_project_slug": "dot5zo-new-construction",
    "deleted_media_ids": []
}


def test_edit_new_construction(stage_brand_user, caplog):
	"""Passing the end point"""
	with caplog.at_level(logging.INFO):
		try:
			logging.info("Passing the endpoint")
			url = f"{stage_brand_user.base_url}/api/user/edit-announce-your-project/"
			logging.info("Successfully done - Testcase 1.1 is passed")

			logging.info("Passing the required data for the endpoint")
			response = stage_brand_user.post(url, json=data)
			logging.info("Successfully done - Testcase 1.2 is passed")

			logging.info("Validating the status code")
			assert response.status_code == 200
			logging.info("Successfully done- Testcase 1.3 is passed")

			logging.info("Validating the reason")
			assert response.reason == "OK"
			logging.info("Successfully done - Testcase 1.4 is passed")

			logging.info("Validating the Http method")
			assert response.request.method == 'POST'
			logging.info("Successfully done - Testcase 1.5 is passed")

			print(response.json())

			logging.info("Validating the response data")
			assert response.json().get("message") == "Updated successfully"
			logging.info("Successfully done - Testcase 1.6 is passed")

		except AssertionError as e:
			logging.error("The assertion error is {}".format(e))
			raise
