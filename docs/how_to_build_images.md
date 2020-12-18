# How to build images

Use appropriate playbook inside `playbooks` directory to build the images you need. It is assumed that `podman` is available.

To build localhost/foreman:2.1-42 image:

```
ansible-playbook playbooks/build-foreman-image.yml -e version=2.1 -e release=42
```

To build awesome-repo/foreman:2.1-1 and push into the registry:

```
ansible-playbook playbooks/build-foreman-image.yml -e version=2.1 -e registry=awesome-repo -e registry_user=admin -e registry_token=changeme -e push=true
```

It is possible to use additional snippets to modify an image build. The expected path is `snippets/$image_name`. This is useful when you need to copy additional files into an image:

```
# Create `container-assets` which will hold additional items that will be copied to the build context.
mkdir -p snippets/foreman/container-assets

touch snippets/foreman/container-assets/add-this-to-image.txt

# Extend Dockerfile with additional steps
cat <<'EOF' >> snippets/foreman/foo.j2
COPY container-assets/add-this-to-image.txt /usr/share/foreman/add-this-to-image.txt
EOF

ansible-playbook playbooks/build-foreman-image.yml -e "{ 'version': '2.1', 'snippets': ['foo.j2'] }"

```

To install additional plugins, specify the rpm packages you wish to install. Do not forget to add your configs (smart-proxy plugins only).
If your plugin needs anything more, use the snippets as described above.

```
ansible-playbook playbooks/build-foreman-proxy-image.yml -e '{ "rpms_to_install": ["tfm-rubygem-smart_proxy_remote_execution", "tfm-rubygem-smart_proxy_remote_execution_ssh"], "configs_to_copy": ["remote_execution_ssh.yml"]}'

```

Or using a vars file:

```
cat <<'EOF' >> plugins.yaml
---
rpms_to_install:
  - tfm-rubygem-smart_proxy_remote_execution
  - tfm-rubygem-smart_proxy_remote_execution_ssh
configs_to_copy:
  - remote_execution_ssh.yml
EOF

ansible-playbook playbooks/build-foreman-proxy-image.yml -e @plugins.yaml
```
