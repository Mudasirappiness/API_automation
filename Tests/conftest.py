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
			'X-Session': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhaSI6ImdBQUFBQUJuc3Y0VkYxRDRpejRqVjNMeDFaMXVrek5kUm5TWGNOaVhQSE5Wam1ZTkU0TExMVE40MGZvcXpsSUNCZWRoR25EdVJLZ2RzV0N5NmJyX3JaMERFcGF2aklhYnFRPT0iLCJiaSI6ImdBQUFBQUJuc3Y0VjRiSkRDdS1zLVlpNGRLalNyYXR4NjZ4ck1udVJkTVh2REZ3VEZkdnpRaEFLVzNGU1ZfWGppTC1Mc2tIcjR6Nmt6Nkg2RzJhb1FkM2tGN094cC1DZUtYd2FXUnRfSm9vNEVhc1NkV3IxWlZJPSIsImNpIjoiZ0FBQUFBQm5zdjRWdkR5MGU5b1NlZnFkNlZIeGlvODZJTkRhZ29Hd3dNYVp4VFVSaWlYcVBveGZrUVpueGRtcjZacFltSlZ1ekxvcWpQMVJXcktveHI4cURqRHBuZ1RZNGc9PSIsInBhc3N3b3JkIjoiZ0FBQUFBQm5zdjRWZ3Bsa19GT2ZWakhCbVBvbjhBSVRwaTFrRXBjdUY1VFM4Vks3ZW5yckk3Qy1DQW5kcnV3RW1nYWFWNmN3ZER6ajMyYmhEUy12dE5xb01EZk1MeUFNZERjR2JlS2hueHhoTlppWWs2QnFEWXc1c0h6cDZnaWRNSHB0TTVMcnJCX2E1YWREcTRKeGtUckxsQlpEWHBMemFfUmVlYmpKYVRiSWFjQ1VKZ2JqMEw0eGdoclAyQ3V6VGhrb2tjbFdQeFVLIn0.3_VFf9Vz62YGSysogc2wDlFY3WmocOcQsc3I8p9Sgq8',

			'Content-Type': 'application/json',

		}
	)
	yield session
	session.close()


@pytest.fixture
def stage_brand_user():
	session = requests.session()
	session.base_url = "https://bwbeddev.buildingworld.com"
	session.headers.update(
		{
			'X-Session': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhaSI6ImdBQUFBQUJudUI1UTFIcTVvb1psN2VLSFFiNGVNNFYyQzZGZmdfVnFfY3lTNnF0Q01MWHNPcTYxUkhvaDNhNmRXYkM1cVhBaDV2QUhXbTJQUHFYZFZjYkdfcmhESGRQc0dBPT0iLCJtb2JpbGVfbnVtYmVyIjoiZ0FBQUFBQm51QjVRVkh3LVQzbHdtcWR2WWU3QnJ1U0lXcjZlRFVYMzUzTTNBMEtwRWR1THlDY19tdWV6eTVpNVpTTUlieDNhdDBQdGIyQTlhb29xZ3U3d0xSUXM0X0dmVUE9PSIsImVtYWlsX2lkIjoiZ0FBQUFBQm51QjVRc0RjTEZCWXhaekJPMkt4RGJfVk00cXJqamNZZnE4S2YwTmU0SlI4M1lUQzY2aXZ1VEJvX0VQWmswR3NxUUszaE5jOVQxVW9pdXlDN09sMVB6TVpiRW1zdFBleGpfZkN4ZjYzNHNnY3FjZ29TaUdJejVlaDJNa0wzUGwwT2d3MzIiLCJpc191c2VyIjp0cnVlfQ.6EXIsQrvVR5pCYmTRPyWHXNFpKFmYQFK0eUGhXBU96Q',
			'Content -Type' : 'application/json',
		}
	)
	yield session
	session.close()



