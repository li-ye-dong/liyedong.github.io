<font style="color:rgb(51, 51, 51);">SQLite之后是称为语法的一组独特的规则和准则。本章列出了所有基本的SQLite语法。</font>

## <font style="color:rgb(51, 51, 51);">区分大小写</font>
<font style="color:rgb(51, 51, 51);">需要注意的一点是，SQLite不区分大小写，即子句GLOB和glob在SQLite语句中具有相同的含义。</font>

## <font style="color:rgb(51, 51, 51);">注释</font>
<font style="color:rgb(51, 51, 51);">SQLite注释是额外的注释，可以添加到SQLite代码中以提高其可读性，并且可以出现在任何地方；可以出现空白，包括表达式内部和其他SQL语句的中间，但不能嵌套。</font>

<font style="color:rgb(51, 51, 51);">SQL注释以两个连续的“-”字符（ASCII 0x2d）开头，并扩展到下一个换行符（ASCII 0x0a）或直到输入结束，以先到者为准。</font>

<font style="color:rgb(51, 51, 51);">您还可以使用C样式的注释，该注释以“ / *”开头，并扩展到下一个“ * /”字符对并包括下一个“ * /”字符对，或者直到输入结束（以先到者为准）。C样式注释可以跨越多行。</font>

```sql
sqlite> .help -- This is a single line comment
```

## <font style="color:rgb(51, 51, 51);">SQLite语句</font>
<font style="color:rgb(51, 51, 51);">所有SQLite语句均以SELECT，INSERT，UPDATE，DELETE，ALTER，DROP等任何关键字开头，所有语句均以分号（;）结尾。</font>

### <font style="color:rgb(51, 51, 51);">SQLite ANALYZE语句</font>
```sql
ANALYZE;
or
ANALYZE database_name;
or
ANALYZE database_name.table_name;
```

### <font style="color:rgb(51, 51, 51);">SQLite AND / OR子句</font>
```sql
SELECT column1, column2....columnN
FROM table_name
WHERE CONDITION-1 {AND|OR} CONDITION-2;
```

### <font style="color:rgb(51, 51, 51);">SQLite ALTER TABLE语句</font>
```sql
ALTER TABLE table_name ADD COLUMN column_def...;
```

### <font style="color:rgb(51, 51, 51);">SQLite ALTER TABLE语句（重命名）</font>
```sql
ALTER TABLE table_name RENAME TO new_table_name;
```

### <font style="color:rgb(51, 51, 51);">SQLite ATTACH DATABASE语句</font>
```sql
ATTACH DATABASE 'DatabaseName' As 'Alias-Name';
```

### <font style="color:rgb(51, 51, 51);">SQLite BEGIN TRANSACTION语句</font>
```sql
BEGIN;
or
BEGIN EXCLUSIVE TRANSACTION;
```

### <font style="color:rgb(51, 51, 51);">SQLite BETWEEN子句</font>
```sql
SELECT column1, column2....columnN
FROM table_name
WHERE column_name BETWEEN val-1 AND val-2;
```

### <font style="color:rgb(51, 51, 51);">SQLite COMMIT语句</font>
<font style="color:rgb(51, 51, 51);">COMMIT;</font>

### <font style="color:rgb(51, 51, 51);">SQLite CREATE INDEX语句</font>
```sql
CREATE INDEX index_name
ON table_name ( column_name COLLATE NOCASE );
```

### <font style="color:rgb(51, 51, 51);">SQLite CREATE UNIQUE INDEX语句</font>
```sql
CREATE UNIQUE INDEX index_name
ON table_name ( column1, column2,...columnN);
```

### <font style="color:rgb(51, 51, 51);">SQLite CREATE TABLE语句</font>
```sql
CREATE TABLE table_name(
  column1 datatype,
  column2 datatype,
  column3 datatype,
  .....
  columnN datatype,
  PRIMARY KEY( one or more columns ));
```

### <font style="color:rgb(51, 51, 51);">SQLite CREATE TRIGGER语句</font>
```sql
CREATE TRIGGER database_name.trigger_name 
BEFORE INSERT ON table_name FOR EACH ROW
BEGIN 
   stmt1; 
   stmt2;
   ....
END;
```

### <font style="color:rgb(51, 51, 51);">SQLite CREATE VIEW语句</font>
```sql
CREATE VIEW database_name.view_name AS
SELECT statement....;
```

### <font style="color:rgb(51, 51, 51);">SQLite CREATE VIRTUAL TABLE语句</font>
```sql
CREATE VIRTUAL TABLE database_name.table_name USING weblog( access.log );
or
CREATE VIRTUAL TABLE database_name.table_name USING fts3( );
```

### <font style="color:rgb(51, 51, 51);">SQLite COMMIT TRANSACTION语句</font>
<font style="color:rgb(51, 51, 51);">COMMIT;</font>

### <font style="color:rgb(51, 51, 51);">SQLite COUNT子句</font>
```sql
SELECT COUNT(column_name)FROM table_name
WHERE CONDITION;
```

