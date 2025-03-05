<font style="color:rgb(51, 51, 51);">在本章中，您将学习如何在C / C ++程序中使用SQLite。</font>

### <font style="color:rgb(51, 51, 51);">安装</font>
<font style="color:rgb(51, 51, 51);">在我们的C / C ++程序中开始使用SQLite之前，您需要确保在计算机上设置了SQLite库。您可以查看“ SQLite安装”一章以了解安装过程。</font>

## <font style="color:rgb(51, 51, 51);">C / C ++接口API</font>
<font style="color:rgb(51, 51, 51);">以下是重要的C / C ++ SQLite接口示例，这些示例足以满足您从C / C ++程序使用SQLite数据库的要求。如果您正在寻找更复杂的应用程序，则可以查阅SQLite官方文档。</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">API和说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | **<font style="color:rgb(51, 51, 51);">sqlite3_open(const char *filename, sqlite3 **ppDb)</font>**<br/><font style="color:rgb(51, 51, 51);">该例程打开与SQLite数据库文件的连接，并返回一个数据库连接对象，供其他SQLite例程使用。</font><br/><font style="color:rgb(51, 51, 51);">如果</font>_<font style="color:rgb(51, 51, 51);">filename</font>_<font style="color:rgb(51, 51, 51);">参数为NULL或'：memory：'，则sqlite3_open()将在RAM中创建一个内存数据库，该数据库仅在会话期间持续存在。</font><br/><font style="color:rgb(51, 51, 51);">如果文件名不为NULL，则sqlite3_open()尝试使用其值打开数据库文件。如果不存在该名称的文件，则sqlite3_open()将打开该名称的新数据库文件。</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | **<font style="color:rgb(51, 51, 51);">sqlite3_exec(sqlite3*, const char *sql, sqlite_callback, void *data, char **errmsg)</font>**<br/><font style="color:rgb(51, 51, 51);">此例程提供了一种快速，简便的方法来执行由sql参数提供的SQL命令，该参数可由多个SQL命令组成。</font><br/><font style="color:rgb(51, 51, 51);">在这里，第一个参数</font>_<font style="color:rgb(51, 51, 51);">sqlite3</font>_<font style="color:rgb(51, 51, 51);">是一个开放的数据库对象，</font>_<font style="color:rgb(51, 51, 51);">sqlite_callback</font>_<font style="color:rgb(51, 51, 51);">是一个回调，其</font>_<font style="color:rgb(51, 51, 51);">数据</font>_<font style="color:rgb(51, 51, 51);">是第一个参数，并且将返回errmsg以捕获例程引发的任何错误。</font><br/><font style="color:rgb(51, 51, 51);">sqlite3_exec()例程解析并执行</font>**<font style="color:rgb(51, 51, 51);">sql</font>**<font style="color:rgb(51, 51, 51);">参数中给定的每个命令，直到到达字符串末尾或遇到错误为止。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | **<font style="color:rgb(51, 51, 51);">sqlite3_close(sqlite3*)</font>**<br/><font style="color:rgb(51, 51, 51);">此例程关闭先前通过调用sqlite3打开的数据库连接_open()。与连接关联的所有准备好的语句应在关闭连接之前完成。</font><br/><font style="color:rgb(51, 51, 51);">如果还有任何尚未完成的查询，则sqlite3_close()将返回SQLITE_BUSY，错误消息由于未完成的语句而无法关闭。</font> |


## <font style="color:rgb(51, 51, 51);">连接到数据库</font>
<font style="color:rgb(51, 51, 51);">以下C代码段显示了如何连接到现有数据库。如果数据库不存在，则将创建该数据库，最后将返回一个数据库对象。</font>

```c
#include <stdio.h>
#include <sqlite3.h> 

int main(int argc, char* argv[]) {
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;

    rc = sqlite3_open("test.db", &db);   if( rc ) {
        fprintf(stderr, "无法打开数据库: %s\n", sqlite3_errmsg(db));
        return(0);
    } else {
        fprintf(stderr, "成功打开数据库\n");
    }
    sqlite3_close(db);
}
```

