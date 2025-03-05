<font style="color:rgb(51, 51, 51);">在本章中，您将学习如何在Java程序中使用SQLite。</font>

## <font style="color:rgb(51, 51, 51);">安装</font>
<font style="color:rgb(51, 51, 51);">在我们的Java程序中开始使用SQLite之前，您需要确保在计算机上设置了SQLite JDBC驱动程序和Java。您可以检查Java教程以在计算机上安装Java。现在，让我们检查一下如何设置SQLite JDBC驱动程序。</font>

+ <font style="color:rgb(51, 51, 51);">从</font>[<font style="color:rgb(51, 51, 51);">sqlite-jdbc</font>](https://bitbucket.org/xerial/sqlite-jdbc/downloads)<font style="color:rgb(51, 51, 51);">存储库下载最新版本的</font>_<font style="color:rgb(51, 51, 51);">sqlite-jdbc-(VERSION).jar</font>_<font style="color:rgb(51, 51, 51);">。</font>
+ <font style="color:rgb(51, 51, 51);">将下载的jar文件</font>_<font style="color:rgb(51, 51, 51);">sqlite-jdbc-(VERSION).jar添加</font>_<font style="color:rgb(51, 51, 51);">到您的类路径中，或者将其与-classpath选项一起使用，如以下示例中所述。</font>

## <font style="color:rgb(51, 51, 51);">连接到数据库</font>
<font style="color:rgb(51, 51, 51);">以下Java程序显示了如何连接到现有数据库。如果数据库不存在，则将创建该数据库，最后将返回一个数据库对象。</font>

```java
import java.sql.*;

public class SQLiteJDBC {
    public static void main( String args[] ) {
        Connection c = null;

        try {
            Class.forName("org.sqlite.JDBC");
            c = DriverManager.getConnection("jdbc:sqlite:test.db");
        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        }
        System.out.println("已成功打开数据库");
    }
}
```

<font style="color:rgb(51, 51, 51);">现在，让我们编译并运行上述程序，以</font>**<font style="color:rgb(51, 51, 51);">test.db</font>**<font style="color:rgb(51, 51, 51);">在当前目录中创建数据库。您可以根据需要更改路径。我们假定当前路径中提供了最新版本的JDBC驱动程序</font>_<font style="color:rgb(51, 51, 51);">sqlite-jdbc-3.7.2.jar</font>_<font style="color:rgb(51, 51, 51);">。</font>

```java
$javac SQLiteJDBC.java
$java -classpath ".:sqlite-jdbc-3.7.2.jar" SQLiteJDBC
Open database successfully
```

<font style="color:rgb(51, 51, 51);">如果您要使用Windows计算机，则可以按以下方式编译和运行代码-</font>

```java
$javac SQLiteJDBC.java
$java -classpath ".;sqlite-jdbc-3.7.2.jar" SQLiteJDBC
已成功打开数据库
```

## <font style="color:rgb(51, 51, 51);">创建表</font>
<font style="color:rgb(51, 51, 51);">以下Java程序将用于在先前创建的数据库中创建表。</font>

```java
import java.sql.*;

public class SQLiteJDBC {

    public static void main( String args[] ) {
        Connection c = null;
        Statement stmt = null;

        try {
            Class.forName("org.sqlite.JDBC");
            c = DriverManager.getConnection("jdbc:sqlite:test.db");
            System.out.println("已成功打开数据库");

            stmt = c.createStatement();
            String sql = "CREATE TABLE COMPANY " +
            "(ID INT PRIMARY KEY     NOT NULL," +
            " NAME           TEXT    NOT NULL, " + 
            " AGE            INT     NOT NULL, " + 
            " ADDRESS        CHAR(50), " + 
            " SALARY         REAL)"; 
            stmt.executeUpdate(sql);
            stmt.close();
            c.close();
        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        }
        System.out.println("表创建成功");
    }
}
```

<font style="color:rgb(51, 51, 51);">编译并执行上述程序后，它将在您的公司中创建COMPANY表，</font>**<font style="color:rgb(51, 51, 51);">test.db</font>**<font style="color:rgb(51, 51, 51);">文件的最终列表如下-</font>

```java
-rw-r--r--. 1 root root 3201128 Jan 22 19:04 sqlite-jdbc-3.7.2.jar
-rw-r--r--. 1 root root    1506 May  8 05:43 SQLiteJDBC.class
-rw-r--r--. 1 root root     832 May  8 05:42 SQLiteJDBC.java
-rw-r--r--. 1 root root    3072 May  8 05:43 test.db
```

## <font style="color:rgb(51, 51, 51);">INSERT 操作</font>
<font style="color:rgb(51, 51, 51);">以下Java程序显示了如何在上面的示例中创建的COMPANY表中创建记录。</font>

```java
import java.sql.*;

public class SQLiteJDBC {

    public static void main( String args[] ) {
        Connection c = null;
        Statement stmt = null;

        try {
            Class.forName("org.sqlite.JDBC");
            c = DriverManager.getConnection("jdbc:sqlite:test.db");
            c.setAutoCommit(false);
            System.out.println("已成功打开数据库");

            stmt = c.createStatement();
            String sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) " +
            "VALUES (1, 'Paul', 32, 'California', 20000.00 );"; 
            stmt.executeUpdate(sql);

            sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) " +
            "VALUES (2, 'Allen', 25, 'Texas', 15000.00 );"; 
            stmt.executeUpdate(sql);

            sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) " +
            "VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );"; 
            stmt.executeUpdate(sql);

            sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) " +
            "VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );"; 
            stmt.executeUpdate(sql);

            stmt.close();
            c.commit();
            c.close();
        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        }
        System.out.println("记录创建成功");
    }
}
```

<font style="color:rgb(51, 51, 51);">编译并执行上述程序时，它将在COMPANY表中创建给定记录，并显示以下两行-</font>

```java
已成功打开数据库
记录创建成功
```

## <font style="color:rgb(51, 51, 51);">SELECT 操作</font>
<font style="color:rgb(51, 51, 51);">以下Java程序显示了如何从在上面的示例中创建的COMPANY表中获取和显示记录。</font>

```java
import java.sql.*;

public class SQLiteJDBC {

    public static void main( String args[] ) {

        Connection c = null;
        Statement stmt = null;
        try {
            Class.forName("org.sqlite.JDBC");
            c = DriverManager.getConnection("jdbc:sqlite:test.db");
            c.setAutoCommit(false);
            System.out.println("已成功打开数据库");

            stmt = c.createStatement();
            ResultSet rs = stmt.executeQuery( "SELECT * FROM COMPANY;" );

            while ( rs.next() ) {
                int id = rs.getInt("id");
                String  name = rs.getString("name");
                int age  = rs.getInt("age");
                String  address = rs.getString("address");
                float salary = rs.getFloat("salary");

                System.out.println( "ID = " + id );
                System.out.println( "NAME = " + name );
                System.out.println( "AGE = " + age );
                System.out.println( "ADDRESS = " + address );
                System.out.println( "SALARY = " + salary );
                System.out.println();
            }
            rs.close();
            stmt.close();
            c.close();
        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        }
        System.out.println("已操作成功");
    }
}
```

<font style="color:rgb(51, 51, 51);">编译并执行上述程序后，将产生以下结果。</font>

```java
已成功打开数据库
ID = 1
NAME = Paul
AGE = 32
ADDRESS = California
SALARY = 20000.0

ID = 2
NAME = Allen
AGE = 25
ADDRESS = Texas
SALARY = 15000.0

ID = 3
NAME = Teddy
AGE = 23
ADDRESS = Norway
SALARY = 20000.0

ID = 4
NAME = Mark
AGE = 25
ADDRESS = Rich-Mond
SALARY = 65000.0
已操作成功
```

## <font style="color:rgb(51, 51, 51);">UPDATE 操作</font>
<font style="color:rgb(51, 51, 51);">以下Java代码显示了如何使用UPDATE语句更新任何记录，然后从COMPANY表中获取并显示更新的记录。</font>

```java
import java.sql.*;

public class SQLiteJDBC {

    public static void main( String args[] ) {

        Connection c = null;
        Statement stmt = null;

        try {
            Class.forName("org.sqlite.JDBC");
            c = DriverManager.getConnection("jdbc:sqlite:test.db");
            c.setAutoCommit(false);
            System.out.println("已成功打开数据库");

            stmt = c.createStatement();
            String sql = "UPDATE COMPANY set SALARY = 25000.00 where ID=1;";
            stmt.executeUpdate(sql);
            c.commit();

            ResultSet rs = stmt.executeQuery( "SELECT * FROM COMPANY;" );

            while ( rs.next() ) {
                int id = rs.getInt("id");
                String  name = rs.getString("name");
                int age  = rs.getInt("age");
                String  address = rs.getString("address");
                float salary = rs.getFloat("salary");

                System.out.println( "ID = " + id );
                System.out.println( "NAME = " + name );
                System.out.println( "AGE = " + age );
                System.out.println( "ADDRESS = " + address );
                System.out.println( "SALARY = " + salary );
                System.out.println();
            }
            rs.close();
            stmt.close();
            c.close();
        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        }
        System.out.println("操作成功完成");
    }
}
```

<font style="color:rgb(51, 51, 51);">编译并执行上述程序后，将产生以下结果。</font>

```java
已成功打开数据库
ID = 1
NAME = Paul
AGE = 32
ADDRESS = California
SALARY = 25000.0

ID = 2
NAME = Allen
AGE = 25
ADDRESS = Texas
SALARY = 15000.0

ID = 3
NAME = Teddy
AGE = 23
ADDRESS = Norway
SALARY = 20000.0

ID = 4
NAME = Mark
AGE = 25
ADDRESS = Rich-Mond
SALARY = 65000.0

操作成功完成
```

## <font style="color:rgb(51, 51, 51);">删除操作</font>
<font style="color:rgb(51, 51, 51);">以下Java代码显示了如何使用DELETE语句删除任何记录，然后从COMPANY表中获取并显示其余记录。</font>

```java
import java.sql.*;

public class SQLiteJDBC {

    public static void main( String args[] ) {
        Connection c = null;
        Statement stmt = null;

        try {
            Class.forName("org.sqlite.JDBC");
            c = DriverManager.getConnection("jdbc:sqlite:test.db");
            c.setAutoCommit(false);
            System.out.println("已成功打开数据库");

            stmt = c.createStatement();
            String sql = "DELETE from COMPANY where ID=2;";
            stmt.executeUpdate(sql);
            c.commit();

            ResultSet rs = stmt.executeQuery( "SELECT * FROM COMPANY;" );

            while ( rs.next() ) {
                int id = rs.getInt("id");
                String  name = rs.getString("name");
                int age  = rs.getInt("age");
                String  address = rs.getString("address");
                float salary = rs.getFloat("salary");

                System.out.println( "ID = " + id );
                System.out.println( "NAME = " + name );
                System.out.println( "AGE = " + age );
                System.out.println( "ADDRESS = " + address );
                System.out.println( "SALARY = " + salary );
                System.out.println();
            }
            rs.close();
            stmt.close();
            c.close();
        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        }
        System.out.println("已操作成功");
    }
}
```

<font style="color:rgb(51, 51, 51);">编译并执行上述程序后，将产生以下结果。</font>

```java
已成功打开数据库
ID = 1
NAME = Paul
AGE = 32
ADDRESS = California
SALARY = 25000.0

ID = 3
NAME = Teddy
AGE = 23
ADDRESS = Norway
SALARY = 20000.0

ID = 4
NAME = Mark
AGE = 25
ADDRESS = Rich-Mond
SALARY = 65000.0
已操作成功
```

