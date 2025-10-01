## ✅ Java 17 + Maven 多阶段构建 Dockerfile
```bash
# 第一阶段：构建 Java 应用
FROM maven:3.9-eclipse-temurin-17 AS builder

# 设置国内 Maven 源（可选）
COPY settings.xml /root/.m2/settings.xml

WORKDIR /app

# 复制项目文件并构建
COPY pom.xml ./
COPY src ./src
RUN mvn clean package -DskipTests

# 第二阶段：运行 jar 应用
FROM eclipse-temurin:17-jre

WORKDIR /app

# 拷贝构建好的 jar 包（假设名称为 app.jar）
COPY --from=builder /app/target/*.jar app.jar

# 暴露服务端口
EXPOSE 8080

# 启动命令
ENTRYPOINT ["java", "-jar", "app.jar"]
```



```bash
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0">
  <mirrors>
    <mirror>
      <id>aliyunmaven</id>
      <mirrorOf>*</mirrorOf>
      <name>Aliyun Maven</name>
      <url>https://maven.aliyun.com/repository/public</url>
    </mirror>
  </mirrors>
</settings>

```

## ✅ Java 8 + Maven 多阶段构建 Dockerfile
```plain
dockerfile


复制编辑
# -------- 第一阶段：使用 Maven 构建 --------
FROM maven:3.9-eclipse-temurin-8 AS builder

# 设置阿里云 maven 镜像源（可选）
COPY settings.xml /root/.m2/settings.xml

WORKDIR /app

# 拷贝 pom.xml 和源码，分步缓存依赖
COPY pom.xml ./
RUN mvn dependency:resolve

COPY src ./src
RUN mvn clean package -DskipTests

# -------- 第二阶段：运行 jar 应用 --------
FROM eclipse-temurin:8-jre

WORKDIR /app

# 拷贝构建产物
COPY --from=builder /app/target/*.jar app.jar

EXPOSE 8080

CMD ["java", "-jar", "app.jar"]
```

---

## ✅ Java 11 + Maven 多阶段构建 Dockerfile
```plain
dockerfile


复制编辑
# -------- 第一阶段：构建 --------
FROM maven:3.9-eclipse-temurin-11 AS builder

COPY settings.xml /root/.m2/settings.xml

WORKDIR /app

COPY pom.xml ./
RUN mvn dependency:resolve

COPY src ./src
RUN mvn clean package -DskipTests

# -------- 第二阶段：运行 --------
FROM eclipse-temurin:11-jre

WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar

EXPOSE 8080

CMD ["java", "-jar", "app.jar"]
```

---

## ☁️ Maven 国内源 settings.xml 示例（阿里云源）
放在项目根目录，与 Dockerfile 同级：

```plain
xml


复制编辑
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0">
  <mirrors>
    <mirror>
      <id>aliyunmaven</id>
      <mirrorOf>*</mirrorOf>
      <name>Aliyun Maven</name>
      <url>https://maven.aliyun.com/repository/public</url>
    </mirror>
  </mirrors>
</settings>
```

---

## 📌 推荐镜像说明
| Java 版本 | Maven 镜像 | 运行时镜像 |
| --- | --- | --- |
| Java 8 | `maven:3.9-eclipse-temurin-8` | `eclipse-temurin:8-jre` |
| Java 11 | `maven:3.9-eclipse-temurin-11` | `eclipse-temurin:11-jre` |


---

## 🧪 构建命令示例
```plain
bash


复制编辑
docker build -t my-java8-app -f Dockerfile.java8 .
docker build -t my-java11-app -f Dockerfile.java11 .
```

---

如果你希望进一步统一 Harbor 镜像仓库地址（如 `harbor.liyedong.com/java/temurin:8-jre`），我也可以帮你自定义基础镜像，或者构建 Drone CI/CD 的 pipeline 文件（如 `.drone.yml`）来实现自动构建部署。是否继续？

询问 ChatGPT

