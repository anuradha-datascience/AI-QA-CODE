import pytest, requests


@pytest.mark.api
def test_basic_get(logger):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    logger.info(f"Testing GET {url}")
    response = requests.get(url)
    assert response.status_code == 200
    logger.info(f"Response OK with title: {response.json()['title']}")


@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_get_post(base_url):
    resp = requests.get(f"{base_url}/posts/1")
    assert resp.status_code == 200
    data = resp.json()
    assert "title" in data
    assert len(data["title"]) > 0
