### 告警信息
```sql
The CPU has been disabled by the guest operating system. Power off or reset the virtual machine.
```

[https://knowledge.broadcom.com/external/article/313529/virtual-machine-rebooted-with-the-follow.html](https://knowledge.broadcom.com/external/article/313529/virtual-machine-rebooted-with-the-follow.html)

## ✅ 官方推荐的排查流程
**该错误需与 Guest OS 厂商协同排查**，以下为官方建议的收集与排除步骤：[Support Portal](https://knowledge.broadcom.com/external/article/313529/virtual-machine-rebooted-with-the-follow.html?utm_source=chatgpt.com)

1. 记录虚拟机名称与故障发生时间。
2. 尽快收集：
    - Guest OS 日志（如 RHEL 的 sosreport），联系操作系统供应商确认所需日志。
    - ESXi 主机日志（hostd.log、vmkernel.log 等）及 vCenter 日志。
3. 如果 VM 在 panic 画面屏幕停滞（如 Windows 蓝屏）：
    - 截图保存；
    - 通过 vSphere 客户端右键 VM “Suspend” —— 生成 `.vmss` 和 `.vmem`；
    - 使用 `vmss2core` 工具转换为 core dump 供进一步分析。
4. 恢复 VM 并重启/reset VM。
5. 如果 Guest OS 厂商确认问题来自 VMware 组件（如 VMware Tools），则联系 Broadcom/VMware 支持处理。



### 临时解决方案
 禁用 soft lockup 和 NMI watchdog 

CSS Misscount 和 Disk Misscount 超时时间从默认 27 秒提升至约 90 秒  

```sql
cat <<EOF | sudo tee -a /etc/sysctl.conf
kernel.softlockup_panic = 0
kernel.nmi_watchdog = 0
EOF

sudo sysctl -p

```

```sql
defaults {
    checker_timeout 30
    max_fds 8192
    no_path_retry queue
    polling_interval 10
    flush_on_last_del yes
}

devices {
    device {
        vendor "*"
        product "*"
        hardware_handler "0"
        path_selector "round-robin 0"
        path_grouping_policy "multibus"
        rr_min_io 100
        rr_weight uniform
        failback immediate
        no_path_retry 60
        fast_io_fail_tmo 90        # 默认是 5 或 10，可改为 90
        dev_loss_tmo 90            # 默认是 30，可改为 90
    }
}
```

```sql
sudo systemctl restart multipathd
```

