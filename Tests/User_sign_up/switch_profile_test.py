import requests
import logging



# data set
headers = {

	"x-session": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhaSI6ImdBQUFBQUJucGU1b0VraFNxeW9IdkFzcmRCSFJFZjhGSDdDVmFCOWtsemtYbDgta2pXbVU0aUFaVHREN191M0xOSzRHX1pLY0t1MEN2amwyYlkyUUJfam13T1NaaFpDU2RnPT0iLCJtb2JpbGVfbnVtYmVyIjoiZ0FBQUFBQm5wZTVvVmpIMF83T0IyVzRvNHNMTjV2XzdROEpsNm1oSWdKZURuR1Vvb0pkNHVzSE9tVWdPWUNvb1ZjZXVUT0hGRDFzVWdjaHpkbGFaNkRjRnJkaHRIMWxvdWc9PSIsImVtYWlsX2lkIjoiZ0FBQUFBQm5wZTVvOFBVNmtHT0ZXV01fUS1vV1JTcnlhcnZpLTh5SEtNT3haMUxyQWk3Y1pKQW1vTmNKUXdLbmVURHU2VHYyTS14NTZJRmR6NG9lbjhzS3dncEY4TkpxWXc9PSIsImlzX3VzZXIiOnRydWV9.fvwQqKX8089f2PWDzl9wdGjc5iC9DtpM3g005kjOfTI"

}

data = {
	"user_type": 2
}


def test_get_profile(stage_client_getprofile, caplog):
	with caplog.at_level(logging.INFO):

		"""Passing the endpoint"""
		try:
			logging.info("Passing the end point")
			url = f"{stage_client_getprofile.base_url}/api/user/switch-profile/"
			logging.info("Successfully done - Testcase 1.1 is passed")

			logging.info("Passing the required data to create the idea")
			response = stage_client_getprofile.post(url, headers=headers, json=data)
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
			assert response.json().get("is_user_type_selected")== True
			logging.info("Successfully done - Testcase 1.5 is passed")

		except AssertionError as e:
			logging.error(f"Assertion error occurred: {e}")
			raise


