import logging

logger = logging.getLogger(__name__)

#dataset

data = {
    "id_user": "LpK0DftzPtIo0qtGnpimog==",
    "project_name": "Dummy project",
    "project_code": "45634564565409",
    "client_name": "04274556395",
    "type_of_building_id": 154,
    "location": "Chennai, Tamil Nadu",
    "approx_service_cost": "Less than 1 crore",
    "types_of_services": [
        38
    ],
    "image_urls": [
        {
            "is_cover_image": True,
            "url": "https://buildingworld-dev.s3.ap-south-1.amazonaws.com/Images/services/8a711f5c3591831d.webp"
        }
    ],
    "video_urls": [],
    "service_keywords":"system words, export"
}


def test_create_project(stage_admin_user,caplog):
    with caplog.at_level(logging.INFO):
        """Passing the end point"""
        try:
            logging.info("Passing the end point")
            url = f"{stage_admin_user.base_url}/api/admin/service-provider/create-user-service/"
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

            logging.info("Validating the reason")
            assert response.json().get('message') == 'Created successfully'
            logging.info("Successfully done - Testcase 1.4 is passed")

        except AssertionError as e:
            logging.error(f"Assertion error occurred: {e}")
            raise




