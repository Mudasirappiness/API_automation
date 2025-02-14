import logging

logger = logging.getLogger(__name__)

# data set
data = {
	"filters": [
		{
			"field": "is_active",
			"value": True
		},
		{
			"field": "dealer_id",
			"value": "WS6S5NlkgrgZuSUJsIa3qA=="
		},
		{
			"field": "product_main_category",
			"value": [
				3,
				1
			]
		}
	],
	"sort": {
		"field": "updated_at",
		"order": "DESC"
	},
	"page": 1,
	"list_per_page": 10
}


def test_dealer_brand_listings(stage_admin_user, caplog):
	with caplog.at_level(logging.INFO):

		"""Passing the endpoint"""
		try:
			logging.info("Passing the end point")
			url = f"{stage_admin_user.base_url}/api/admin/dealer-list-brand/"
			logging.info("Successfully done - Testcase 1.1 is passed")

			logging.info("Passing the required data to create the idea")
			response = stage_admin_user.post(url, json=data)
			logging.info("Successfully done - Testcase 1.2 is passed")

			logging.info("Validating the status code")
			assert response.status_code == 200
			logging.info("Successfully done - Testcase 1.3 is passed")

			response_data = response.json()
			print(response_data)

			logging.info("Validating the Method ")
			assert response.request.method == 'POST', "HTTP method should be Post"
			logging.info("Successfully done - Testcase 1.4 is passed")

		except AssertionError as e:
			logging.error(f"Assertion error occurred: {e}")
			raise
