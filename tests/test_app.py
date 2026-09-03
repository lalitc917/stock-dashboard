from app.app import app


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200


def test_health_response():
    client = app.test_client()

    response = client.get("/health")

    assert response.json["status"] == "healthy"


def test_dashboard_endpoint():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200