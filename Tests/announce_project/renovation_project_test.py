import logging

"""Data set"""

data = {
	"project_name": "salemsse",
	"location": 470760,
	"construction_type": "8",
	"build_up_area": 21335,
	"project_type": "renovation",
	"prefered_brands": [],
	"time_line": 4,
	"description": "{\n\t\"project_name\": \"Project world\",\n\t\"location\": 470760,\n\t\"construction_type\": \"154\",\n\t\"build_up_area\": 345433,\n\t\"project_type\": \"new construction\",\n\t\"prefered_brands\": [],\n\t\"time_line\": 3,\n\t\"description\": \"hello\",\n\t\"estimated_cost\": \"Less than 1 crore\",\n\t\"services_required\": [],\n\t\"build_unit_type\": \"Sq.ft\",\n\t\"allow_call_whatsapp\": True,\n\t\"image_urls\": [\n\t\t\"https://buildingworld-dev.s3.ap-south-1.amazonaws.com/Images/products/138fba9136ffee43.webp\"\n\t]\n}",
	"estimated_cost": "Less than 5 crore",
	"services_required": [
		1
	],
	"build_unit_type": "Sq.ft",
	"allow_call_whatsapp": True,
	"image_urls": [
		"https://buildingworld-dev.s3.ap-south-1.amazonaws.com/Images/products/cbf4b490474344b7.webp"
	]
}


def test_renovation_project(stage_brand_user, caplog):
	"""Passing the end point"""
	with caplog.at_level(logging.INFO):
		try:
			logging.info("Passing the endpoint")
			url = f"{stage_brand_user.base_url}/api/user/create-announce-your-project/"
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
			assert response.json().get("message") == "Created successfully"
			logging.info("Successfully done - Testcase 1.6 is passed")

		except AssertionError as e:
			logging.error("The assertion error is {}".format(e))
			raise
