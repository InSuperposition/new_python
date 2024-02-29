docker_build('example-python-image', '.', dockerfile='containerfile')
k8s_yaml('k8s.yaml')
k8s_resource('example-python', port_forwards=8000)