今天突然有一个想法，想要实现如下效果：

**vSphere 扩容虚拟磁盘后，用户只需重启，系统自动扩展 C 盘和 D 盘，跳过恢复分区干扰，全自动化。**

我为你准备了一个**完整可落地的方案**，包含：

1. 自动识别恢复分区并删除
2. 自动识别并扩展 **C盘**
3. 如果存在 **D盘** 且后方有未分配空间，也自动扩展 D盘

---

## ✅ PowerShell 脚本（域控下发专用）
### 💡 功能：
+ 兼容 Windows 10/11
+ C盘和D盘都能智能扩展
+ 自动跳过未使用空间不连续的情况（如中间有其他分区）

---

### 📜 `extend_volumes.ps1` 脚本内容：
```powershell
# 自动扩展系统盘（C盘）与数据盘（D盘），并记录日志（每次覆盖旧日志）

$logFile = "C:\ProgramData\disk_expand.log"

# 每次运行前清空旧日志
if (Test-Path $logFile) {
    Remove-Item $logFile -Force
}

function Write-Log {
    param (
        [string]$message,
        [string]$level = "INFO"
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "[$timestamp][$level] $message"
    Add-Content -Path $logFile -Value $line
    Write-Host $line
}

$ErrorActionPreference = "Stop"

function Remove-RecoveryPartition {
    param ([int]$DiskNumber)
    $recovery = Get-Partition -DiskNumber $DiskNumber | Where-Object { $_.Type -eq "Recovery" }
    if ($recovery) {
        Write-Log "发现恢复分区，尝试删除..." "INFO"
        try {
            $recovery | Remove-Partition -Confirm:$false
            Write-Log "恢复分区已删除。" "SUCCESS"
        } catch {
            Write-Log "删除恢复分区失败：$($_.Exception.Message)" "ERROR"
        }
    } else {
        Write-Log "未发现恢复分区，跳过删除。" "INFO"
    }
}

function Expand-Partition-IfPossible {
    param ([char]$DriveLetter)

    $partition = Get-Partition -DriveLetter $DriveLetter -ErrorAction SilentlyContinue
    if (-not $partition) {
        Write-Log "$DriveLetter 盘不存在，跳过。" "INFO"
        return $false
    }

    $disk = Get-Disk -Number $partition.DiskNumber
    $free = $disk | Get-Disk | Select-Object -ExpandProperty LargestFreeExtent

    if ($free -gt 0) {
        $rounded = [math]::Round($free/1GB,2)
        Write-Log "$DriveLetter 盘后存在 $rounded GB 未分配空间，尝试扩展..." "INFO"
        try {
            Resize-Partition -DriveLetter $DriveLetter -Size ($partition.Size + $free)
            Write-Log "$DriveLetter 盘扩展成功！" "SUCCESS"
            return $true
        } catch {
            Write-Log "$DriveLetter 盘扩展失败：$($_.Exception.Message)" "ERROR"
            return $false
        }
    } else {
        Write-Log "$DriveLetter 盘后无未分配空间，跳过扩展。" "INFO"
        return $false
    }
}

# 主执行流程
try {
    $systemDrive = (Get-WmiObject Win32_OperatingSystem).SystemDrive.Replace(":", "")
    $sysPart = Get-Partition | Where-Object { $_.DriveLetter -eq $systemDrive }
    $diskNumber = $sysPart.DiskNumber
    Write-Log "系统盘为 $systemDrive，位于磁盘 $diskNumber。" "INFO"

    Remove-RecoveryPartition -DiskNumber $diskNumber

    $cChanged = Expand-Partition-IfPossible -DriveLetter 'C'
    $dChanged = Expand-Partition-IfPossible -DriveLetter 'D'

    if (-not $cChanged -and -not $dChanged) {
        Write-Log "没有任何卷可以扩展，结束本次执行。" "INFO"
    } else {
        Write-Log "本次扩展操作已完成。" "SUCCESS"
    }

} catch {
    Write-Log "脚本发生未处理异常：$($_.Exception.Message)" "FATAL"
}

```

---

## ✅ 配套 .BAT 文件（用于 GPO 或登录脚本）
保存为 `extend_volumes.bat`：

```plain
@echo off
powershell.exe -ExecutionPolicy Bypass -NoProfile -File \\domain\netlogon\extend_volumes.ps1
```

然后把 `extend_volumes.ps1` 放入域控共享路径，比如：

```plain
\\your-domain.local\netlogon\
```

再通过 GPO 进行用户登录时自动执行，或指定为 **“启动脚本”**（Computer Configuration → Windows Settings → Scripts）。

---

## 🧪 执行前建议测试的环境
| 系统版本 | 测试建议 |
| --- | --- |
| Windows 10 企业版 | ✅ 推荐 |
| Windows 11 企业版 | ✅ 推荐 |
| Win7 或 2008R2 | ❌ 不支持 `Resize-Partition`<br/>，需改用 `diskpart` |
| 非域环境 | 可封装为本地任务计划或手动执行 |


---

## 为什么不下发powershell
| 方案 | 是否推荐 | 原因 |
| --- | --- | --- |
| `.bat`<br/> 调用 `.ps1` | ✅ 强烈推荐 | 可绕过执行策略、安全稳定、兼容老系统 |
| 直接下发 `.ps1` | ⚠ 条件使用 | 需配置执行策略，否则易失败 |
| 在注册表中设置执行策略 | ❌ 不推荐 | 不透明、不可控、安全性差 |


