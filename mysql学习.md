# mysql学习

`print(hello,world)`

## 创建库

先到对应的目录下，然后cmd--》dir-->cd bin-->mysql -u root -p  -->输入数据库密码(这样就就进入到数据库里面了)-->

导入scott数据库

### 创建 scott 数据库中的 dept 表

```sql
create table dept(
    deptno      int unsigned auto_increment primary key COMMENT '部门编号',
    dname       varchar(15) COMMENT '部门名称',
    loc         varchar(50) COMMENT '部门所在位置'
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='部门表';
```

### 创建 scott 数据库中的 emp 表

```sql
create table emp(
    empno           int unsigned auto_increment primary key COMMENT '雇员编号',
    ename           varchar(15) COMMENT '雇员姓名',
    job             varchar(10) COMMENT '雇员职位',
    mgr             int unsigned COMMENT '雇员对应的领导的编号',
    hiredate        date COMMENT '雇员的雇佣日期',
    sal             decimal(7,2) COMMENT '雇员的基本工资',
    comm            decimal(7,2) COMMENT '奖金',
    deptno          int unsigned COMMENT '所在部门',
    foreign key(deptno) references dept(deptno)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='雇员表';
```

### 创建数据库 scott 中的 salgrade 表，工资等级表

```sql
create table salgrade(
    grade       int unsigned COMMENT '工资等级',
    losal       int unsigned COMMENT '此等级的最低工资',
    hisal       int unsigned COMMENT '此等级的最高工资'  
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='工资等级表';
```

### 创建数据库 scott 的 bonus 表，工资表

```sql
create table bonus(
    ename       varchar(10) COMMENT '雇员姓名',
    job         varchar(9) COMMENT '雇员职位',
    sal         decimal(7,2) COMMENT '雇员工资',
    comm        decimal(7,2) COMMENT '雇员资金'  
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='工资表';
```

### 插入数据库 scott 中表 dept 的初始化数据

```sql
INSERT INTO dept VALUES (10,'ACCOUNTING','NEW YORK');
INSERT INTO dept VALUES (20,'RESEARCH','DALLAS');
INSERT INTO dept VALUES (30,'SALES','CHICAGO');
INSERT INTO dept VALUES (40,'OPERATIONS','BOSTON');
```

### 插入数据库 scott 中表 emp 的初始数据

```sql
INSERT INTO emp VALUES    (7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20);
INSERT INTO emp VALUES    (7499,'ALLEN','SALESMAN',7698,'1981-2-20',1600,300,30);
INSERT INTO emp VALUES    (7521,'WARD','SALESMAN',7698,'1981-2-22',1250,500,30);
INSERT INTO emp VALUES    (7566,'JONES','MANAGER',7839,'1981-4-2',2975,NULL,20);
INSERT INTO emp VALUES    (7654,'MARTIN','SALESMAN',7698,'1981-9-28',1250,1400,30);
INSERT INTO emp VALUES    (7698,'BLAKE','MANAGER',7839,'1981-5-1',2850,NULL,30);
INSERT INTO emp VALUES    (7782,'CLARK','MANAGER',7839,'1981-6-9',2450,NULL,10);
INSERT INTO emp VALUES    (7788,'SCOTT','ANALYST',7566,'87-7-13',3000,NULL,20);
INSERT INTO emp VALUES    (7839,'KING','PRESIDENT',NULL,'1981-11-17',5000,NULL,10);
INSERT INTO emp VALUES    (7844,'TURNER','SALESMAN',7698,'1981-9-8',1500,0,30);
INSERT INTO emp VALUES    (7876,'ADAMS','CLERK',7788,'87-7-13',1100,NULL,20);
INSERT INTO emp VALUES    (7900,'JAMES','CLERK',7698,'1981-12-3',950,NULL,30);
INSERT INTO emp VALUES    (7902,'FORD','ANALYST',7566,'1981-12-3',3000,NULL,20);
INSERT INTO emp VALUES    (7934,'MILLER','CLERK',7782,'1982-1-23',1300,NULL,10);
```

插入数据库 scott 中表 salgrade 的初始数据

```sql
INSERT INTO salgrade VALUES (1,700,1200);
INSERT INTO salgrade VALUES (2,1201,1400);
INSERT INTO salgrade VALUES (3,1401,2000);
INSERT INTO salgrade VALUES (4,2001,3000);
INSERT INTO salgrade VALUES (5,3001,9999);
```

## Mysql数据库

### SQL-DQL语句

