import logging

logger = logging.getLogger(__name__)

# data set
data = {
	"brand_ids": [
		"bVVElpYlZfDnvRrrrLU9uw=="
	],
	"dealer_id": "WS6S5NlkgrgZuSUJsIa3qA=="
}


def test_dealer_product_list(stage_admin_user, caplog):
	with caplog.at_level(logging.INFO):

		"""Passing the endpoint"""
		try:
			logging.info("Passing the end point")
			url = f"{stage_admin_user.base_url}/api/user/dealer-list-create/"
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
