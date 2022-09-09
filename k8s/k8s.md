```bash
export KUBECONFIG=/etc/kubernetes/admin.conf | cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
kubectl get nodes   #pod、service类似
kubectl describe node node1   #pod、service类似
kubectl get svc tomcat-service -o yaml  <-> kubectl create -f tomcat-service.yaml
```