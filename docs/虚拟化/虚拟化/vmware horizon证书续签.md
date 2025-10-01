## 🛠 你实际需要做的操作流程：
### 1️⃣ 生成新证书（你已完成）
```powershell
$cert = New-SelfSignedCertificate `
  -DnsName "xmview03-c-s.kehua.org" `
  -CertStoreLocation "Cert:\LocalMachine\My" `
  -FriendlyName "VMware Horizon Self-Signed Cert" `
  -KeyExportPolicy Exportable `
  -NotAfter (Get-Date).AddYears(10)
```

---

### 2️⃣ 删除旧证书的 `FriendlyName = "vdm"`（或重命名）
```powershell
# 查找旧证书
$old = Get-ChildItem -Path Cert:\LocalMachine\My | Where-Object { $_.FriendlyName -eq "vdm" }

# 修改其名称，防止冲突
$old.FriendlyName = "vdm-old"
```

---

### 3️⃣ 将新证书的 FriendlyName 改成 "vdm"
```powershell
$cert.FriendlyName = "vdm"
```

---

### 4️⃣ 重启 Horizon 服务（或整个服务器）
```powershell
Restart-Service -Name "wsbroker"
Restart-Service -Name "wsnm"
```

或者：

```powershell
Restart-Computer
```

