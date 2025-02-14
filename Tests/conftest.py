import pytest
import requests


@pytest.fixture
def stage_client():
	session = requests.session()
	session.base_url = "https://bwbeddev.buildingworld.com"
	session.headers.update(
		{
			'X-Session': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhaSI6ImdBQUFBQUJucnN4dDJwWlB6TkVfSmF2Zl9LS0sxNWdZN0pFWnUxdV81Z2RJOUpkVmx1aVNudVp6d185S0Y2Z3Z0ZnJBRHMyUHRmb1pSQ0p6TExtRFlYX2x0VkUyLXgxRVdRPT0iLCJtb2JpbGVfbnVtYmVyIjoiZ0FBQUFBQm5yc3h0QTZQa1NtdFJ3MDdUTFRkWlVMLURCd3h5aFRGMUUtaVVGMXloZko2dk1sekk4bGdqQVRHTGlXZHgzbVlBMnF0RWk1UW13elhaM2dzakRoLUxOaVRFZXc9PSIsImVtYWlsX2lkIjoiZ0FBQUFBQm5yc3h0NDk4bUY1TUlLNnJOS3F0RFBhemtwbmxiRHVqM0xwcW5KUDlJSXgwQjBPVkNFSm1yOXJKeWU1dG44ekhYV3hWVEc2ZXpFazFxNEhUaEE0YWxydFdudzN4Q2o1X0VGX1d6WlB1ampiM2tBWVU9IiwiaXNfdXNlciI6dHJ1ZX0.hhZcJYTc5t55vnLM_qRbUiDC3I6NGdghSqOA2OJGN0M',
			'Content-Type': 'application/json',

		}
	)
	yield session
	session.close()


@pytest.fixture
def stage_client_new_user():
	session = requests.session()
	session.base_url = "https://bwbeddev.buildingworld.com/"
	session.headers.update(
		{

			'Content-Type': 'application/json',
			'X-Session': '',

		}
	)
	yield session
	session.close()

@pytest.fixture
def stage_client_getprofile():
	session = requests.session()
	session.base_url = "https://bwbeddev.buildingworld.com"
	# session.headers.update(
	# 	{
	# 		'X-Session': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhaSI6ImdBQUFBQUJucGF2TzdPRVVVckFUTXRKOG9rYUxaNnYtM3A1M0RTc0VMMHJkRzVmdXZGMDJrQy1xU0tHLU1YRjNYSUNTdGswNUNaQng2aWdqU0hPVU91U25MdjdiWkpTcWhRPT0iLCJtb2JpbGVfbnVtYmVyIjoiZ0FBQUFBQm5wYXZPRVc0TkR3emZYcWlmRml0TWNRUEVqYUVGZkpBTjhQN0hnWVR6YVNBZDZRd0RfZG1VOUhhanp2RUt2b21OQmRDcnVITTlma29DMTl1ajY2dWpTcnNyY2c9PSIsImVtYWlsX2lkIjoiZ0FBQUFBQm5wYXZPRHllVm1WcTFVU1JJYXJTOVNGTnF4VERvMjBnYkJySlRzcVh6VEc1a1VJc3V5Zm9RTXJ1cmVZeWVGcFBlT1hkUWJmaGMwbjQ2RFZpdzhxRzV1Rkt2bk9vVGd4SWVBYmtQX1V0OVRxZ3FTMDlOaVZSRWxvSk1xZ2pIZ0EtZ01EMXIiLCJpc191c2VyIjp0cnVlfQ.lK6Cw3HuiuFyfN6Qy8v-yCleBk6LuhfCM8U8JSY6u00',
	# 		# 'Content-Type': 'application/json',
	#
	# 	}
	# )
	yield session
	session.close()

@pytest.fixture
def stage_admin_user():
	session = requests.session()
	session.base_url = "https://bwbeddev.buildingworld.com"
	session.headers.update(
		{
			'X-Session': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhaSI6ImdBQUFBQUJucmI2ekF2Y01XM18yVW85Z19vRHV4WUdDUmRFa1diMDZmSDlKX2ZMSUNUYXpiYlQtUjBvUUc2SkFXT2JsUVdnd2JTZXA4allqa1FpdzM1ZkxGSl9EalZ6RUJnPT0iLCJiaSI6ImdBQUFBQUJucmI2ejNiTkVTSnYyWGRvZ3pzRVlUMFJaaW5lSk9FSnJ2ZFFpLXNlYnVqRWN3dDVPYTZnTHR6UWdXWVREbUE4RDRLLUFfNERheUlsMzB5TlBrNXNwTnRwejNQWUZwU2RLcUhNQTlPeUstRlpkS1VZPSIsImNpIjoiZ0FBQUFBQm5yYjZ6cVQwVUl0c25ZMGs5dkhWNHBhUkV4M0hoaGE3dFBvdjQ0VURXblB6c3AwWWxkWWVnaDNDcjBJUUxXSW90U0FWY0tJeUZPaFRudTdISUo3cGRYV29IN0E9PSIsInBhc3N3b3JkIjoiZ0FBQUFBQm5yYjZ6bU96X2xiTGE2bXZXMlhPSGlUS19sVFhsU25VV2ZMNTNiNXJWWXUzQUlxc2pqV3RkZExUMV9mSWwzZWV0akRDT2RldzhaS0ZySE1IUDIwdHRqUlNGOUhLMXVsOG90Y2FDNTRBcVRsY2hzNVdjR3BuU1dub2tIX1lSWTd5Q3RzbTJVaXZHNXpwMTdsejdJLURjTDBDNkVJbXRwWXNZTDAtU3FLdURGZUxJWjdGZWp2OWNVOWYxN3BIOWdvbm1PcnpYIn0.-dI7l0G6lIZZ4OH2_vxKwbrpHjzCoMR484VL5K-_4Z0',

			'Content-Type': 'application/json',

		}
	)
	yield session
	session.close()



