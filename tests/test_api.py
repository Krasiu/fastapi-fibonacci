from fastapi.testclient import TestClient

from app.api.main import app, celery_app

client = TestClient(app)


def test_get_root_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_get_root_returns_hello():
    response = client.get("/")
    assert response.json() == {"Hello": "Fibonacci"}


def test_get_first_n_fibonacci_numbers_returns_202(monkeypatch):
    def mock_result(*args, **kwargs):
        class Result:
            pass
        result = Result()
        result.id = "123"
        return result

    monkeypatch.setattr(celery_app, "send_task", mock_result)
    response = client.get("/fibonacci/10")
    assert response.status_code == 202


def test_get_first_n_fibonacci_numbers_with_string_path_parameter_returns_422():
    response = client.get("/fibonacci/blah")
    assert response.status_code == 422


def test_get_task_with_non_uuid_path_parameter_returns_422():
    response = client.get("/tasks/blah")
    assert response.status_code == 422

    response = client.get("/tasks/9")
    assert response.status_code == 422
