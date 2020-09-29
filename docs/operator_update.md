# How to update operator

Prerequisities:
* [Operator SDK](https://sdk.operatorframework.io/docs/installation/install-operator-sdk/)

Any changes to Ansible roles or the playbook contained within operator means the operator image needs to be rebuilt.

1. Make your changes to Ansible roles
2. Build new operator version (using optional builder flag if you use something else than default `docker` command) with: `operator-sdk build $REGISTRY/$STREAM/theforeman-operator:x.y.z --image-builder podman`
3. Push the new image into registry
4. Bump operator image version in `theforeman-operator/deploy/operator.yaml`, save and apply to make changes to your cluster.