#### 格式：

select 列名*N From 表象 Where 查询条件1 and/or 查询条件2 Group by 列 Having 分组条件 Order by 排序

大小写要保持一致。

--这就是注释。

### Select 列和别名

```
--查询所有员工的信息（*通配符，默认查询所有的列）
Select * From emp;
-- 查询员工的姓名
Select ename from emp;
-- 查询员工的姓名和薪资
select ename,sal from emp;
select ename 姓名,sal 薪资 from emp;
select ename sal from emp;        --会把sal当作ename的别名这个东西,不能少
--这个查询出的列可以作一些运算。
select ename,sal * 12 年薪 from emp;
计算年薪时需要加上津贴
select ename,(sal + comm)*12 from emp;    --这个时候有的员工的年薪会是null（有的人没有津贴）。
--拼接
select concat(ename,'的薪资是',sal) from emp;
select concat(ename,'的薪资是',sal) 员工薪资 from emp;
```

### DQL条件查询

如果查询错误，下面会有一个错误编号，直接搜索mysql 错误编号就行了。

#### 普通条件查询

```
--查询指定的列(条件的等值查询)
select * from emp where empno = 7844;
select * from emp where sal = 3000;
select * from emp where job = SALESMAN  --因为没有加""所以被当成列了推荐使用单引号
--
select * from emp where sal > 1000;
select * from emp where sal < 1000;
select * from emp where job != 'SALESMAN';   --不等于也可以写成<>
select * from emp where sal between 1600 and 3000;   --这个包含两边的
```

#### in在某个范围内查询

```
select * from emp where empno in (7499,7566,7698);
select * from emp where empno not in (7499,7566,7698);
```

#### null值查询

```
select * from emp where comm is null;
select * from emp where comm is not null;
```

上面这些都是入门级查询

#### like模糊查询

```sql
--里面有M，%代表任意字符的任意次
select * from emp where ename like '%N';
select * from emp where ename like 'M%';
select * from emp where ename like '%M%';    --这个语句可以多理解
--下划线代表任意字符的一次
select * from emp where ename like '_M%';
--查询里面带%的数据，需要用\才能查询出来
update emp set ename = 'JAM%ES' where empno = 7900;
select * from emp where ename like '%\%%';
```

普通文本用模糊查询，复杂的文本需要用专门的文本的检索工具（分布式检索的工具ES），查询不连续的明月两字的古诗，这个时候怎么查询（京东查询iphone 小火车）

#### 多条件查询连接查询（多个不同的条件）

```sql
select * from emp ename = 'SMITH' or empno = 7900;
select * from emp deptno = 10 and sal > 2000;
```

#### 结果排序

DQL之查询结果排序视频在P11节

一般情况下数据是以主键进行排序的。

如果是名字的话，有可能是按字典进行排序。默认是

```sql
select * from emp order by sal;
select * from emp order by job;
select * from emp order by hiredate;
--查看每个工作下的最高薪资、最低
select * from emp order by job,sal;
--下面这样也行，虽然有的排序字段不在要搜索范围内，下面的1,2不怎么推荐
select ename,sal from emp order by job,sal;
select ename,sal from emp order by 1;  --这个的意思是以要搜索的第一列进行排序
select ename,sal from emp order by 2;  --同上是以第二列进行排序。
select ename,sal from emp order by 3;  --会报错，可以用错误代码搜索下看看
select ename,sal from emp order by job,sal desc;
```

#### DQL之分页查询

```Mysql
select ename from emp limit 3;        --每次查询第n行
--分别查询第N页，每页显示M个
select * from emp limit 1,3;        --从第一行开始数，数出三个记录。
select * from emp limit 0,3; 
select * from emp limit 3,3;
select * from emp limit 6,3;        --以3每页，找第3页
select * from emp limit (n-1)*M,M; 
--查询薪资大于1000的前五条记录,逆序排列显示前五列。
select * from emp where sal>1000 limit 5;
select * from emp where sal>1000 order by sal desc limit 5;
```

## 函数介绍

比如查询一个字符串第八个字符必须是a。如果第88个字符是a？将部分字段数据为null直接转为0.日期转为年月日。这就涉及到了函数

### 单行函数、多行函数

单行函数：指的是操作一行数据返回一行数据，操作10行数据就返回10行数据。集中于字符串、日期、数字、转换、其他函数。

```sql
select lower(ename),length(ename),lpad(ename,8,'#'),rpad(ename,8,'#'),replace(ename,'S','@'),substr(ename,1,3) from emp 
where substr(ename,2,1) = 'A';
```

