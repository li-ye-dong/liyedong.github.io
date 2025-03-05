<font style="color:rgb(89, 97, 114);">RVTools 当前最新</font>[版本](https://www.robware.net/versionInfo)<font style="color:rgb(89, 97, 114);">为 </font>[RVTools 4.6.1](https://resources.robware.net/resources/prod/RVTools4.6.1.msi)<font style="color:rgb(89, 97, 114);">，支持 vSphere 5.x、6.x、7.x、8.x 版本，Windows 安装环境需要 </font>[.NET 4.6.2](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net462)<font style="color:rgb(89, 97, 114);"> 支持。RVTools 默认安装在“C:\Program Files (x86)\Dell\RVTools”文件夹，如果是自定义安装那找到自行设置的文件夹即可，打开文件资源管理器导航到该文件夹后可以看到如下图内容。</font>

<font style="color:rgb(89, 97, 114);">我后面就不再使用文件资源管理器进行查看，全部通过 PowerShell 查看，你可以打开 PowerShell 使用下面命令进入到 RVTools 的安装文件夹。</font>

```powershell
PS C:\Users\Public\Desktop> cd "C:\Program Files (x86)\Dell\RVTools"
PS C:\Program Files (x86)\Dell\RVTools> ls


    目录: C:\Program Files (x86)\Dell\RVTools


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2024/5/14      9:48        1184256 ClosedXML.dll
-a----         2024/5/14      9:48        5124488 DocumentFormat.OpenXml.dll
-a----         2024/5/14      9:48         123839 EULA.rtf
-a----         2024/5/14      9:48          30208 ExcelNumberFormat.dll
-a----         2024/5/14      9:48          26624 FastMember.dll
-a----         2024/5/14      9:48          26624 FastMember.Signed.dll
-a----         2024/5/14      9:48            707 log4net.config
-a----         2024/5/14      9:48         270336 log4net.dll
-a----         2024/5/14      9:48         386488 Microsoft.ApplicationInsights.dll
-a----         2024/5/14      9:48         701992 Newtonsoft.Json.dll
-a----         2024/5/14      9:48         758520 RVTools.exe
-a----         2024/5/14      9:48           7894 RVTools.exe.config
-a----         2024/5/14      9:48        3120364 RVTools.pdf
-a----         2024/5/14      9:48           4286 rvtools32x32.ico
-a----         2024/5/14      9:48          13200 RVToolsBatchMultipleVCs.ps1
-a----         2024/5/14      9:48          16950 RVToolsCreateLocalUser.ps1
-a----         2024/5/14      9:48          16959 RVToolsFindBadVM.ps1
-a----         2024/5/14      9:48          26360 RVToolsMergeExcelFiles.exe
-a----         2024/5/14      9:48            786 RVToolsMergeExcelFiles.exe.config
-a----         2024/5/14      9:48          16819 RVToolsPasswordEncryption.ps1
-a----         2024/5/14      9:48          24312 RVToolsSendMail.exe
-a----         2024/5/14      9:48            163 RVToolsSendMail.exe.config
-a----         2024/4/22     18:55          53760 STSService.dll
-a----         2024/5/14      9:48          20856 System.Buffers.dll
-a----         2024/5/14      9:48          98184 System.Diagnostics.DiagnosticSource.dll
-a----         2024/5/14      9:48          22784 System.IO.FileSystem.Primitives.dll
-a----         2024/5/14      9:48         141184 System.Memory.dll
-a----         2024/5/14      9:48          85184 System.Net.Http.dll
-a----         2024/5/14      9:48         115856 System.Numerics.Vectors.dll
-a----         2024/5/14      9:48          16768 System.Runtime.CompilerServices.Unsafe.dll
-a----         2024/5/14      9:48       14236160 Vim25Service.dll
-a----         2024/5/14      9:48          24576 VMware.Binding.WsTrust.dll
```

<font style="color:rgb(89, 97, 114);">在 RVTools 的安装目录里，提供了如下图所示的 PowerShell 示例脚本文件，而此次重点要使用到的是 </font>**<font style="color:rgb(89, 97, 114);">RVToolsBatchMultipleVCs.ps1</font>**<font style="color:rgb(89, 97, 114);"> 脚本，通过这个脚本文件可以使用 PowerShell 自动导出 vSphere 环境信息，再配合 Windows 的任务计划程序实现自动化任务。当然，配合这个脚本使用的还有另外三个脚本文件，主要会用到 RVToolsPasswordEncryption.ps1 脚本，使用这个脚本对密码进行加密，另外两个脚本可选使用，RVToolsCreateLocalUser.ps1 脚本用于创建专用于执行自动化任务的本地用户，RVToolsFindBadVM.ps1 脚本用于查找未被 RVTools 导出到清单的虚拟机（通常是具有大量磁盘文件需要被整合的虚拟机）。</font>

```powershell
PS C:\Program Files (x86)\Dell\RVTools> ls *.ps1


    目录: C:\Program Files (x86)\Dell\RVTools


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2024/5/14      9:48          13200 RVToolsBatchMultipleVCs.ps1
-a----         2024/5/14      9:48          16950 RVToolsCreateLocalUser.ps1
-a----         2024/5/14      9:48          16959 RVToolsFindBadVM.ps1
-a----         2024/5/14      9:48          16819 RVToolsPasswordEncryption.ps1
```

<font style="color:rgb(89, 97, 114);">其实，RVToolsBatchMultipleVCs.ps1 脚本文件中真正使用到的是如下图所示的可执行程序。默认情况下，安装完 RVTools 使用到的 GUI 客户端就是 RVTools.exe 执行程序，虽然我们都是用图形化界面，不过 RVTools.exe 执行程序也可以通过命令行运行，也就是 RVToolsBatchMultipleVCs.ps1 脚本所应用的方法。RVToolsMergeExcelFiles.exe 和 RVToolsSendMail.exe 执行程序是另外两个有用的工具，第一个可以将导出的多个 EXCEL 表格文件合成一个表格文件，第二个可以将这个导出的表格文件通过配置 SMTP 服务器后以邮件的方式发送给管理员。</font>

```powershell
PS C:\Program Files (x86)\Dell\RVTools> ls *.exe


    目录: C:\Program Files (x86)\Dell\RVTools


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2024/5/14      9:48         758520 RVTools.exe
-a----         2024/5/14      9:48          26360 RVToolsMergeExcelFiles.exe
-a----         2024/5/14      9:48          24312 RVToolsSendMail.exe
```

<font style="color:rgb(89, 97, 114);">RVToolsMergeExcelFiles.exe 和 RVToolsSendMail.exe 工具可选，这在 RVToolsBatchMultipleVCs.ps1 脚本中可以配置，不过重点需要使用 RVTools.exe 执行程序，下面详细介绍一下这个程序的命令行选项。</font>

<font style="color:rgb(89, 97, 114);">RVTools.exe 命令行可提供使用以下选项：</font>

+ <font style="color:rgb(89, 97, 114);">-s    //需要连接的 ESXi 主机或 vCenter（域名或IP地址）。</font>
+ <font style="color:rgb(89, 97, 114);">-passthroughAuth    //使用直通身份验证连接到 ESXi 主机或 vCenter（使用当前的 Windows 登录凭据）。</font>
+ <font style="color:rgb(89, 97, 114);">-u    //用于连接到 ESXi 主机或 vCenter 的用户名。</font>
+ <font style="color:rgb(89, 97, 114);">-p    //用于连接到 ESXi 主机或 vCenter 的密码。</font>
+ <font style="color:rgb(89, 97, 114);">-c    //使用的导出选项。</font>
+ <font style="color:rgb(89, 97, 114);">-d    //设置导出的目录。</font>
+ <font style="color:rgb(89, 97, 114);">-f    //设置导出的 XLSX 或 CSV 格式的文件名。如果不设置文件名，RVTools 将创建一个带有日期时间戳的文件名。</font>

<font style="color:rgb(89, 97, 114);">下列选项适用于选择 </font>`-passthroughAuth`<font style="color:rgb(89, 97, 114);"> </font><font style="color:rgb(89, 97, 114);">时使用：</font>

+ <font style="color:rgb(89, 97, 114);">-ExcludeCustomAnnotations    //不导出自定义注释字段。</font>
+ <font style="color:rgb(89, 97, 114);">-ExcludeTags    //不导出标签字段。</font>
+ <font style="color:rgb(89, 97, 114);">-DBColumnNames    //使用 RVTools intenal 列名称。如果将导出上传到 DBMS，则很有用。</font>
+ <font style="color:rgb(89, 97, 114);">-GetFriendlyNames    //如果使用 vSAN 并希望导出显示友好的 vSAN 名称而不是 UUID。</font>
+ <font style="color:rgb(89, 97, 114);">-GetFileInfo    //将填充 vFileInfo 选项卡页。注意：这可能需要很长时间。</font>

<font style="color:rgb(89, 97, 114);">关于</font><font style="color:rgb(89, 97, 114);"> </font>`-c`<font style="color:rgb(89, 97, 114);"> </font><font style="color:rgb(89, 97, 114);">导出选项，支持以下导出的信息：</font>

+ <font style="color:rgb(89, 97, 114);">-c ExportAll2xlsx    //将RVTools中所有选项卡导出为 xlsx 格式。</font>
+ <font style="color:rgb(89, 97, 114);">-c ExportAll2csv    //将RVTools中所有选项卡导出为 csv 格式。</font>
+ <font style="color:rgb(89, 97, 114);">-c Export<tab>2xlsx    //将RVTools中特定<选项卡>导出为 xlsx 格式。</font>
+ <font style="color:rgb(89, 97, 114);">-c Export<tab>2csv    //将RVTools中特定<选项卡>导出为 csv 格式。</font>

<font style="color:rgb(89, 97, 114);">这里<tab>选项卡支持以下</font>[<font style="color:rgb(89, 97, 114);">值</font>](https://www.robware.net/readMore)<font style="color:rgb(89, 97, 114);">：</font>

    - <font style="color:rgb(89, 97, 114);">vInfo</font>
    - <font style="color:rgb(89, 97, 114);">vCpu</font>
    - <font style="color:rgb(89, 97, 114);">vMemory</font>
    - <font style="color:rgb(89, 97, 114);">vDisk</font>
    - <font style="color:rgb(89, 97, 114);">vPartition</font>
    - <font style="color:rgb(89, 97, 114);">vNetwork</font>
    - <font style="color:rgb(89, 97, 114);">vCD</font>
    - <font style="color:rgb(89, 97, 114);">vUSB</font>
    - <font style="color:rgb(89, 97, 114);">vSnapshot</font>
    - <font style="color:rgb(89, 97, 114);">vTools</font>
    - <font style="color:rgb(89, 97, 114);">vSource</font>
    - <font style="color:rgb(89, 97, 114);">vRP</font>
    - <font style="color:rgb(89, 97, 114);">vCluster</font>
    - <font style="color:rgb(89, 97, 114);">vHost</font>
    - <font style="color:rgb(89, 97, 114);">vHBA</font>
    - <font style="color:rgb(89, 97, 114);">vNic</font>
    - <font style="color:rgb(89, 97, 114);">vSwitch</font>
    - <font style="color:rgb(89, 97, 114);">vPort</font>
    - <font style="color:rgb(89, 97, 114);">dvSwitch</font>
    - <font style="color:rgb(89, 97, 114);">dvPort</font>
    - <font style="color:rgb(89, 97, 114);">vSC+VMK</font>
    - <font style="color:rgb(89, 97, 114);">vDatastore</font>
    - <font style="color:rgb(89, 97, 114);">vMultiPath</font>
    - <font style="color:rgb(89, 97, 114);">vLicense</font>
    - <font style="color:rgb(89, 97, 114);">vFileInfo</font>
    - <font style="color:rgb(89, 97, 114);">vHealth</font>

<font style="color:rgb(89, 97, 114);">在了解了 RVTools 相关命令行选项及含义后，下面演示一下使用 RVTools 命令行来完成 GUI 完成的相关工作。</font>

<font style="color:rgb(89, 97, 114);">运行 RVTools 命令使用 pass-through 的认证方式来连接 ESXi 主机或 vCenter，pass-through 认证方式就是使用当前 Windows 登录用户及凭证，如果 vSphere 环境已经加入了 AD 域环境，同时当前运行 RVTools 的Windows 终端用户是域用户，则可以使用这种方式，否则大部分情况下是使用下面用户名+密码的方法连接到 ESXi 主机或 vCenter。</font>

```powershell
.\RVTools.exe –passthroughAuth –s vcsa8-02.mulab.local


```

获取加密密码

```powershell
.\RVToolsPasswordEncryption.ps1
```

运行

```powershell
.\RVTools.exe -s vcenter地址 -u 账号 -p 加密后的密码
```

<font style="color:rgb(89, 97, 114);">不过因为加密后的密码太长了，可以给加密后的密码创建一个变量，这样直接带入变量要方便一些。</font>

```powershell
$password = ""
```

<font style="color:rgb(89, 97, 114);">运行 RVTools 命令使用 ExportAll2xlsx 导出选项将所有选项卡以 XLSX 格式导出到指定目录，使用 </font>`<font style="color:rgb(89, 97, 114);">-f</font>`<font style="color:rgb(89, 97, 114);"> 选项指定导出文件的名称，不指定则导出带有时间戳的文件名。</font>

```powershell
.\RVTools.exe -s vcenter地址 -u 账号 -p $password -c ExportAll2xlsx -d C:\RVTools\Temp\ -f all
```

<font style="color:rgb(89, 97, 114);">运行 RVTools 命令使用 ExportAll2csv 导出选项将所有选项卡以 CSV 格式导出到指定目录。</font>

```powershell
.\RVTools.exe -s vcsa8-02.mulab.local -u vsphere.local\administrator -p $password -c ExportAll2csv -d C:\RVTools\Temp\
```

<font style="color:rgb(89, 97, 114);">运行 RVTools 命令使用 ExportvInfo2xlsx 导出选项将 vInfo 选项卡以 XLSX 格式导出到指定目录，使用 </font>`<font style="color:rgb(89, 97, 114);">-f</font>`<font style="color:rgb(89, 97, 114);"> 选项指定导出文件的名称，不指定则导出带有时间戳的文件名。</font>

```powershell
.\RVTools.exe -s vcsa8-02.mulab.local -u vsphere.local\administrator -p $password -c ExportvInfo2xlsx -d C:\RVTools\Temp\ -f vInfo
```

<font style="color:rgb(89, 97, 114);">运行 RVTools 命令使用 ExportvInfo2csv 导出选项将 vInfo 选项卡以 CSV 格式导出到指定目录，使用 </font>`<font style="color:rgb(89, 97, 114);">-f</font>`<font style="color:rgb(89, 97, 114);"> 选项指定导出文件的名称，不指定则导出带有时间戳的文件名。</font>

```powershell
.\RVTools.exe -s vcsa8-02.mulab.local -u vsphere.local\administrator -p $password -c ExportvInfo2csv -d C:\RVTools\Temp\ -f vInfo
```

<font style="color:rgb(89, 97, 114);">了解了 RVTools 的命令行使用方式，现在让我们回到 PowerShell 脚本 RVToolsBatchMultipleVCs.ps1 中来，看看如何通过脚本创建自动化导出任务。先来看一下 RVToolsBatchMultipleVCs.ps1 脚本中的内容。</font>

```powershell
# =============================================================================================================
# Script:    RVToolsBatchMultipleVCs.ps1
# Version:   1.4
# Date:      November, 2023
# By:        Dell Technologies
# =============================================================================================================

<#
.SYNOPSIS
With this example script you can start the the RVTools export all to xlsx function for multiple vCenter servers.
The output xlsx files will be merged to one xlsx file which will be mailed
	
.DESCRIPTION
With this example script you can start the the RVTools export all to xlsx function for multiple vCenter servers.
The output xlsx files will be merged to one xlsx file which will be mailed


.EXAMPLE
 .\RVToolsBatchMultipleVCs.ps1

#>

# Save current directory
$SaveCurrentDir = (get-location).Path

# Set RVTools path
[string] $RVToolsPath = "C:\Program Files (x86)\Dell\RVTools"

# cd to RVTools directory
set-location $RVToolsPath


# -----------------------------------------------------
# Set parameters for vCenter 1 and start RVTools export
# -----------------------------------------------------
[string] $VCServer = "192.168.2.220"                                                    # my test vCenter server
[string] $User = "vsphere.local\rob"                                                    

# use -passthroughAuth or an encrypted password. You can encrypt your password with the provided PowerShell script RVToolsPasswordEncryption.ps1
[string] $EncryptedPassword = "_RVToolsV3PWD01000000d08c9ddf0115d1118c7a00c04fc297eb01000000325cf1e07062a848a422825c7ccd19f100000000020000000000106600000001000020000000397128ff49bbd394092555bac4ea58b61232edf65d9c19f61f94516857e87e3c000000000e8000000002000020000000d068a8d3251e73170b8fd63e329aecb048885da168bc6a24c363e18f1a0a446c20000000efca9029a70b20b9d2d1042d3f34a1c370b965c085f2933a3fa453a0dd5392324000000084b7ad15d00299271c13ce7f44ad45fb6a6d8ded586f22a27" 

[string] $XlsxDir1 = "C:\RVTools"
[string] $XlsxFile1 = "vCenter1.xlsx"

# Start cli of RVTools
Write-Host "Start export for vCenter $VCServer" -ForegroundColor DarkYellow
$Arguments = "-u $User -p $EncryptedPassword -s $VCServer -c ExportAll2xlsx -d $XlsxDir1 -f $XlsxFile1"

Write-Host $Arguments

$Process = Start-Process -FilePath ".\RVTools.exe" -ArgumentList $Arguments -NoNewWindow -Wait -PassThru

if($Process.ExitCode -eq -1)
{
    Write-Host "Error: Export failed! RVTools returned exitcode -1, probably a connection error! Script is stopped" -ForegroundColor Red
    exit 1
}


# -----------------------------------------------------
# Set parameters for vCenter 2 and start RVTools export
# -----------------------------------------------------
[string] $VCServer = "192.168.2.220"
[string] $User = "vsphere.local\rob"

# use -passthroughAuth or an encrypted password. You can encrypt your password with the provided PowerShell script RVToolsPasswordEncryption.ps1
[string] $EncryptedPassword = "_RVToolsV3PWD01000000d08c9ddf0115d1118c7a00c04fc297eb01000000325cf1e07062a848a422825c7ccd19f100000000020000000000106600000001000020000000397128ff49bbd394092555bac4ea58b61232edf65d9c19f61f94516857e87e3c000000000e8000000002000020000000d068a8d3251e73170b8fd63e329aecb048885da168bc6a24c363e18f1a0a446c20000000efca9029a70b20b9d2d1042d3f34a1c370b965c085f2933a3fa453a0dd5392324000000084b7ad15d00299271c13ce7f44ad45fb6a6d8ded586f22a27" 

[string] $XlsxDir2 = "C:\RVTools"
[string] $XlsxFile2 = "vCenter2.xlsx"

# Start cli of RVTools
Write-Host "Start export for vCenter $VCServer" -ForegroundColor DarkYellow
$Arguments = "-u $User -p $EncryptedPassword -s $VCServer -c ExportAll2xlsx -d $XlsxDir2 -f $XlsxFile2"

Write-Host $Arguments

$Process = Start-Process -FilePath ".\RVTools.exe" -ArgumentList $Arguments -NoNewWindow -Wait -PassThru

if($Process.ExitCode -eq -1)
{
    Write-Host "Error: Export failed! RVTools returned exitcode -1, probably a connection error! Script is stopped" -ForegroundColor Red
    exit 1
}


# -----------------------------------------------------
# Set parameters for vCenter 3 and start RVTools export
# -----------------------------------------------------
[string] $VCServer = "192.168.2.220"
[string] $User = "vsphere.local\rob"

# use -passthroughAuth or an encrypted password. You can encrypt your password with the provided PowerShell script RVToolsPasswordEncryption.ps1
[string] $EncryptedPassword = "_RVToolsV3PWD01000000d08c9ddf0115d1118c7a00c04fc297eb01000000325cf1e07062a848a422825c7ccd19f100000000020000000000106600000001000020000000397128ff49bbd394092555bac4ea58b61232edf65d9c19f61f94516857e87e3c000000000e8000000002000020000000d068a8d3251e73170b8fd63e329aecb048885da168bc6a24c363e18f1a0a446c20000000efca9029a70b20b9d2d1042d3f34a1c370b965c085f2933a3fa453a0dd5392324000000084b7ad15d00299271c13ce7f44ad45fb6a6d8ded586f22a27" 

[string] $XlsxDir3 = "C:\RVTools"
[string] $XlsxFile3 = "vCenter3.xlsx"

# Start cli of RVTools
Write-Host "Start export for vCenter $VCServer" -ForegroundColor DarkYellow
$Arguments = "-u $User -p $EncryptedPassword -s $VCServer -c ExportAll2xlsx -d $XlsxDir3 -f $XlsxFile3"

Write-Host $Arguments

$Process = Start-Process -FilePath ".\RVTools.exe" -ArgumentList $Arguments -NoNewWindow -Wait -PassThru

if($Process.ExitCode -eq -1)
{
    Write-Host "Error: Export failed! RVTools returned exitcode -1, probably a connection error! Script is stopped" -ForegroundColor Red
    exit 1
}


# -----------------------------------------------
# Merge xlsx files vCenter1 + vCenter2 + vCenter3
# -----------------------------------------------
$OutputFile = "C:\RVTools\vCenter123.xlsx"
& .\RVToolsMergeExcelFiles.exe -input "$XlsxDir1\$XlsxFile1;$XlsxDir2\$XlsxFile2;$XlsxDir3\$XlsxFile3" -output $OutputFile -overwrite -verbose


# ---------------------
# Mail output xlsx file
# ---------------------
[string] $SMTPserver = "your smtp server"
[string] $SMTPport = "25"
[string] $Mailto = "your email send to address"
[string] $MailFrom = "Your email send from address"
[string] $MailSubject = "`"RVTools export all for vCenter 1 and 2`""

Write-Host "Send output file by mail" -ForegroundColor DarkYellow
$Arguments = "/SMTPserver $SMTPserver /smtpport $SMTPport /mailto $Mailto /mailfrom $Mailfrom /mailsubject $Mailsubject /attachment  $OutputFile"
Write-Host $Arguments
#Start-Process -FilePath ".\RVToolsSendmail.exe" -ArgumentList $Arguments -NoNewWindow -Wait


# Back to starting dir
Set-Location $SaveCurrentDir
```

<font style="color:rgb(89, 97, 114);">我们来详细看一下 RVToolsBatchMultipleVCs.ps1 脚本的组成部分，分为几个板块，下面一个一个来说明这几个板块的作用。下面脚本开头中的是介绍，这个脚本文件可以执行多个 vCenter 的导出任务。</font>

```powershell
# =============================================================================================================
# Script:    RVToolsBatchMultipleVCs.ps1
# Version:   1.4
# Date:      November, 2023
# By:        Dell Technologies
# =============================================================================================================

<#
.SYNOPSIS
With this example script you can start the the RVTools export all to xlsx function for multiple vCenter servers.
The output xlsx files will be merged to one xlsx file which will be mailed
	
.DESCRIPTION
With this example script you can start the the RVTools export all to xlsx function for multiple vCenter servers.
The output xlsx files will be merged to one xlsx file which will be mailed


.EXAMPLE
 .\RVToolsBatchMultipleVCs.ps1

#>
```

<font style="color:rgb(89, 97, 114);">下面内容表示设置环境中 RVTools 的安装路径，如果自定义安装在其他目录，则需要在“$RVToolsPath” 后面改成自行设置的目录。</font>

```powershell
# Save current directory
$SaveCurrentDir = (get-location).Path

# Set RVTools path
[string] $RVToolsPath = "C:\Program Files (x86)\Dell\RVTools"

# cd to RVTools directory
set-location $RVToolsPath
```

<font style="color:rgb(89, 97, 114);">下面内容表示 RVTools 真实执行导出 vCenter 环境信息的脚本命令，因为这是一个批量导出多个 vCenter 的脚本，所以可以看到有三个 vCenter 相同的命令列表信息，因为都是一样的，所以我只说其中一个，如果环境中只有一个 vCenter ，则只需要把脚本中的另外两个删掉即可。</font>

+ <font style="color:rgb(89, 97, 114);">“$VCServer”后面表示定义自己环境中的 ESXi 主机或 vCenter 的地址（域名或IP地址）。</font>
+ <font style="color:rgb(89, 97, 114);">“$User” 后面表示定义自己环境中的 ESXi 主机或 vCenter 的用户名。</font>
+ <font style="color:rgb(89, 97, 114);">“$EncryptedPassword”后面表示定义自己环境中的 ESXi 主机或 vCenter 的密码。注意，需要提前使用 RVToolsPasswordEncryption.ps1 脚本将 ESXi 主机或 vCenter 的登录密码生成加密密码，如果使用了passthrough 认证连接方式，则也需要加密 Windows 登录凭证，参考前面。</font>
+ <font style="color:rgb(89, 97, 114);">“$XlsxDir1”后面表示定义自己环境中的导出文件的文件夹。</font>
+ <font style="color:rgb(89, 97, 114);">“$XlsxFile1”后面表示定义导出的文件的名称。</font>
+ <font style="color:rgb(89, 97, 114);">“$Arguments”后面表示定义执行导出的命令。默认</font><font style="color:rgb(89, 97, 114);"> </font>`-c `<font style="color:rgb(89, 97, 114);"> </font><font style="color:rgb(89, 97, 114);">导出选项为导出所有选项卡为 XLSX 格式，可自行设置导出选项，若不使用</font><font style="color:rgb(89, 97, 114);"> </font>`-f`<font style="color:rgb(89, 97, 114);"> </font><font style="color:rgb(89, 97, 114);">选项，则导出带有时间戳的文件名，参考前面。</font>

```powershell
# -----------------------------------------------------
# Set parameters for vCenter 1 and start RVTools export
# -----------------------------------------------------
[string] $VCServer = "192.168.2.220"                                                    # my test vCenter server
[string] $User = "vsphere.local\rob"                                                    

# use -passthroughAuth or an encrypted password. You can encrypt your password with the provided PowerShell script RVToolsPasswordEncryption.ps1
[string] $EncryptedPassword = "_RVToolsV3PWD01000000d08c9ddf0115d1118c7a00c04fc297eb01000000325cf1e07062a848a422825c7ccd19f100000000020000000000106600000001000020000000397128ff49bbd394092555bac4ea58b61232edf65d9c19f61f94516857e87e3c000000000e8000000002000020000000d068a8d3251e73170b8fd63e329aecb048885da168bc6a24c363e18f1a0a446c20000000efca9029a70b20b9d2d1042d3f34a1c370b965c085f2933a3fa453a0dd5392324000000084b7ad15d00299271c13ce7f44ad45fb6a6d8ded586f22a27" 

[string] $XlsxDir1 = "C:\RVTools"
[string] $XlsxFile1 = "vCenter1.xlsx"

# Start cli of RVTools
Write-Host "Start export for vCenter $VCServer" -ForegroundColor DarkYellow
$Arguments = "-u $User -p $EncryptedPassword -s $VCServer -c ExportAll2xlsx -d $XlsxDir1 -f $XlsxFile1"

Write-Host $Arguments

$Process = Start-Process -FilePath ".\RVTools.exe" -ArgumentList $Arguments -NoNewWindow -Wait -PassThru

if($Process.ExitCode -eq -1)
{
    Write-Host "Error: Export failed! RVTools returned exitcode -1, probably a connection error! Script is stopped" -ForegroundColor Red
    exit 1
}


# -----------------------------------------------------
# Set parameters for vCenter 2 and start RVTools export
# -----------------------------------------------------
[string] $VCServer = "192.168.2.220"
[string] $User = "vsphere.local\rob"

# use -passthroughAuth or an encrypted password. You can encrypt your password with the provided PowerShell script RVToolsPasswordEncryption.ps1
[string] $EncryptedPassword = "_RVToolsV3PWD01000000d08c9ddf0115d1118c7a00c04fc297eb01000000325cf1e07062a848a422825c7ccd19f100000000020000000000106600000001000020000000397128ff49bbd394092555bac4ea58b61232edf65d9c19f61f94516857e87e3c000000000e8000000002000020000000d068a8d3251e73170b8fd63e329aecb048885da168bc6a24c363e18f1a0a446c20000000efca9029a70b20b9d2d1042d3f34a1c370b965c085f2933a3fa453a0dd5392324000000084b7ad15d00299271c13ce7f44ad45fb6a6d8ded586f22a27" 

[string] $XlsxDir2 = "C:\RVTools"
[string] $XlsxFile2 = "vCenter2.xlsx"

# Start cli of RVTools
Write-Host "Start export for vCenter $VCServer" -ForegroundColor DarkYellow
$Arguments = "-u $User -p $EncryptedPassword -s $VCServer -c ExportAll2xlsx -d $XlsxDir2 -f $XlsxFile2"

Write-Host $Arguments

$Process = Start-Process -FilePath ".\RVTools.exe" -ArgumentList $Arguments -NoNewWindow -Wait -PassThru

if($Process.ExitCode -eq -1)
{
    Write-Host "Error: Export failed! RVTools returned exitcode -1, probably a connection error! Script is stopped" -ForegroundColor Red
    exit 1
}


# -----------------------------------------------------
# Set parameters for vCenter 3 and start RVTools export
# -----------------------------------------------------
[string] $VCServer = "192.168.2.220"
[string] $User = "vsphere.local\rob"

# use -passthroughAuth or an encrypted password. You can encrypt your password with the provided PowerShell script RVToolsPasswordEncryption.ps1
[string] $EncryptedPassword = "_RVToolsV3PWD01000000d08c9ddf0115d1118c7a00c04fc297eb01000000325cf1e07062a848a422825c7ccd19f100000000020000000000106600000001000020000000397128ff49bbd394092555bac4ea58b61232edf65d9c19f61f94516857e87e3c000000000e8000000002000020000000d068a8d3251e73170b8fd63e329aecb048885da168bc6a24c363e18f1a0a446c20000000efca9029a70b20b9d2d1042d3f34a1c370b965c085f2933a3fa453a0dd5392324000000084b7ad15d00299271c13ce7f44ad45fb6a6d8ded586f22a27" 

[string] $XlsxDir3 = "C:\RVTools"
[string] $XlsxFile3 = "vCenter3.xlsx"

# Start cli of RVTools
Write-Host "Start export for vCenter $VCServer" -ForegroundColor DarkYellow
$Arguments = "-u $User -p $EncryptedPassword -s $VCServer -c ExportAll2xlsx -d $XlsxDir3 -f $XlsxFile3"

Write-Host $Arguments

$Process = Start-Process -FilePath ".\RVTools.exe" -ArgumentList $Arguments -NoNewWindow -Wait -PassThru

if($Process.ExitCode -eq -1)
{
    Write-Host "Error: Export failed! RVTools returned exitcode -1, probably a connection error! Script is stopped" -ForegroundColor Red
    exit 1
}
```

<font style="color:rgb(89, 97, 114);">下面内容表示将上面导出的多个 vCenter 的 Excel 文件合并成一个表格文件并输出到指定目录，这里就使用了 RVTools 安装目录中的 RVToolsMergeExcelFiles.exe 执行程序，如果环境中具有多个 vCenter 可以使用这个功能，如果没有或不想使用这个功能，那可以把这块内容删掉即可。</font>

```powershell
# -----------------------------------------------
# Merge xlsx files vCenter1 + vCenter2 + vCenter3
# -----------------------------------------------
$OutputFile = "C:\RVTools\vCenter123.xlsx"
& .\RVToolsMergeExcelFiles.exe -input "$XlsxDir1\$XlsxFile1;$XlsxDir2\$XlsxFile2;$XlsxDir3\$XlsxFile3" -output $OutputFile -overwrite -verbose
```

<font style="color:rgb(89, 97, 114);">下面内容表示将上面合并输出的 Excel 文件通过邮件发送给管理员，这里就使用了 RVTools 安装目录中的 RVToolsSendmail.exe 执行程序，默认情况下在执行命令的最后一行被注释掉了，如果需要用到这个功能，可以配置相关信息并将最后一行的注释“#”删除掉，如果不用到这个功能可以不管它或者将这块内容删掉。</font>

```powershell
# ---------------------
# Mail output xlsx file
# ---------------------
[string] $SMTPserver = "your smtp server"
[string] $SMTPport = "25"
[string] $Mailto = "your email send to address"
[string] $MailFrom = "Your email send from address"
[string] $MailSubject = "`"RVTools export all for vCenter 1 and 2`""

Write-Host "Send output file by mail" -ForegroundColor DarkYellow
$Arguments = "/SMTPserver $SMTPserver /smtpport $SMTPport /mailto $Mailto /mailfrom $Mailfrom /mailsubject $Mailsubject /attachment  $OutputFile"
Write-Host $Arguments
#Start-Process -FilePath ".\RVToolsSendmail.exe" -ArgumentList $Arguments -NoNewWindow -Wait
```

<font style="color:rgb(89, 97, 114);">最后，返回到启动该脚本的目录。</font>

```powershell
# Back to starting dir
Set-Location $SaveCurrentDir
```

<font style="color:rgb(89, 97, 114);">经过上面对 RVToolsBatchMultipleVCs.ps1 脚本内容的了解，结合自身环境中的情况，可以修改脚本中的内容调整为自己使用的脚本。比如，我当前环境中只想对一个 vCenter 执行导出任务，我调整的脚本如下。</font>

```powershell
# =============================================================================================================
# Script:    RVToolsBatchVC.ps1
# Version:   1.0
# Date:      June, 2024
# By:        JUNIOR MU
# =============================================================================================================


# Save current directory
$SaveCurrentDir = (get-location).Path

# Set RVTools path
[string] $RVToolsPath = "C:\Program Files (x86)\Dell\RVTools"

# cd to RVTools directory
set-location $RVToolsPath


# -----------------------------------------------------
# Set parameters for vCenter 1 and start RVTools export
# -----------------------------------------------------
[string] $VCServer = "vcsa8-02.mulab.local"
[string] $User = "vsphere.local\administrator"

# use -passthroughAuth or an encrypted password. You can encrypt your password with the provided PowerShell script RVToolsPasswordEncryption.ps1
[string] $EncryptedPassword = "_RVToolsV3PWD01000000d08c9ddf0115d1118c7a00c04fc297eb010000001af35e7a80eab64998aeed360314277d00000000020000000000106600000001000020000000c6eda441a4fb0787f966d9990f8ce505de268890c1df387421922247dd951382000000000e80000000020000200000005d1195f9f473904b4433882ff823b62de740fb2c0f10352dd6dc1e3ffe7e6a0b3000000097c976cd9792dcc693f022efb4d32187b1a5705676255adc402dc87233a448dab076e41e69f4d1ff27de235d3226343b4000000061c72a72a652d0df185f3767520c01e0faaadbbe9cc307651deee3288dcee3ea7b7198d8d42e145d1a521d4e2cbbe67bb8a45db4756a2f1fa5d4ebc4640829e7" 

[string] $XlsxDir1 = "C:\RVTools\Task"
[string] $XlsxFile1 = "vCenter.xlsx"

# Start cli of RVTools
Write-Host "Start export for vCenter $VCServer" -ForegroundColor DarkYellow
$Arguments = "-u $User -p $EncryptedPassword -s $VCServer -c ExportAll2xlsx -d $XlsxDir1 -f $XlsxFile1"

Write-Host $Arguments

$Process = Start-Process -FilePath ".\RVTools.exe" -ArgumentList $Arguments -NoNewWindow -Wait -PassThru

if($Process.ExitCode -eq -1)
{
    Write-Host "Error: Export failed! RVTools returned exitcode -1, probably a connection error! Script is stopped" -ForegroundColor Red
    exit 1
}


# Back to starting dir
Set-Location $SaveCurrentDir
```

<font style="color:rgb(89, 97, 114);">现在你可以使用这个脚本在 PowerShell 中执行，确定是否能正常导出。如果能正常导出，那可以进行后续步骤。</font>

<font style="color:rgb(89, 97, 114);"></font>

<font style="color:rgb(89, 97, 114);">Windows 运行 Win+R 键，然后输入“taskschd.msc”，按 Enter 键打开任务计划程序。</font>

<font style="color:rgb(89, 97, 114);">点击右边的“创建基本任务”，设置任务的名称。</font>

<font style="color:rgb(89, 97, 114);">设置任务的执行时间，选择“每天”，并设置具体执行的时间</font>

<font style="color:rgb(89, 97, 114);">设置任务执行的操作，选择“启动程序”，设置执行程序为“PowerShell”，添加执行参数“C:\RVTools\Task\RVToolsBatchVC.ps1”。</font>

<font style="color:rgb(89, 97, 114);">确定任务，勾选下面的复选框，点击完成。</font>

<font style="color:rgb(89, 97, 114);">在“安全选项”设置中，勾选“不管用户是否登录都要运行”，配置合适的系统类型，点击确定并输入执行任务的用户密码。</font>

<font style="color:rgb(89, 97, 114);">最后，等待任务执行，并查看结果。</font>

<font style="color:rgb(89, 97, 114);">批量使用循环导出并且合并，可以搭配任务计划程序</font>

# <font style="color:rgb(89, 97, 114);">批量导出的powershell脚本</font>
```powershell
# Save current directory
$SaveCurrentDir = (get-location).Path

# Set RVTools path
[string] $RVToolsPath = "D:\Program Files (x86)\Dell\RVTools"

# cd to RVTools directory
set-location $RVToolsPath

# 定义多个 vCenter Server 的数组
[string[]] $VCServers = @("192.168.xxx.xxx",
						  "192.168.xxx.xxx", 
						  "192.168.xxx.100",
						  "192.168.xxx.5",
						  "192.168.xxx.100", 
						  "192.168.xxx.100",
						  "192.168.xxx.231",
						  "192.168.xxx.231")

# 定义用户和加密密码
[string] $User = "administrator@vsphere.local"
[string] $EncryptedPassword = "_RVToolsV3PWD01000000d08c9ddf0115d1118c7a00c04fc297eb01000000154ab263f21f8d468e1984cc409001dd00000000020000000000106600000001000020000000a322e7942f6897def448e69e4abe167bd1f57569d74514baba40516ee7f621f9000000000e80000000020000200000001aec6b2937e340e8e085377f6d24c48cf2ce672373e450cb7b37c5cf810b704120000000ce7e08996f817aac399db2da054bc087fca04141fc83fa19dea0a7f7424fe0d94000000060fe21381765f31dccbe215005922258d97468177e1b79cfe6b1e04402908fce98bf323a001893f7de4dcb41884efb1c5d806b458b51809e8b0428479079295b"

# 定义导出目录和文件名模板
[string] $XlsxDir = "D:\RVtools-file"
[string] $OutputFile = "$XlsxDir\vcenter_combined.xlsx"
# 定义一个空数组，用于保存所有导出的文件路径
[string[]] $ExportedFiles = @()

# 删除目录下的所有文件，确保干净的环境
Write-Host "Cleaning directory $XlsxDir" -ForegroundColor Yellow
Remove-Item -Path "$XlsxDir\*" -Force -Recurse

# 遍历每个 vCenter Server
foreach ($VCServer in $VCServers) {
    # 动态生成导出文件名
    $XlsxFile = "$VCServer.xlsx"
	# 添加导出的文件路径到数组
    $ExportedFiles += "$XlsxDir\$XlsxFile"
    # 开始导出当前 vCenter Server 的数据
    Write-Host "Start export for vCenter $VCServer" -ForegroundColor DarkYellow
    $Arguments = "-u $User -p $EncryptedPassword -s $VCServer -c ExportAll2xlsx -d $XlsxDir -f $XlsxFile"
    
    Write-Host $Arguments

    # 启动 RVTools.exe 并传递参数
    $Process = Start-Process -FilePath ".\RVTools.exe" -ArgumentList $Arguments -NoNewWindow -Wait -PassThru

    # 检查进程的退出代码，确保导出成功
    if ($Process.ExitCode -eq -1) {
        Write-Host "Error: Export failed for $VCServer! RVTools returned exitcode -1, probably a connection error! Skipping to the next server." -ForegroundColor Red
        continue  # 跳过当前的 vCenter，继续下一个
    } else {
        Write-Host "Export for $VCServer completed successfully." -ForegroundColor Green
    }
}

Write-Host "All exports completed." -ForegroundColor Cyan

# 如果有导出的文件，开始合并
if ($ExportedFiles.Count -gt 0) {
    # 将数组中的文件路径连接成一个字符串，使用分号分隔
    $InputFiles = [string]::Join(";", $ExportedFiles)

    # 执行合并命令
    Write-Host "Start merging files: $InputFiles" -ForegroundColor Cyan
    & .\RVToolsMergeExcelFiles.exe -input $InputFiles -output $OutputFile -overwrite -verbose

    Write-Host "Merge completed. Combined file saved at: $OutputFile" -ForegroundColor Green
} else {
    Write-Host "No files were exported, skipping merge process." -ForegroundColor Yellow
}



```

# 导入数据库
```python
import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, Text, MetaData
from sqlalchemy.sql import text  # 新增此行导入
from pandas.api.types import is_string_dtype, is_numeric_dtype
import datetime

# 连接到 SQLite 数据库
engine = create_engine('sqlite:///vcenter.db')

# 获取连接对象
with engine.connect() as connection:
    # 删除所有表
    metadata = MetaData()
    metadata.reflect(bind=engine)
    for table in reversed(metadata.sorted_tables):
        connection.execute(text(f"DROP TABLE IF EXISTS {table.name}"))  # 使用 text 函数
    print("所有表已删除")

    # 读取 Excel 文件
    file_path = 'vcenter_combined.xlsx'
    xls = pd.ExcelFile(file_path)

    # 遍历每个表单
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)


        # 转换 timedelta 类型为秒
        def convert_timedelta(val):
            if isinstance(val, datetime.timedelta):
                return val.total_seconds()
            return val


        # 对每一列进行 timedelta 转换
        df = df.apply(lambda col: col.map(convert_timedelta))

        # 获取表名
        table_name = sheet_name.lower()

        # 自动创建表结构
        metadata = MetaData()
        columns = []

        for col_name in df.columns:
            if is_string_dtype(df[col_name]):
                if df[col_name].str.len().max() > 255:
                    columns.append(Column(col_name, Text))  # 处理较长文本
                else:
                    columns.append(Column(col_name, String(255)))  # 默认字符串长度255
            elif is_numeric_dtype(df[col_name]):
                columns.append(Column(col_name, Integer))  # 数字类型
            else:
                columns.append(Column(col_name, String(255)))  # 默认处理为 String

        # 创建表
        table = Table(table_name, metadata, *columns)
        metadata.create_all(engine)

        # 将数据插入数据库
        df.to_sql(table_name, engine, if_exists='append', index=False)

print("所有表单已成功导入到数据库！")

```

# poetry管理项目
```powershell
pip install poetry
创建虚拟环境后,进入虚拟环境
./venv/Scripts/acvivate
poetry init
poetry add openpyxl sqlalchemy pandas
poetry install 
```