### <font style="color:rgb(51, 51, 51);">SQLite DELETE语句</font>
```sql
DELETE FROM table_name
WHERE {CONDITION};
```

### <font style="color:rgb(51, 51, 51);">SQLite DETACH DATABASE语句</font>
```sql
DETACH DATABASE 'Alias-Name';
```

### <font style="color:rgb(51, 51, 51);">SQLite DISTINCT子句</font>
```sql
SELECT DISTINCT column1, column2....columnN
FROM table_name;
```

### <font style="color:rgb(51, 51, 51);">SQLite DROP INDEX语句</font>
```sql
DROP INDEX database_name.index_name;
```

### <font style="color:rgb(51, 51, 51);">SQLite DROP TABLE语句</font>
```sql
DROP TABLE database_name.table_name;
```

### <font style="color:rgb(51, 51, 51);">SQLite DROP VIEW语句</font>
```sql
DROP INDEX database_name.view_name;
```

### <font style="color:rgb(51, 51, 51);">SQLite DROP TRIGGER语句</font>
```sql
DROP INDEX database_name.trigger_name;
```

### <font style="color:rgb(51, 51, 51);">SQLite EXISTS子句</font>
```sql
SELECT column1, column2....columnN
FROM table_name
WHERE column_name EXISTS (SELECT * FROM   table_name );
```

### <font style="color:rgb(51, 51, 51);">SQLite EXPLAIN语句</font>
```sql
EXPLAIN INSERT statement...;
or 
EXPLAIN QUERY PLAN SELECT statement...;
```

### <font style="color:rgb(51, 51, 51);">SQLite GLOB子句</font>
```sql
SELECT column1, column2....columnN
FROM table_name
WHERE column_name GLOB { PATTERN };
```

### <font style="color:rgb(51, 51, 51);">SQLite GROUP BY子句</font>
```sql
SELECT SUM(column_name)FROM table_name
WHERE CONDITION
GROUP BY column_name;
```

### <font style="color:rgb(51, 51, 51);">SQLite HAVING子句</font>
```sql
SELECT SUM(column_name)FROM table_name
WHERE CONDITION
GROUP BY column_name
HAVING (arithematic function condition);
```

### <font style="color:rgb(51, 51, 51);">SQLite INSERT INTO语句</font>
```sql
INSERT INTO table_name( column1, column2....columnN)
VALUES ( value1, value2....valueN);
```

### <font style="color:rgb(51, 51, 51);">SQLite IN子句</font>
```sql
SELECT column1, column2....columnN
FROM table_name
WHERE column_name IN (val-1, val-2,...val-N);
```

### <font style="color:rgb(51, 51, 51);">SQLite LIKE子句</font>
```sql
SELECT column1, column2....columnN
FROM table_name
WHERE column_name LIKE { PATTERN };
```

### <font style="color:rgb(51, 51, 51);">SQLite NOT IN子句</font>
```sql
SELECT column1, column2....columnN
FROM table_name
WHERE column_name NOT IN (val-1, val-2,...val-N);
```

### <font style="color:rgb(51, 51, 51);">SQLite ORDER BY子句</font>
```sql
SELECT column1, column2....columnN
FROM table_name
WHERE CONDITION
ORDER BY column_name {ASC|DESC};
```

### <font style="color:rgb(51, 51, 51);">SQLite PRAGMA语句</font>
```sql
PRAGMA pragma_name;

For example:

PRAGMA page_size;
PRAGMA cache_size = 1024;
PRAGMA table_info(table_name);
```

### <font style="color:rgb(51, 51, 51);">SQLite RELEASE SAVEPOINT语句</font>
<font style="color:rgb(51, 51, 51);">RELEASE savepoint_name;</font>

### <font style="color:rgb(51, 51, 51);">SQLite REINDEX语句</font>
```sql
REINDEX collation_name;
REINDEX database_name.index_name;
REINDEX database_name.table_name;
```

### <font style="color:rgb(51, 51, 51);">SQLite ROLLBACK语句</font>
```sql
ROLLBACK;
or
ROLLBACK TO SAVEPOINT savepoint_name;
```

### <font style="color:rgb(51, 51, 51);">SQLite SAVEPOINT语句</font>
<font style="color:rgb(51, 51, 51);">SAVEPOINT savepoint_name;</font>

### <font style="color:rgb(51, 51, 51);">SQLite SELECT语句</font>
```sql
SELECT column1, column2....columnN
FROM table_name;
```

### <font style="color:rgb(51, 51, 51);">SQLite UPDATE语句</font>
```sql
UPDATE table_name
SET column1 = value1, column2 = value2....columnN=valueN
[ WHERE  CONDITION ];
```

### <font style="color:rgb(51, 51, 51);">SQLite VACUUM语句</font>
<font style="color:rgb(51, 51, 51);">VACUUM;</font>

### <font style="color:rgb(51, 51, 51);">SQLite WHERE子句</font>
```sql
SELECT column1, column2....columnN
FROM table_name
WHERE CONDITION;
```

