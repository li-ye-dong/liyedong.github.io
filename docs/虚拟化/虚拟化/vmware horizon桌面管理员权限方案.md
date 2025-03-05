### **方法 1：使用组策略 (GPO)**
1. 将domain users的组使用受限制的组策略，加入的本地Administrators组中，较为方便，不需要进入域控添加用户。
2. 采用手工创建受限制组，每次都需要手动加入用户，到安全组中，较为繁琐，但是开放权限较小。

---

### **方法 2：创建 Horizon 桌面模板时预设权限**
1. **准备模板虚拟机**：
    - 在创建 Horizon 桌面模板时，将 `HorizonAdmins` 组（或特定用户）添加到本地 Administrators 组中。

```plain
net localgroup administrators "DOMAIN\HorizonAdmins" /add
```

2. **从模板克隆桌面**：
    - 使用预设权限的模板来克隆桌面，克隆后的每台桌面自动继承模板的配置。

---

### **方法 3：通过 PowerShell 自动化**
如果需要为动态添加的用户快速授予管理员权限，可以使用 PowerShell 脚本自动执行。

1. **示例脚本**： 将以下脚本运行在 Horizon 桌面上，或通过远程方式执行：

```plain
# 设置用户变量
$user = "DOMAIN\Username"  # 替换为实际用户
$group = "Administrators"

# 添加用户到本地管理员组
Add-LocalGroupMember -Group $group -Member $user
```

2. **批量执行**：
    - 结合 Horizon 的桌面池特性，可以通过 PowerCLI 或其他工具自动分配权限。

---

### **方法 3：通过 Horizon 自定义脚本**
在 Horizon 桌面池配置中，启用自定义脚本：

1. **新建桌面时触发脚本**：
    - 在桌面池设置中，使用 `Post-synchronization script`。
2. **脚本内容**：
    - 实现与方法 3 类似的逻辑，动态分配权限。