<font style="color:rgb(51, 51, 51);">现在，让我们编译并运行上述程序，以</font>**<font style="color:rgb(51, 51, 51);">test.db</font>**<font style="color:rgb(51, 51, 51);">在当前目录中创建数据库。您可以根据需要更改路径。</font>

```c
$gcc test.c -l sqlite3
$./a.out
成功打开数据库
```

<font style="color:rgb(51, 51, 51);">如果要使用C ++源代码，则可以按以下方式编译代码-</font>

$g++ test.c -l sqlite3

<font style="color:rgb(51, 51, 51);">在这里，我们将程序与sqlite3库链接在一起，以提供C程序所需的功能。这将在您的目录中创建一个数据库文件test.db，您将得到以下结果。</font>

```c
-rwxr-xr-x. 1 root root 7383 May 8 02:06 a.out
-rw-r--r--. 1 root root  323 May 8 02:05 test.c
-rw-r--r--. 1 root root    0 May 8 02:06 test.db
```

## <font style="color:rgb(51, 51, 51);">创建表</font>
<font style="color:rgb(51, 51, 51);">以下C代码段将用于在先前创建的数据库中创建表-</font>

```c
#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h> 

static int callback(void *NotUsed, int argc, char **argv, char **azColName) {
    int i;
    for(i = 0; i<argc; i++) {
        printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
    }
    printf("\n");
    return 0;
}

int main(int argc, char* argv[]) {
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    char *sql;

    /*打开数据库*/
    rc = sqlite3_open("test.db", &db);   
    if( rc ) {
        fprintf(stderr, "无法打开数据库: %s\n", sqlite3_errmsg(db));
        return(0);
    } else {
        fprintf(stdout, "已成功打开数据库\n");
    }

    /* 创建SQL语句 */
    sql = "CREATE TABLE COMPANY("  \
        "ID INT PRIMARY KEY     NOT NULL," \
        "NAME           TEXT    NOT NULL," \
        "AGE            INT     NOT NULL," \
        "ADDRESS        CHAR(50)," \
        "SALARY         REAL );";

    /* 执行 SQL 语句 */
    rc = sqlite3_exec(db, sql, callback, 0, &zErrMsg);

    if( rc != SQLITE_OK ){
        fprintf(stderr, "SQL error: %s\n", zErrMsg);
        sqlite3_free(zErrMsg);
    } else {
        fprintf(stdout, "表创建成功\n");
    }
    sqlite3_close(db);
    return 0;
}
```

<font style="color:rgb(51, 51, 51);">编译并执行上述程序后，它将在test.db中创建COMPANY表，文件的最终列表如下-</font>

```c
-rwxr-xr-x. 1 root root 9567 May 8 02:31 a.out
-rw-r--r--. 1 root root 1207 May 8 02:31 test.c
-rw-r--r--. 1 root root 3072 May 8 02:31 test.db
```

## <font style="color:rgb(51, 51, 51);">Insert 操作</font>
<font style="color:rgb(51, 51, 51);">以下C代码段显示了如何在上述示例中创建的COMPANY表中创建记录-</font>

```c
#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h> 

static int callback(void *NotUsed, int argc, char **argv, char **azColName) {
    int i;
    for(i = 0; i<argc; i++) {
        printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
    }
    printf("\n");
    return 0;
}

int main(int argc, char* argv[]) {
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    char *sql;

    /* Open database */
    rc = sqlite3_open("test.db", &db);   
    if( rc ) {
        fprintf(stderr, "无法打开数据库: %s\n", sqlite3_errmsg(db));
        return(0);
    } else {
        fprintf(stderr, "已成功打开数据库\n");
    }

    /* 创建SQL语句 */
    sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) "  \
        "VALUES (1, 'Paul', 32, 'California', 20000.00 ); " \
        "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) "  \
        "VALUES (2, 'Allen', 25, 'Texas', 15000.00 ); "     \
        "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)" \
        "VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );" \
        "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)" \
        "VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );";

    /* 执行SQL语句 */
    rc = sqlite3_exec(db, sql, callback, 0, &zErrMsg);

    if( rc != SQLITE_OK ){
        fprintf(stderr, "SQL error: %s\n", zErrMsg);
        sqlite3_free(zErrMsg);
    } else {
        fprintf(stdout, "已成功创建记录\n");
    }
    sqlite3_close(db);
    return 0;
}
```