例如：给10个员工加1000元薪资，这10个全部要加一遍。

多行函数：最高分、最低分。进去n行返回一行,又叫分组函数。分组后就可能有多个情况。

### 字符串函数

### 伪表dual

```sql
seect 9+2 from dual;
select abs(-10) from dual;        --abs取绝对值
select ceil(3.2) ,floor(3.6) from dual;        --ceil向上取整,floor向下取整
select power(2,3) from dual;        --取2的3次方
select round(3.2),round(3.8),round(3.0) from dual;    --四舍五入
select hiredate,now() from emp;        --获取当时系统时间now()
--取出指定时间的月、天、年等.
select hiredate,extract(month from hiredate) from emp;
select extract(second from now()) from dual;  --可以
--获取当前日期、当前时间、当前详细时间
select hiredate,current_date(),current_time(),current_timestamp() from emp;
--获取指定格式的日期
select hiredate,date_format(hiredate,'%Y-%M-%D') from emp;
select hiredate,date_format(hiredate,'%Y-%m-%d') from emp;
select hiredate,date_format(hiredate,'%Y年%m月%d日') from emp;
select hiredate,date_format(now(),'%Y年%m月%d日 %H-%m-%s') from emp;
--某个日期加减几天
select hiredate,adddate(hiredate,9),adddate(hiredate,-9) from emp;
--返回一个月的最后select hiredate,adddate(hiredate,9) from emp;select last_day(hiredate) from emp;
```

现在学习到了P17节

### 其它函数--空值处理、加密

```sql
--空值处理
select sal + comm from emp;
select sal + ifnull(comm,0) from emp;
select sal + ifnull(comm,1000) from emp;
--加密处理，md5只能加密，不能解密,md5为不可逆加密（判断加密后的信息即可），还有对称加密，非对称加密。加严可以从账号里面取几位联接密码一起进行加密
select MD5("hello") from dual;
```

不可逆：1+4			15= x +y    

### 单选函数之转换函数

字符串、日期、数字三种之间的转换。推荐以字符串为中转，进行互转。

```sql
--日期==〉字符串
select date_formate
--字符串==〉日期
select STR_TO_DATE('10月2012年11日','%m月%Y年%d日');
--数字到字符串，直接拼接一个字符串即可，可以自动转化。
select lpad(123,10,'$');
select '123' + 456;
select concat('123',456);
```

### 常用的五个多行函数

max、min、avg、sum（如果求和过程中有Null,那么不会计算在内）、count（如果统计的数据中有null，不会把Null统计在内）。

```sql
--查看入职时间最长的职工,注意这个区别。这个sum与Count对Null区别对待。Sum对数字使用，对字符串不生效。
select max(sal),min(sal),sum(sal),count(job),avg(sal) from emp;
select min(hiredate) from emp;
select min(hiredate),max(ename),min(ename),sum(comm),count(comm),avg(comm) from emp;
--查询薪资最低的员工。
select min(sal) ,ename from emp;
select max(sal),ename from emp;
select ename from emp where sal = min(sal);
select ename,sal from emp order by sal desc limit 1;
--查询每个部门的最高薪资，用分组函数，谁的薪资高于所在部门的平均薪资
```

组合函数是不能和单列放在一起，分组的列是可以放在一起的,虽然Mysql语法不会报错，但是结果是错误的。

### 数据分组group +having

