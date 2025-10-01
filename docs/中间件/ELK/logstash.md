```yaml
input {
  kafka {
    bootstrap_servers => "192.168.107.65:9092"
    topics => ["test-esign"]
    codec => "json"
    type => "test-esign"
  }
}

filter {
  if  [type] =="bpm" {
    mutate {
      rename => {
        "[log][file][path]" => "file_path"
      }
      rename => {
        "[log][offset]" => "offset"
      }
      rename => {
        "[host][name]" => "host_name"
      }
      convert => {
        "Module_Version" => "string"
      }
      convert => {
        "OS_Version" => "string"
      }
    }
  }

}

output {
  if [type] == "test-esign" {
    elasticsearch {
      hosts => ["http://192.168.107.186:9200"]
      index => "%{Platform}-test-esign-%{Module_Type}-%{+YYYY.MM}"
    }
  }
}

```

