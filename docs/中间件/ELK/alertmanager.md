```yaml
name: "APP ERROR OR Exception Log Detected"
type: any
index: "*test-esign*"
timestamp_field: "@timestamp"
filter:
  - match:
      Log_Type: "error"

# 触发动作，发送邮件
alert:
  - "email"
  - "command" # 添加 command 类型的告警
# 邮件告警的配置
email:
  - "xxxx@xxxx.com"
  - "xxx@xxxx.com"
# 邮件告警的标题和内容
email_subject: "test-esign APP ERROR OR Exception Log Detected"
alert_text_type: alert_text_only
email_body: |
  <h1>test-xxx Java 出现错误</h1>
  <p>test-xxx app 错误日志</p>
  <p> 涉及主机: {}</p>
  <p> 部分有关信息: {}</p>
  <p>请及时处理</p>

alert_text_args:
  - Host_IP
  - message

# 命令告警的配置
command:
  [
    "/usr/local/bin/python",
    "/opt/elastalert/rules/elk_to_im.py",
    "['xxxx','xxxxx']",
    "test-xxxx的APP出现错误",
    "{Host_IP}",
    "{message}"
  ]



```

