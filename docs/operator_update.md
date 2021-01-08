# How to update operator

Any changes to Ansible roles or the playbook contained within operator means the operator image needs to be rebuilt. There are 2 ways to do that:

## With Operator SDK

Prerequisities:
* [Operator SDK](https://sdk.operatorframework.io/docs/installation/install-operator-sdk/)

1. Make your changes to Ansible roles
2. Build new operator version (using optional builder flag if you use something else than default `docker` command) with: `operator-sdk build $REGISTRY/$STREAM/theforeman-operator:x.y.z --image-builder podman`

## With included playbook

1. Make your changes to Ansible roles
2. `ansible-playbook playbooks/build_operator.yml -e image=theforeman-operator:x.y.z`
