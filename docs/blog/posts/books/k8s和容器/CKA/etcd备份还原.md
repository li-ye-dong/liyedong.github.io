



```bash
#!/bin/bash
#export snapshost.db
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/opt/KUIN00601/ca.crt --cert=/opt/KUIN00601/etcd-client.crt --key=/opt/KUIN00601/etcd-client.key \
  snapshot save /var/lib/backup/etcd-snapshot.db

#stop etcd and api
mv /etc/kubernets/manifests /etc/kubernets/manifests.bak
sleep 30
#backup etcd
rm -rf /var/lib/etcd.bak
mv /var/lib/etcd /var/lib/etcd.bak
#restore etcd
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/opt/KUIN00601/ca.crt --cert=/opt/KUIN00601/etcd-client.crt --key=/opt/KUIN00601/etcd-client.key \
  snapshot restore /var/lib/backup/etcd-snapshot.db --data-dir /var/lib/etcd

#start etcd and api
mv /etc/kubernets/manifests.bak /etc/kubernets/manifests
```