<font style="color:rgb(51, 51, 51);">编译并执行上述程序后，它将在COMPANY表中创建给定记录，并显示以下两行-</font>

```c
已成功打开数据库
已成功创建记录
```

## <font style="color:rgb(51, 51, 51);">Select 操作</font>
<font style="color:rgb(51, 51, 51);">在继续实际示例以获取记录之前，让我们看一下在示例中使用的有关回调函数的一些细节。该回调提供了一种从SELECT语句获取结果的方法。它具有以下声明-</font>

```c
typedef int (*sqlite3_callback)(
    void*,    /* 在sqlite3_exec()的第4个参数中提供的数据 */
    int,      /* 行中的列数 */
    char**,   /* 表示行中字段的字符串数组 */
    char**    /* 表示列名的字符串数组 */
);
```

<font style="color:rgb(51, 51, 51);">如果上述回调在sqlite_exec()例程中作为第三个参数提供，则SQLite将为在SQL参数内执行的每个SELECT语句中处理的每个记录调用此回调函数。</font>

<font style="color:rgb(51, 51, 51);">以下C代码段显示了如何从上例中创建的COMPANY表中获取和显示记录-</font>

```c
#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h> 

static int callback(void *data, int argc, char **argv, char **azColName){
    int i;
    fprintf(stderr, "%s: ", (const char*)data);

    for(i = 0; i<argc; i++){
        printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
    }

    printf("\n");
    return 0;
}

int main(int argc, char* argv[]) {
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    char *sql;
    const char* data = "Callback function called";

    /* 打开数据库 */
    rc = sqlite3_open("test.db", &db);   
    if( rc ) {
        fprintf(stderr, "无法打开数据库: %s\n", sqlite3_errmsg(db));
        return(0);
    } else {
        fprintf(stderr, "已成功打开数据库\n");
    }

    /* 创建SQL语句 */
    sql = "SELECT * from COMPANY";

    /* 执行SQL语句 */
    rc = sqlite3_exec(db, sql, callback, (void*)data, &zErrMsg);

    if( rc != SQLITE_OK ) {
        fprintf(stderr, "SQL error: %s\n", zErrMsg);
        sqlite3_free(zErrMsg);
    } else {
        fprintf(stdout, "操作成功完成\n");
    }
    sqlite3_close(db);
    return 0;
}
```

<font style="color:rgb(51, 51, 51);">编译并执行上述程序后，将产生以下结果。</font>

```c
已成功打开数据库
Callback function called: ID = 1
    NAME = Paul
AGE = 32
    ADDRESS = California
SALARY = 20000.0

    Callback function called: ID = 2
        NAME = Allen
AGE = 25
        ADDRESS = Texas
SALARY = 15000.0

        Callback function called: ID = 3
            NAME = Teddy
AGE = 23
            ADDRESS = Norway
SALARY = 20000.0

            Callback function called: ID = 4
                NAME = Mark
AGE = 25
                ADDRESS = Rich-Mond
SALARY = 65000.0

                操作成功完成
```

## <font style="color:rgb(51, 51, 51);">UPDATE操作</font>
<font style="color:rgb(51, 51, 51);">以下C代码段显示了如何使用UPDATE语句更新任何记录，然后从COMPANY表中获取并显示更新的记录。</font>

