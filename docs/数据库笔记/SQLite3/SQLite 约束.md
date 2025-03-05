<font style="color:rgb(51, 51, 51);">约束是对表的数据列强制执行的规则。这些用于限制可以进入表的数据类型。这样可以确保数据库中数据的准确性和可靠性。</font>

<font style="color:rgb(51, 51, 51);">约束可以是列级别或表级别。列级约束仅应用于一列，而表级约束则应用于整个表。</font>

<font style="color:rgb(51, 51, 51);">以下是SQLite中可用的常用约束。</font>

+ **<font style="color:rgb(51, 51, 51);">NOT NULL</font>****<font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">约束−确保列不能为NULL值。</font>
+ **<font style="color:rgb(51, 51, 51);">DEFAULT</font>****<font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">约束−如果未指定，则为列提供默认值。</font>
+ **<font style="color:rgb(51, 51, 51);">UNIQUE</font>****<font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">约束−确保列中的所有值均不同。</font>
+ **<font style="color:rgb(51, 51, 51);">PRIMARY Key</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">−唯一标识数据库表中的每一行/记录。</font>
+ **<font style="color:rgb(51, 51, 51);">CHECK</font>****<font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">约束−确保列中的所有值都满足某些条件。</font>

## <font style="color:rgb(51, 51, 51);">NOT NULL 约束</font>
<font style="color:rgb(51, 51, 51);">默认情况下，列可以保存NULL值。如果您不希望某列具有NULL值，则需要在此列上定义此类约束，以指定该列现在不允许NULL。</font>

<font style="color:rgb(51, 51, 51);">NULL等于没有数据，它代表未知数据。</font>

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">例如，下面的SQLite语句创建一个名为COMPANY的新表，并添加五列，其中三列（ID，NAME和AGE）指定不接受NULL。</font>

```sql
CREATE TABLE COMPANY(
  ID INT PRIMARY KEY     NOT NULL,
  NAME           TEXT    NOT NULL,
  AGE            INT     NOT NULL,
  ADDRESS        CHAR(50),
  SALARY         REAL
);
```

## <font style="color:rgb(51, 51, 51);">DEFAULT 约束</font>
<font style="color:rgb(51, 51, 51);">当INSERT INTO语句未提供特定值时，DEFAULT约束将为列提供默认值。</font>

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">例如，以下SQLite语句创建一个名为COMPANY的新表并添加五列。此处，SALARY列默认情况下设置为5000.00，因此，如果INSERT INTO语句不为此列提供值，则默认情况下，此列将设置为5000.00。</font>

```sql
CREATE TABLE COMPANY(
  ID INT PRIMARY KEY     NOT NULL,
  NAME           TEXT    NOT NULL,
  AGE            INT     NOT NULL,
  ADDRESS        CHAR(50),
  SALARY         REAL    DEFAULT 50000.00
);
```

## <font style="color:rgb(51, 51, 51);">UNIQUE 约束</font>
<font style="color:rgb(51, 51, 51);">UNIQUE约束可防止两个记录在特定列中具有相同的值。例如，在COMPANY表中，您可能要防止两个或多个人具有相同的年龄。</font>

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">例如，以下SQLite语句创建一个名为COMPANY的新表并添加五列。在这里，AGE列设置为UNIQUE，因此您不能拥有两个具有相同年龄的记录-</font>

```sql
CREATE TABLE COMPANY(
  ID INT PRIMARY KEY     NOT NULL,
  NAME           TEXT    NOT NULL,
  AGE            INT     NOT NULL UNIQUE,
  ADDRESS        CHAR(50),
  SALARY         REAL    DEFAULT 50000.00
);
```

## <font style="color:rgb(51, 51, 51);">PRIMARY Key约束</font>
<font style="color:rgb(51, 51, 51);">PRIMARY KEY约束唯一地标识数据库表中的每个记录。可以有更多的UNIQUE列，但表中只有一个主键。在设计数据库表时，主键很重要。主键是唯一的ID。</font>

<font style="color:rgb(51, 51, 51);">我们使用它们来引用表行。在表之间创建关系时，主键成为其他表中的外键。由于“长期的编码监督”，SQLite中的主键可以为NULL。其他数据库则不是这种情况。</font>

<font style="color:rgb(51, 51, 51);">主键是表中的字段，它唯一地标识数据库表中的每一行/记录。主键必须包含唯一值。主键列不能具有NULL值。</font>

<font style="color:rgb(51, 51, 51);">一个表只能有一个主键，它可以由单个或多个字段组成。当多个字段用作主键时，它们称为</font>**<font style="color:rgb(51, 51, 51);">composite key</font>**<font style="color:rgb(51, 51, 51);">。</font>

<font style="color:rgb(51, 51, 51);">如果表在任何表上定义了主键field(s)，则不能有两个记录具有相同的值field(s)。</font>

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">您已经在上面看到了许多示例，在这些示例中，我们创建了以ID为主键的COMPANY表。</font>

```sql
CREATE TABLE COMPANY(
  ID INT PRIMARY KEY     NOT NULL,
  NAME           TEXT    NOT NULL,
  AGE            INT     NOT NULL,
  ADDRESS        CHAR(50),
  SALARY         REAL
);
```

## <font style="color:rgb(51, 51, 51);">CHECK约束</font>
<font style="color:rgb(51, 51, 51);">CHECK 约束使条件能够检查输入到记录中的值。如果条件的计算结果为false，则记录违反了约束且未输入到表中。</font>

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">例如，以下SQLite创建一个名为COMPANY的新表并添加五列。在这里，我们添加了一个带有SALARY的CHECK列，因此您不能有任何SALARY 0。</font>

```sql
CREATE TABLE COMPANY3(
  ID INT PRIMARY KEY     NOT NULL,
  NAME           TEXT    NOT NULL,
  AGE            INT     NOT NULL,
  ADDRESS        CHAR(50),
  SALARY         REAL    CHECK(SALARY > 0)
);
```

## <font style="color:rgb(51, 51, 51);">删除约束</font>
<font style="color:rgb(51, 51, 51);">SQLite支持ALTER TABLE的有限子集。SQLite中的ALTER TABLE命令允许用户重命名表或向现有表添加新列。不能重命名列、删除列或在表中添加或删除约束。</font>

