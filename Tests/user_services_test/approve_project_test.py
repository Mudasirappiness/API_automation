import logging

logger = logging.getLogger(__name__)

# dataset

data = {
	"unique_code": "qczczczdw"
}


def test_project_approve(stage_admin_user, caplog):
	with caplog.at_level(logging.INFO):
		"""Passing the end point"""
		try:
			logging.info("Passing the end point")
			url = f"{stage_admin_user.base_url}/api/admin/service-provider/change-project-status/"
			logging.info("Successfully done - Testcase 1.1 is passed")

			logging.info("Passing the required data to create the idea")
			response = stage_admin_user.post(url, json=data)
			logging.info("Successfully done - Testcase 1.2 is passed")

			logging.info("Validating the status code")
			assert response.status_code == 200
			logging.info("Successfully done - Testcase 1.3 is passed")

			logging.info("Validating the Method ")
			assert response.request.method == 'POST', "HTTP method should be Post"
			logging.info("Successfully done - Testcase 1.4 is passed")

			response_json = response.json()
			print(response_json)

			logging.info("Validating the JSON data")
			assert response_json.get("is_value_exists") == False
			logging.info("Successfully done - Testcase 1.5 is passed")

		except AssertionError as e:

			logging.error(f"Assertion error occurred: {e}")
			raise
