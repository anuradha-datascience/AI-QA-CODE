import pytest, yaml, google.generativeai as genai, logging, os

@pytest.fixture(scope="session")
def config():
    with open("configs/config.yaml") as f:
        return yaml.safe_load(f)["gemini"]

@pytest.fixture(scope="session", autouse=True)
def logger():
    os.makedirs("reports/logs", exist_ok=True)
    logging.basicConfig(
        filename="reports/logs/test_run.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)

@pytest.fixture(scope="session")
def gemini_client(config):
    genai.configure(api_key=config["api_key"])
    return genai.GenerativeModel(config["model"])

# conftest.py
import pytest, logging, os, yaml

@pytest.fixture(scope="session", autouse=True)
def logger():
    os.makedirs("reports/logs", exist_ok=True)
    log_file = "reports/logs/test_run.log"
    logging.basicConfig(
        filename=log_file,
        filemode="w",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    logging.info("==== Test Session Started ====")
    return logging.getLogger(__name__)