```c
#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h> 

static int callback(void *data, int argc, char **argv, char **azColName){
    int i;
    fprintf(stderr, "%s: ", (const char*)data);

    for(i = 0; i<argc; i++) {
        printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
    }
    printf("\n");
    return 0;
}

int main(int argc, char* argv[]) {
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    char *sql;
    const char* data = "Callback function called";

    /* Open database */
    rc = sqlite3_open("test.db", &db);   
    if( rc ) {
        fprintf(stderr, "无法打开数据库: %s\n", sqlite3_errmsg(db));
        return(0);
    } else {
        fprintf(stderr, "已成功打开数据库\n");
    }

    /*创建合并SQL语句*/
    sql = "UPDATE COMPANY set SALARY = 25000.00 where ID=1; " \
        "SELECT * from COMPANY";

    /* 执行SQL语句 */
    rc = sqlite3_exec(db, sql, callback, (void*)data, &zErrMsg);

    if( rc != SQLITE_OK ) {
        fprintf(stderr, "SQL error: %s\n", zErrMsg);
        sqlite3_free(zErrMsg);
    } else {
        fprintf(stdout, "Operation done successfully\n");
    }
    sqlite3_close(db);
    return 0;
}
```

<font style="color:rgb(51, 51, 51);">编译并执行上述程序后，将产生以下结果。</font>

```c
已成功打开数据库
Callback function called: ID = 1
    NAME = Paul
AGE = 32
    ADDRESS = California
SALARY = 25000.0

    Callback function called: ID = 2
        NAME = Allen
AGE = 25
        ADDRESS = Texas
SALARY = 15000.0

        Callback function called: ID = 3
            NAME = Teddy
AGE = 23
            ADDRESS = Norway
SALARY = 20000.0

            Callback function called: ID = 4
                NAME = Mark
AGE = 25
                ADDRESS = Rich-Mond
SALARY = 65000.0

                Operation done successfully
```

## <font style="color:rgb(51, 51, 51);">Delete 操作</font>
<font style="color:rgb(51, 51, 51);">以下C代码段显示了如何使用DELETE语句删除任何记录，然后从COMPANY表中获取并显示其余记录。</font>

```c
#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h> 

static int callback(void *data, int argc, char **argv, char **azColName) {
    int i;
    fprintf(stderr, "%s: ", (const char*)data);

    for(i = 0; i<argc; i++) {
        printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
    }
    printf("\n");
    return 0;
}

int main(int argc, char* argv[]) {
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    char *sql;
    const char* data = "Callback function called";

    /* 打开数据库 */
    rc = sqlite3_open("test.db", &db);   
    if( rc ) {
        fprintf(stderr, "无法打开数据库: %s\n", sqlite3_errmsg(db));
        return(0);
    } else {
        fprintf(stderr, "已成功打开数据库\n");
    }

    /* 创建合并SQL语句 */
    sql = "DELETE from COMPANY where ID=2; " \
        "SELECT * from COMPANY";

    /* 执行SQL语句 */
    rc = sqlite3_exec(db, sql, callback, (void*)data, &zErrMsg);

    if( rc != SQLITE_OK ) {
        fprintf(stderr, "SQL error: %s\n", zErrMsg);
        sqlite3_free(zErrMsg);
    } else {
        fprintf(stdout, "Operation done successfully\n");
    }
    sqlite3_close(db);
    return 0;
}
```

<font style="color:rgb(51, 51, 51);">编译并执行上述程序后，将产生以下结果。</font>

```c
已成功打开数据库
Callback function called: ID = 1
    NAME = Paul
AGE = 32
    ADDRESS = California
SALARY = 20000.0

    Callback function called: ID = 3
        NAME = Teddy
AGE = 23
        ADDRESS = Norway
SALARY = 20000.0

        Callback function called: ID = 4
            NAME = Mark
AGE = 25
            ADDRESS = Rich-Mond
SALARY = 65000.0

            Operation done successfully
```

