import requests
import logging



# data set
headers = {

	"x-session": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhaSI6ImdBQUFBQUJucGF2TzdPRVVVckFUTXRKOG9rYUxaNnYtM3A1M0RTc0VMMHJkRzVmdXZGMDJrQy1xU0tHLU1YRjNYSUNTdGswNUNaQng2aWdqU0hPVU91U25MdjdiWkpTcWhRPT0iLCJtb2JpbGVfbnVtYmVyIjoiZ0FBQUFBQm5wYXZPRVc0TkR3emZYcWlmRml0TWNRUEVqYUVGZkpBTjhQN0hnWVR6YVNBZDZRd0RfZG1VOUhhanp2RUt2b21OQmRDcnVITTlma29DMTl1ajY2dWpTcnNyY2c9PSIsImVtYWlsX2lkIjoiZ0FBQUFBQm5wYXZPRHllVm1WcTFVU1JJYXJTOVNGTnF4VERvMjBnYkJySlRzcVh6VEc1a1VJc3V5Zm9RTXJ1cmVZeWVGcFBlT1hkUWJmaGMwbjQ2RFZpdzhxRzV1Rkt2bk9vVGd4SWVBYmtQX1V0OVRxZ3FTMDlOaVZSRWxvSk1xZ2pIZ0EtZ01EMXIiLCJpc191c2VyIjp0cnVlfQ.lK6Cw3HuiuFyfN6Qy8v-yCleBk6LuhfCM8U8JSY6u00"

}


def test_get_profile(stage_client_getprofile, caplog):
	with caplog.at_level(logging.INFO):

		"""Passing the endpoint"""
		try:
			logging.info("Passing the end point")
			url = f"{stage_client_getprofile.base_url}/api/user/get-profile/"
			logging.info("Successfully done - Testcase 1.1 is passed")

			logging.info("Passing the required data to create the idea")
			response = stage_client_getprofile.post(url, headers=headers)
			logging.info("Successfully done - Testcase 1.2 is passed")

			logging.info("Validating the status code")
			assert response.status_code == 200
			logging.info("Successfully done - Testcase 1.3 is passed")

			logging.info("Validating the Method ")
			assert response.request.method == 'POST', "HTTP method should be Post"
			logging.info("Successfully done - Testcase 1.4 is passed")

			logging.info("Validating the details")
			response_json = response.json()
			print(response_json)
			# print("This is", response_json)
			assert response.json().get("is_user_type_selected")== True
			logging.info("Successfully done - Testcase 1.5 is passed")

		except AssertionError as e:
			logging.error(f"Assertion error occurred: {e}")
			raise



