import logging

logger = logging.getLogger(__name__)

#dataset

data = {
    "filters": [
        {
            "field": "is_active",
            "value": True
        },
        {
            "field": "search_term",
            "value": None
        },
        {
            "field": "type_of_building",
            "value": None
        },
        {
            "field": "status",
            "value": 1
        },
        {
            "field": "location",
            "value": ""
        },
        {
            "field": "from",
            "value": None
        },
        {
            "field": "to",
            "value": None
        },
        {
            "field": "pending_media_list",
            "value": None
        }
    ],
    "sort": {
        "field": "updated_at",
        "order": "DESC"
    },
    "values": [
        "id",
        "id_user",
        "project_name",
        "client_name",
        "type_of_building",
        "location",
        "types_of_services",
        "image_urls",
        "video_urls",
        "created_at",
        "user_details",
        "project_code"
    ],
    "pending_media_count": None,
    "page": 1,
    "list_per_page": 2
}


def test_list_projects(stage_admin_user,caplog):
    with caplog.at_level(logging.INFO):
        """Passing the end point"""
        try:
            logging.info("Passing the end point")
            url = f"{stage_admin_user.base_url}/api/admin/service-provider/services-list/"
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

        except AssertionError as e:
            logging.error(f"Assertion error occurred: {e}")
            raise




