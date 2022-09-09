Ref to [Install k8s with Ansible use root user on ubuntu 18.04](https://github.com/yanmo96/alcor-perf/tree/ansible_k8s/scripts/ansible-playbook/k8s_deploy_fresh_machine)
### Step 1: Preparation
准备两个node节点，一个做master，另一个做worker  
分发master的private key到worker实现ssh免密登录  
通过apt安装python3-dev python3-venv libffi-dev gcc libssl-dev git docker ansible  
配置ansible主机
```bash
mkdir ~/kube-cluster
cd ~/kube-cluster
vim ~/kube-cluster/hosts
###hosts文件，master_ip和worker_1_ip分别为master和worker的ip地址
[masters]
master ansible_host=master_ip ansible_user=root

[workers]
worker1 ansible_host=worker_1_ip ansible_user=root

[all:vars]
ansible_python_interpreter=/usr/bin/python3
```
### Step 2: Install K8s dependencies 
install k8s images(master+worker)
```bash
docker pull k8s.gcr.io/kube-apiserver:v1.19.16 && \
docker pull k8s.gcr.io/kube-controller-manager:v1.19.16 && \
docker pull k8s.gcr.io/kube-scheduler:v1.19.0 && \
docker pull k8s.gcr.io/kube-proxy:v1.19.16 && \
docker pull k8s.gcr.io/pause:3.2 && \
docker pull k8s.gcr.io/etcd:3.4.13-0 && \
docker pull k8s.gcr.io/coredns:1.7.0
```

```bash
docker save k8s.gcr.io/kube-apiserver:v1.19.16 -o kube-apiserver_v1.19.16.tar && \
docker save k8s.gcr.io/kube-controller-manager:v1.19.16 -o kube-controller-manager_v1.19.16.tar && \
docker save k8s.gcr.io/kube-scheduler:v1.19.16 -o kube-scheduler_v1.19.16.tar && \
docker save k8s.gcr.io/kube-proxy:v1.19.16 -o kube-proxy_v1.19.16.tar && \
docker save k8s.gcr.io/pause:3.2 -o pause_3.2.tar && \
docker save k8s.gcr.io/etcd:3.4.13-0 -o etcd_3.4.13-0.tar && \
docker save k8s.gcr.io/coredns:1.7.0 -o coredns_1.7.0.tar
```

```bash
docker load -i kube-apiserver_v1.19.16.tar && \
docker load -i kube-controller-manager_v1.19.16.tar && \
docker load -i kube-scheduler_v1.19.16.tar && \
docker load -i kube-proxy_v1.19.16.tar && \
docker load -i pause_3.2.tar && \
docker load -i etcd_3.4.13-0.tar && \
docker load -i coredns_1.7.0.tar
```

```bash
vim ~/kube-cluster/kube-dependencies.yml
```

```bash
- hosts: all
  become: yes
  tasks:
  # - name: install Docker
  #   apt:
  #     name: docker.io
  #     state: present
  #     update_cache: true

  - name: install APT Transport HTTPS
    apt:
      name: apt-transport-https
      state: present

  - name: add Kubernetes apt-key
    apt_key:
      url: https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg
      state: present

  - name: add Kubernetes' APT repository
    apt_repository:
      repo: deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
      state: present
      filename: 'kubernetes'

  - name: install kubelet
    apt:
      name: kubelet=1.19.4-00
      state: present
      update_cache: true

  - name: install kubeadm
    apt:
      name: kubeadm=1.19.4-00
      state: present

- hosts: master
  become: yes
  tasks:
  - name: install kubectl
    apt:
      name: kubectl=1.19.4-00
      state: present
      force: yes
```

```
ansible-playbook -i hosts ~/kube-cluster/kube-dependencies.yml
```
### Step 3: Set up Master Node
download kube-flannel.yml
```
https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
vim ~/kube-cluster/kube-flannel.yml
```

```bash
- hosts: master
  become: yes
  tasks:
  - name: initialize the cluster
    shell: kubeadm init --apiserver-advertise-address=master_ip --pod-network-cidr=10.244.0.0/16 >> cluster_initialized.txt
    args:
      chdir: $HOME
      creates: cluster_initialized.txt

  - name: install Pod network, flannel
    environment:
      KUBECONFIG: /etc/kubernetes/admin.conf
    become: yes
    shell: kubectl apply -f ~/kube-cluster/kube-flannel.yml >> pod_network_setup.txt
    args:
      chdir: $HOME
      creates: pod_network_setup.txt
```

```
ansible-playbook -i hosts ~/kube-cluster/master.yml
export KUBECONFIG=/etc/kubernetes/admin.conf
kubectl get nodes
kubectl get pods -A
```

### Step 4: Setup Worker Nodes
```bash
vim ~/kube-cluster/workers.yml
```

```bash
- hosts: master
  become: yes
  gather_facts: false
  tasks:
  - name: get join command
    environment:
      KUBECONFIG: /etc/kubernetes/admin.conf
    shell: kubeadm token create --print-join-command
    register: join_command_raw

  - name: set join command
    set_fact:
      join_command: "{{ join_command_raw.stdout_lines[0] }}"

- hosts: workers
  become: yes
  tasks:
  - name: join cluster
    shell: "{{ hostvars['master'].join_command }} >> node_joined.txt"
    args:
      chdir: $HOME
      creates: node_joined.txt
```

```bash
ansible-playbook -i hosts ~/kube-cluster/workers.yml
kubectl get nodes -o wide
```