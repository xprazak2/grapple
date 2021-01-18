# How to run Foreman in K8

**WARNING: This is not yet for production.**

The `definitions` folder contains all the resource definitions needed to deploy a working Foreman instance into your Kubernetes cluster. Rather than applying each file manually, a setup playbook is included for convenience.

Prerequisities for the next steps:
* Ansible
* CRC with `oc` client configured locally and user account with sufficient permissions to create cluster-wide resources OR minkube with kubectl


## CRC

To run a playbook against your [CRC](https://github.com/code-ready/crc) cluster, execute:

```
ansible-playbook crc-setup.yaml
```

To clean-up all the created resources, run:

```
ansible-playbook crc-teardown.yaml
```

## Minikube

To run a playbook against your [CRC](https://minikube.sigs.k8s.io/docs/start/) cluster, execute:

```
ansible-playbook minikube-setup.yaml
```

To clean-up all the created resources, run:

```
ansible-playbook minikube-teardown.yaml
```
