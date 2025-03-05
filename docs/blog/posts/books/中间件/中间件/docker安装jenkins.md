```plain
docker pull jenkins/jenkins
//创建目录
mkdir -p /var/jenkins_home
//授权权限
chmod 777 /var/jenkins_home
docker run -d -p 10240:8080 -p 10241:50000 -v /var/jenkins_home:/var/jenkins_home -v /etc/localtime:/etc/localtime --name myjenkins jenkins/jenkins
docker ps
```

[http://192.168.XX.XX:10240](http://192.168.XX.XX:10240)

### <font style="color:rgb(0, 0, 0);">2.获取管理员密码</font>


```javascript
cat /var/jenkins_home/secrets/initialAdminPassword
```

