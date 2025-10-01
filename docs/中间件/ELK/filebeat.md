```yaml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /usr/local/esign/apps/backend/*/logs/error.log
    - /usr/local/esign/apps/backend/*/logs/service.log
    - /usr/local/esign/apps/backend/*/logs/default.log
  ignore_older: 48h
  close_inactive: 2m
  close_renamed: true
  close_removed: true
  clean_removed: true
  multiline.pattern: '^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3} '
  multiline.negate: true
  multiline.match: after

  fields:
    OS_Type: redhat
    OS_Version: 7.9
    Business_System: test-esign
    Platform: 'app'
    Module_Version: '0'
    Host_IP: 192.168.107.236
  fields_under_root: true

  processors:
    - dissect:
        tokenizer: "/usr/local/esign/apps/backend/%{Module_Type}/logs/%{filename}.log"
        field: "log.file.path"
        target_prefix: "metadata"
    - dissect:
        tokenizer: '%{timestamp} %{+timestamp} %{greedymsg}'
        field: "message"
        target_prefix: ""
        ignore_missing: true
    - rename:
        fields:
          - from: "metadata.filename"
            to: "Log_Type"
          - from: "metadata.Module_Type"
          - to: "Module_Type"
    - timestamp:
        field: "timestamp"
        target_field: "@timestamp"
        layouts:
          - '2006-01-02 15:04:05.000'
        timezone: Asia/Shanghai
 
- type: log
  enabled: true
  paths:
    - /var/log/messages
  ignore_older: 48h
  close_inactive: 2m
  close_renamed: true
  close_removed: true
  clean_removed: true

  fields:
    OS_Type: redhat
    OS_Version: 7.9
    Business_System: test-esign
    Platform: 'os'
    Module_Type: system
    Module_Version: 0
    Host_IP: 192.168.107.236
  fields_under_root: true
  multiline.pattern: '^[A-Za-z]{3}\s{1,2}[0-9]{1,2} [0-9]{2}:[0-9]{2}:[0-9]{2}'
  multiline.negate: true
  multiline.match: after

  processors:
    - script:
        lang: javascript
        id: "msgextract_and_format_timestamp"
        # Jul 28 03:30:01 test-bfs-app systemd: Started Session 8233 of user root.
        source: >
          function process(event) {
            var message = event.Get("message");
            var regex = /^([A-Za-z]{3})\s{1,2}([0-9]{1,2}) ([0-9]{2}:[0-9]{2}:[0-9]{2})/;
            var match = message.match(regex);
            
            var month = match[1];
            var day = match[2];
            var time = match[3];
            var timestamp = month + " " + day + " " + time;
            event.Put("timestamp", timestamp);
          }
    - timestamp:
        field: "timestamp"
        target_field: "@timestamp"
        layouts:
          - 'Jan 2 15:04:05'
        timezone: "Local"
    - drop_fields:
       fields: ["timestamp"]
       
processors:
  - drop_fields:
      fields: ["timestamp","ecs", "input", "container","greedymsg","agent"]
      ignore_missing: true
logging:
  level: info
  to_files: true
  files:
    path: /var/log/filebeat
    keepfiles: 7


output.kafka:
  #hosts: ["192.168.106.63:9092", "192.168.106.64:9092","192.168.106.65:9092"]
  hosts: ["192.168.107.65:9092"]
  topic: '%{[Business_System]}' 
  partition.round_robin:
    reachable_only: false
  required_acks: 1
  compression: gzip
  max_message_bytes: 10000000
#logging.level: debug
#output.console:
#  pretty: true
```



