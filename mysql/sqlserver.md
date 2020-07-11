# SQL

## 连接数据库

```sql
sqlcmd -S localhost -U SA -P 'Liyuan3970'
```

## 创建新的数据库

```sql
CREATE DATABASE TestDB
SELECT Name from sys.Databases
GO
```
## 插入数据

```sql
USE TestDB

CREATE TABLE Inventory (id INT, name NVARCHAR(50), quantity INT)

INSERT INTO Inventory VALUES (1, 'banana', 150); INSERT INTO Inventory VALUES (2, 'orange', 154);

GO


```

## 退出数据库

```sql

QUIT

```









