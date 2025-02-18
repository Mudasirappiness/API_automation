import logging

logger = logging.getLogger(__name__)

# dataset

data = {
	"filters": [
		{
			"field": "742",
			"value": 7
		}
	],
	"sort": {
		"field": "updated_at",
		"order": "DESC"
	},

	"page": 1,
	"list_per_page": 10
}


def test_list_folder_details(stage_brand_user, caplog):
	with caplog.at_level(logging.INFO):
		"""Passing the end point"""
		try:
			logging.info("Passing the end point")
			url = f"{stage_brand_user.base_url}/api/user/list-detail-user-wishlist-collections/"
			logging.info("Successfully done - Testcase 1.1 is passed")

			logging.info("Passing the required data to create the idea")
			response = stage_brand_user.post(url, json=data)
			logging.info("Successfully done - Testcase 1.2 is passed")

			logging.info("Validating the status code")
			assert response.status_code == 200
			logging.info("Successfully done - Testcase 1.3 is passed")

			logging.info("Validating the Method ")
			assert response.request.method == 'POST', "HTTP method should be Post"
			logging.info("Successfully done - Testcase 1.4 is passed")

			response_json = response.json()
			print(response_json)

		except AssertionError as e:

			logging.error(f"Assertion error occurred: {e}")
			raise
