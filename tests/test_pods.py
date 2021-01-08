def test_foreman_pod_running(k8, namespace):
  assert_pod_running(k8, namespace, "app=foreman", "oprazak/foreman:2.0-1")


def test_postgres_pod_running(k8, namespace):
  assert_pod_running(k8, namespace, "app=postgres", "centos/postgresql-12-centos7")


def test_redis_pod_running(k8, namespace):
  assert_pod_running(k8, namespace, "app=redis", "redis")


def assert_pod_running(api, namespace, label, image):
  pods = api.list_namespaced_pod(namespace, label_selector=label).items

  assert len(pods) == 1

  pod = pods.pop()
  assert pod.spec.containers[0].image == image
  assert pod.status.phase == "Running"