[其他人的理解](https://blog.csdn.net/weixin_53908084/article/details/124565198?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168596961716800186533347%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=168596961716800186533347&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-1-124565198-null-null.142^v88^control_2,239^v2^insert_chatgpt&utm_term=%E5%88%86%E7%BB%84%E5%87%BD%E6%95%B0&spm=1018.2226.3001.4187)

按照某一个条件进行分组，第一组返回对应的结果。

Group By可以对指定的列进行分组，列尽量有相同的，普通列不能和分组的列放在一起。

Having可以对分组之后的数据进行过滤，所以能出现在Having中的比较项一定是被分组的列或组函数

### 底层

1. Where是称之为行过滤，处理的是表中第一行数据的过滤
2. Having称之为级级过滤，处理的是分组之后的第一组数据
3. 能使用Where的，尽量不要使用Having

有几组对应几个结果。

```sql
--求每个工种最高薪资
select job ,max(sal) from emp group by job;
--求部门里面的最高薪资是多少。下面第一个里面的Ename是每组里面的第一个人不是想像里面的最高的人
select deptno ,min(sal) ,ename from emp group by deptno;
select * from emp;
--求每个部门的平均薪资
select avg(sal) from emp group by deptno;
--求每个部门3000元以下的平均薪资
select avg(sal) from emp where sal <3000 group by deptno;
select deptno,avg(sal) from emp where sal <3000 group by deptno order by deptno;
--查询平均薪资大于1800的部门，下面第一个报错原因是在分组前使用了avg（sal）〉1000,注意执行的顺序，sal〉1000是普通的比较在Where里面用，而avg是分组函数，它必须在分组之后用
select deptno from emp where avg(sal) >1800 group by deptno;
select deptno,avg(sal) from emp group by deptno having avg(sal) >1000;
select deptno,avg(sal) from emp sal<3000 group by deptno having avg(sal) >1000;
--查询哪个部门每个月的津贴总数超过1000;
select deptno from emp group by deptno having sum(comm) > 800;
select deptno,sum(comm) from emp where comm is not null group by deptno having sum(comm) > 1000;--Where是单行过滤，Having对分组之后的数据进行过滤
--查询20、30部门的平均薪资.能用Where就不用Having。Where是行级过滤
select avg(sal),deptno from emp where deptno in (20,30) group by deptno ;--先过滤完行，再进行分组过滤，
select avg(sal),deptno from emp group by deptno having deptno in (20,30);--先进行分组，后进行过滤。如果数据比较多有上百万，差距就大了。
--查询每个部门中名字带有a的员工平均薪资.能不能将Where里面的条件放在Having里面。
select deptno,avg(sal) from emp where ename like "%a%" group by deptno;
select deptno,avg(sal) from emp group by deptno having ename like "%a%";
--每个小组中男生、女生最高分是多少（这是两次分组）。查询10,20部门中，并且在二月份入职员工中，每个部门中平均薪资高于1500的工作是什么，并按照部门、工作平均薪资进行排序(第四个才是正确答案，11月份有搜索结果)。
select deptno,job,avg(sal) from emp where deptno in (20,10) and extract(month from hiredate) = '02' group by deptno having avg(sal) >1500 order by deptno,avg(sal);
select * from emp;
select deptno,job,avg(sal) from emp where deptno in (20,10) and extract(month from hiredate) = 2 group by deptno having avg(sal) >1500 order by deptno,avg(sal);
select deptno,job,avg(sal) from emp where deptno in (20,10) and extract(month from hiredate) = 2 group by deptno,job having avg(sal) >1500 order by deptno,avg(sal);
```

### DQL单表关键字执行顺序

Select：我们要显示哪些列的数据

From：从哪张表中获取数据

Where：从表中获取数据的时候进行行级的数据过滤

Group by：对数据进行分组处理，一组获取对应的结果 

Having：组级过滤，组级过滤的数据必须是分组条件或者是组函数

Order by：排序、asc、desc

执行顺序：from-->where-->group by-->having-->select--> order by

基本就是两张或者三张表进行多表查询

### 多表查询 

查询的时候如果出现相同名的列，我们需要将表名标注到列名前面

- 如果是非同名的列，表名可加可不加，推荐加上。
- 为了书写方便，可以给表添加别名
- 一般情况下取首字母，特殊情况下取它所代表的含义
- 表的别名只在本次查询中生效

如果表与表进行查询的时候，如果不添加关联条件，查询的总记录数是a*b = 笛卡尔积

- a 15 b 10 c 10 -->1500条

### 多表查询的时候必须加上条件

- 等值
- 非等值

```sql
select * from emp,dept where dept.deptno = emp.deptno;
select * from emp e ,dept d where e.deptno = d.deptno ;
--查询某个员工的薪资等级,非等值查询
select * from emp e ,salgrade s where e.sal between s.losal and s.hisal;
--薪资大于2000员工的办公地址
select d.loc,e.ename from dept d,emp e where d.deptno = e.deptno and e.sal >2000 ;
```

工作中推荐使用99语法。少用92语法。

### 表与表的关联方式

因为表的关联条件和业务查询条件放在一起，为了防止混淆于是提供了下面三种方式

### 自然连接

- 会自动选择列名相同并且类型相同的列

  ```sql
  --查询薪资大于2000的员工姓名和部门名称
  select e.ename,d.dname from emp e,dept d where e.deptno = d.deptno and e.sal>2000;
  --自然连接(前提：列名相同且类型相同)
  select e.ename,d.dname from emp e natural join dept d;
  select e.ename,d.dname from emp e natural join dept d where e.sal>2000;
  ```

  

### Using		

这种用的比较多，用于等值关联

不需要Mysql帮我们选择等值连接的列，现在我们指定等值连接的列

```sql
select * from emp join dept using(deptno) where sal >2000;
```

### On		

我们可以指定两张表关联的条件，可以是非等值的操作

```sql
select  * from emp e join salgrade s on(e.sal between s.losal and hisal);
select * from emp e join dept d on(e.deptno = d.deptno);
```

### 三张表查询

（连接三张表最少需要二个条件，少一个会产生许多数据笛卡尔积）

```sql
--查询员工的部门名称和薪资等级.两张表用Join关联的时候一定要想到有一张大表.三张表连接的过程一定要想清楚
select * from emp e join dept d using(deptno);
select * from emp e join dept d using(deptno) join salgrade s on (e.sal between s.losal and s.hisal);
select e.ename,d.dname,s.grade from emp e join dept d using(deptno) join salgrade s on (e.sal between s.losal and s.hisal);
```

92语法与99语法的区别：表连接条件与查询条件是否连接在一起。

左右外连接99语法。外连接不符合查询条件的也显示出来

当我们对两张表进行关联查询的时候，基于数据的原因导致其中一张表中的数据没有办法完全查询出来。

外连接可以让没查询出来的数据也显示出来 

因为我们写SQL有左右之分，外连接也有：

左外连接，显示左面表所有的数据

右外连接，显示右面表所有的数据

```sql
--查询每个员工对应的部门。有一个员工没有部门，但是下面第一句没有显示出来（原因是大表中对应的deptno为Null）
select e.ename,d.dname from emp e join dept d using(deptno) ;  --有一个没有部门的员工没有查到，他属于员工表
select e.ename,d.dname from emp e left join dept d using(deptno);
--查询每个部门中有多少员工
select count(d.dname) from emp e join dept d using(deptno) group by d.dname;
select deptno,count(*) from emp group by deptno;
--查询部门名称和每个部门分别有多少员工
select d.deptno,d.dname,count(e.empno) from emp e join dept d using(deptno) group by d.deptno,d.dname;-- 40部门没有出现
select d.deptno,d.dname,count(e.empno) from emp e right join dept d using(deptno) group by d.deptno,d.dname;
```

DQL之Union与全外连接

Union的作用是拼接，下面的视图会用到。多个条件在一起就用Union（将查询的结果进行一次累加，）

```sql
--查询员工姓名、薪资，在部门1，并且名字中含有字母A的员工和部门2薪资大于1000的员工，和部门3薪资小于2000的员工（下面可能有多个条件）
select ename,sal,deptno from emp where deptno = 10 and ename like '%A%'
select ename,sal,deptno from emp where deptno = 20 and sal >1000
select ename,sal,deptno from emp where deptno = 30 and sal <2000
select ename,sal,deptno from emp where deptno = 10 and ename like '%A%'
union
select ename,sal,deptno from emp where deptno = 20 and sal >1000
union
select ename,sal,deptno from emp where deptno = 30 and sal <2000;
--查询员工姓名、薪资，名字中含有字母A的员工和部门2薪资大于1000的员工，和部门3薪资小于2000的员工，这个可能有重复的数据（因为部门2、部门3中也可能有含有字母A的员工，有Union会自动去重，如果不想要这个效果就用Union all直接累加）Union的效率高
select ename,sal,deptno from emp where  ename like '%A%'
union
select ename,sal,deptno from emp where deptno = 20 and sal >1000
union
select ename,sal,deptno from emp where deptno = 30 and sal <2000;
--查询所有不符合连接条件的员工各有和部门名称
select e.ename,d.dname from emp e left join dept d using(deptno)
union
select e.ename,d.dname from emp e right join dept d using(deptno);
```

表与表的自连接

我们要查询的两个字段同时处于一张表上，我们只能将一张表当做含有不同意义的两张表去处理

给相同的表取不同的的简称（按照所代表的含义去取）

```sql
--查询当前员工及对应主管的名称
select empno,mgr from emp ;
select e.empno,e.ename,m.empno,m.ename from emp e join emp m on(e.mgr = m.empno);
```

表与表的子连接

把一个SQL语句的查询结果当成另一个的查询条件

```sql
--查询谁的工资比公司的平均工资高（Where行级过滤，avg组级过滤，根本就没有到组级这一步）
select  deptno from emp where sal > avg(sal);
select avg(sal) from emp;
select  deptno from emp where sal >(select avg(sal) from emp);
--查询谁的薪资低于30部门所有人的薪资(二个思路：1找出20里面的最低薪资，)，上面的子查询只返回一条记录，下面第二个返回多条记录，第三个子查询有all就是小于所有
select sal from emp where deptno = 30;
select empno,ename from emp where sal < (select sal from emp where deptno = 30);
select empno,ename from emp where sal < all(select sal from emp where deptno = 30);
select empno,ename,sal from emp where sal < any(select sal from emp where deptno = 30);  --大于或小于其中的一部分即可
--查询公司中薪资最低的员工姓名
select ename,sal from emp where sal =(select min(sal) from emp);
--谁的薪资高于20部门员工的薪资(in与之前使用的一样)
select ename,sal from emp where sal> all(select sal from emp where deptno = 20);
select ename,sal from emp where sal >some(select sal from emp where deptno =20);
select ename,sal from emp where sal in(select sal from emp where deptno = 20);
```

表与表的伪表查询

如果我们所需要的查询条件需要别的SQL语句提供

如果只需要一个条件，那么可以使用子查询来完成

如果需要多个查询条件，这是就要将所有的查询结果当做伪表进行管理

我们需要把一些含有特殊符号的列名设置别名，然后给伪表设置一个别名（见名知意）

```sql
--查询员工信息	高于自己部门平均薪资的员工。子查询只能用于一个列（返回结果列）
select deptno,ename,sal from emp where sal > (select avg(sal) from emp where deptno = 10)
union
select deptno,ename,sal from emp where sal > (select avg(sal) from emp where deptno = 20)
union
select deptno,ename,sal from emp where sal > (select avg(sal) from emp where deptno = 30);
select   * from emp where sal < some(select deptno,avg(sal) from emp group by deptno)		--这里面子连接有两个列，而前面只能同时比较一个列，这个时候应用伪表查询
select * from emp e join (select deptno,avg(sal) avgsal from emp group by deptno) da;
select * from emp e join (select deptno,avg(sal) avgsal from emp group by deptno) da on(e.deptno = da.deptno and e.sal > da.avgsal) order by e.deptno;
```

现在时间2022-10-30  am11：08	P29

增删改（DML）难在事务上面。DQL（查）

SQL-DML插入

Insert Into 表名 Values（）;	如果不写列就按照默认的列进行插入。如果写了列，就按照写的列进行插入。如果有上百个列，就用自动生成

insert into dept values(50,'sxt','shanghai');

要求插入的数据的数量、类型要和定义的表结构一致。后面带select的可以在倒库的时候用比较方便。

```sql
insert into dept values(50,'sxt','shanghai','liyi');
insert into dept values(50,'sxt');
insert into dept values('abcd',50,'sh');
select * from dept where 1<>1;这个查询不到数据， 1<>1是一个错误的
create table dp as select * from dept where 1<>1;  --创建表结构且表结构后后面的表一致，不插入数据
insert into dp select * from dept;   --将别的表中的数据插入到这个表中
insert into dp select empno,ename,job from emp ;   --这个也插入进去了，前提是这个表的结构要与后面一致。
select  * from dept where deptno = 20 or 1 = 1; --这个所有的数据都会查询出来
insert into dp values (80,'guoliping','faliao'),(90,'zhengweidong','zhongruan'),(100,'huangfei','zhongruanguoji');--这个可以插入多条数据。
```

DML删除，工作中删除有风险，一定要谨慎，删库到跑路。

物理删除：就是右键直接删除。逻辑删除：就是有一个列为0,1.0就是无效的，1是有效的可以使用的。

delete from 表名。

delete from 表名 where 条件

上面就是物理删除，删除完之后理论上不能再找回。

```sql
delete from emp;  --这个是删除整个表，尽量用where限制范围
delete from emp where sal >3000;   --这个Orrql里面好像是可以进行找回的，紧急联系网管，所有人不要再操作电脑了。被删除的数据在临时表空间。
truncate table emp;		--这个是截断表，相当于把之前的表给删除了，重新创建一张新表，所有的薄东西都没有了，无法恢复。上面这两种只针对数据。如果删除表，就用Drop
drop table dp;
```

修改，可以一次性修改多个列，用,隔开即可

```sql
update emp set sal = sal +1000;		--这个是全部修改
update emp set sal = sal +1000 where deptno = 10;    --修改指定范围内的员工的工资
update emp set sal = sal +1000 ,comm = comm+200 where deptno = 10;
```

DML之事务P32

事务：程序在执行过程中的一个逻辑单元（要么同时成功，要么同时失效）。在表中的【开始事务】里面的【提交】与【回滚】。没有开启事务，直接修改后就生效了。开启【开户事务】后，修改完成后，点击提交才算成功，点击回溯就回到原始状态。

```
update emp set ename = 'zhangsan' where empno = 7369;
--如何让SQL语句执行完成下面第一个后就执行第二个，属于同一个事务？
update emp set sal = sal -500 where empno = 7369;
update emp set sal = sal +500 where empno = 7369;
```

数据库管理系统执行过程中的一个逻辑单元，由一个有限的数据库操作序列构成。

事务指的是数据库一种保护数据的方式。

事务一般由增删改操作自动调用，事务根据数据库不同提交的时机也是不同的。

Mysql数据库默认执行增删改就会提交事务

我们可以设置为手动提交begin或者start transaction;

事务原则：

- ACID原则

- 原子性

  事务是操作数据的最小单元，不可以再分

- 一致性

  事务提交之后，整个数据库所看到的数据都是最新的的数据

  所有人看到的数据都是一致的

- 隔离性

  别人无法访问到我们未提交的数据，而且一旦这个数据被我修改，别人也无法进行操作

- 持久性

  事务一旦被提交，数据库就进入一个全新的状态

  数据在也不能返回到上一个状态。

  

事务如何开启和提交？

- 开启

  当我们执行增删改操作的时候就会默认开启一个事务

  这个事务和当前操作的窗口有关，别人是无法共享这个事务的

SQL-DDL（数据库定义语言，定义表的结构、视图、索引）

常见的组成：

​	库的操作--表--视图--存储过程--事件--索引

### 数据库的操作

```sql
--数据库的创建
create database 数据库名 charset utf8;
--查看数据库
show databases;
show create database db;
select database();
--选择数据库
user 数据库名
--删除数据库
drop database 数据库名;
-修改数据库
alter database db1 charset utf8;
```

### DDL之数据类型

字符串类型里面的char是定长的（已知字段的长度，例如：性别），varchar(变长的，用多少声明多少)

### 数据库表table的创建

```sql
--我们首先要对要操作的数据有一个基础型的了解
--创建学生表。学号、姓名、性别、年龄、分数、班级、专业、院系。学号是唯一的，姓名不是唯一的，年龄是可变的，一般是不填的，可以为出生日期，分数一般在分数表中（一个学生可能有多个分数）。班级一般一年变一次。一般填写不怎么变的，可以推出其它的。（学号、姓名、性别、出生日期、入学时间、专业、院系）
--学号Int、姓名varchar、性别char、出生日期date、入学时间date、专业varchar(字典表)、院系varchar，创建时间 timestamp.t_studetn(表示是一张学生表)tbl(table的缩写).一个汉字两个字节。varchar默认是255
create table t_student(
	sno int,
    sname varchar(255),
    gender char(1),
    birthday date,
    shcooltime date,
    major varchar(255),
    department varchar(255),
    createtime timestamp
)
```

上面的创建表sql没有进行约束

### 表的结构进行修改

1直接在navicate里面对应表--设计表里面进行修改（这样有瑕疵，有可能连不到navicate）

2用Sql语句

```sql
--根据查询语句创建表
create table stu01 as select * from student;
--添加一列
alter table student add birthday date default sysdate;
--删除一列
alter table student drop column email;
--修改一列
alter table student modify major varchar(20);
--修改列名
alter table student rename column birthday to birth;
--修改表名
alter table student to t_s;
--删除一张表
drop table t_s;
```

### DDL主键约束

#### 表table的约束

约束指的是我们创建的表 别人在插入数据的时候，对数据的约束，而不是对创建人的约束。

主键约束 PRIMARY KEY

- 主键值必须唯一标识表中的每一行，且不能为null，即表中不可能存在有相同的主键值的两行数据。
- 主键分为单字段主键和多字段主键
- 联合主键不能包含不必要的多余字段。当把联合主键的某一字段删除后，如果剩下的字段构成的主键仍然满足唯一性原则，那么这个联合主键是不正确的，这是最小化原则。

```mysql
create table t_pk01(
id int(11) PRIMARY KEY,
name varchar(25),
deptId int(11),
salary FLOAT
);
create table t_pk03(
tid int(11),
cid int(11),
salary float,
PRIMARY KEY(tid,cid)
);
create table t_pk02(
id varchar(40),
name varchar(25),
    salary float
);
#添加主键的sql语句
--Alter table <数据表名> add PRIMARY KEY<字段名>
alter table t_pk02 add PRIMARY KEY(id);
  --Alter table  <数据表名> drop PRIMARY KEY<字段名>
  alter table t_pk02 drop PRIMARY KEY;
select UUID();   --这个会查询到一个十六进制的数字,理论上是不会重复的.
INSERT INTO t_pk02 values (rand(),'zs',88);
insert into t_pk02 values (UUID(),'ls',78);
```

在设计表中可以看到加了金钥匙的就是主键。

t_pk03就是联合主键(不能其中一个为空)。还可以设置自增主键直接在设计表里面选择自动递增就行了。

如何给没有主键的表用sql添加主键，

函数rand(),效果对应随机数

### 单表查询练习

```sql
--01找出各月倒数第3天受雇的所有员工
--02找出早于12年前受雇的员工
--03以首字母大写的方式显示所有员工的姓名
--04显示正好为5个字符的员工的姓名
--05显示不带有“R”的员工的姓名
--06显示所有员工姓名的前三个字符
--07显示所有员工的姓名，用a替换所有的A
--08显示满10服务年限的员工的姓名和受雇日期
--09显示员工的详细资料，按姓名排序
--10显示员工的姓名和受雇日期，根据其服务年限，将最老的员工排在最前面
--11显示所有员工的姓名、工作和薪金，按工作的降序排序，若工作相同则按薪金排序
--12显示所有员工的姓名、加入公司的年份和月份，按受雇日期所在月排序，若月份相同则将最早年份的员工排在最前面
--13找出在（任何年份的）2月份受聘的所有员工
--14对于每个员工，显示所有其加入公司的天数
--15显示姓名字段的任何位置包含“A“的所有员工的姓名
```

### 多表查询

```sql
--01列出至少三个员工的所有部门
--02列出薪金比“SMITH”多的所有员工。（大于最大薪水SMITH员工）
--03列出所有员工的姓名及其直接上级的姓名
--04列出受雇日期早于其直接上级的所有员工
--05列出部门名称和这些部门的员工信息，包括那些没有员工的部门
--06列出所有job为“CLERK”（办事员）的姓名及其部门名称
--07列出最低薪金大于1500的各种工作
--08列出在部门“SALES”（销售部）工作的员工的姓名，假定不知道销售部的部门编号
--09列出薪金高于公司平均薪金的所有员工
--10列出与“SCOTT”从事相同工作的所有员工
--11列出薪金等于部门30中员工的薪金的所有员工的姓名和薪金
--12列出薪金高于在部门30中员工的薪金的所有员工的姓名和薪金
--13列出在每个部门工作的员工数量、平均工资和平均服务期限
--14列出所有员工的姓名、部门名称、和工资
--15列出从事同一种工作但属于不同部门的员工的一种组合
--16列出所有部门的详细信息和部门人数
--17列出各种工作的最低工资
--18列出各个部门的MANGER（经理）的最低薪金（）
--19列出所有员工的年工资，按年薪从低到高排序
--20列出所有job为‘CLERk‘的员工平均薪资
--21列出job为CLerk员工的平均薪资，按照部门分组
--22列出job为Clerk员工的平均薪资，按照部门分组，并且部门编号在10,30,按照平均薪资降序排列
--23列出job为Clerk员工的平均薪资，按照部门分组并且部门编号在20,30并且部门员工数量需要大于或等于2人，按照平均薪资降序排列
```

关于学生

```sql
--1.查询选修课程‘3-105’且成绩在60到80之间的所有记录
--2.查询成绩为85、86、或88的记录
--3.查询‘95031’班的学生人数
--4.查询最低分大于70,且最高分小于90的学号列
--5.查询至少有5名学生选修并以3开头的课程平均成绩
--6.查询平均分大于80分的学生成绩表
--7.查询‘95033’班每个学生所选课程的平均分
--8.以选修‘3-105’为例，查询成绩高于‘109’号同学的所有同学的记录
--9.查询与学号为108的同学同岁的所有同学的学号、姓名和年龄
--10.查询每个老师授课不及格学生名单
--11.查询所有学生的平均成绩
--12.查询每个课程的最高分、显示课程名字和学生姓名和分数
--13.查询每个学生的授课老师
--14.查询每个班级的及格率
```

