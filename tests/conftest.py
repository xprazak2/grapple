import pytest
from kubernetes import client, config

@pytest.fixture
def k8():
  config.load_kube_config()
  api = client.CoreV1Api()
  return api

def pytest_addoption(parser):
  parser.addoption("--namespace", action="store", default="theforeman-test")

@pytest.fixture
def namespace(pytestconfig):
  return pytestconfig.getoption("namespace")
