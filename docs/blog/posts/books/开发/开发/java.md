# 参数框架guava
```java
//断言校验  guava框架
Preconditions.checkNotNull(subjectCategoryDTO.getCategoryType(),"分类类型不能为空");
Preconditions.checkArgument(!StringUtils.isEmpty(subjectCategoryDTO.getCategoryName()),"分类名称不能为空");
Preconditions.checkNotNull(subjectCategoryDTO.getParentId(),"父分类不能为空");
SubjectCategoryBO subjectCategoryBO = SubjectCategoryDTOConverter.INSTANCE.convertDtoToCategoryBo(subjectCategoryDTO);

```

```xml
<dependency>
  <groupId>com.google.guava</groupId>
  <artifactId>guava</artifactId>
  <version>19.0</version>
</dependency>
```

# common.lang3
```xml
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-lang3</artifactId>
            <version>3.12.0</version>
        </dependency>
```

```java
StringUtils.isBlank()
```

# DTO和BO
<font style="color:rgb(13, 13, 13);">在 Java 编程中，BO 和 DTO 是两种常见的设计模式，用于管理数据和业务逻辑。它们分别代表业务对象（Business Object）和数据传输对象（Data Transfer Object）。</font>

