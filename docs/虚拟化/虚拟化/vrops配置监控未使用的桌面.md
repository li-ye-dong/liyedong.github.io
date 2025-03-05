[https://docs.vmware.com/cn/Management-Packs-for-vRealize-Operations/2.5.1/Horizon/GUID-6ACF92E4-5925-43A6-8A9E-E280B1B53F69.html](https://docs.vmware.com/cn/Management-Packs-for-vRealize-Operations/2.5.1/Horizon/GUID-6ACF92E4-5925-43A6-8A9E-E280B1B53F69.html)

<font style="color:rgb(86, 86, 86);">您可以进行配置，以监控未使用的桌面。</font>

## <font style="color:rgb(0, 0, 0);">过程</font>
1. <font style="color:rgb(86, 86, 86);">从左侧菜单中，单击</font>**<font style="color:rgb(86, 86, 86);">可视化</font>****<font style="color:rgb(86, 86, 86);"> </font>****<font style="color:rgb(86, 86, 86);">></font>****<font style="color:rgb(86, 86, 86);"> </font>****<font style="color:rgb(86, 86, 86);">视图</font>**<font style="color:rgb(86, 86, 86);">，然后单击</font>**<font style="color:rgb(86, 86, 86);">创建</font>**<font style="color:rgb(86, 86, 86);">。</font>
2. <font style="color:rgb(86, 86, 86);">在</font>**<font style="color:rgb(86, 86, 86);">视图类型</font>**<font style="color:rgb(86, 86, 86);">屏幕中，单击</font>**<font style="color:rgb(86, 86, 86);">列表</font>**<font style="color:rgb(86, 86, 86);">。</font>

经检测，数据不准确



# 如何筛选出长期未登录的桌面
1. 根据虚拟桌面控制台导出虚拟桌面的计算机信息。

2. 连接事件数据库执行以下sql，日期采用根据需要修改

```sql
SELECT DISTINCT ModuleAndEventText
FROM dbo.event
WHERE Time BETWEEN '2024-09-01 00:00:00' AND '2024-09-25 23:59:59'
AND EventType = 'BROKER_USERLOGGEDIN';
```

3. 根据计算机信息和登录日志，进行数据处理，筛选出未登录的计算机信息

4. 目前还在不断完善中，该方式最为准确

