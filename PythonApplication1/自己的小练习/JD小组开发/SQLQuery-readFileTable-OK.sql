--读取数据库需要用额外组件，必须更改配置才可以，选项属于系统的高级选项，执行以下代码，允许用户修改高级选项：
EXEC sp_configure 'show advanced options', 1  --更改配置
GO
RECONFIGURE       --安装
GO
EXEC sp_configure 'Ad Hoc Distributed Queries', 1
GO
RECONFIGURE
GO
-- 使用以下代码启用xp_cmdshell选项（高危，执行后请立即关闭xp_cmdshell选项，小尧注）：
exec sp_configure 'xp_cmdshell', 1; 
go 
reconfigure; 
go

---读取目录下所有文件名，存入临时表#t
IF object_id('tempdb..#t', 'u') IS NOT NULL
    DROP TABLE #t
GO
create table #t(b varchar(254))
insert into #t
EXEC master.dbo.xp_cmdshell 'dir/b D:\test'

---遍历目录下文件
declare @name varchar(254)
declare @query varchar(1000)
DECLARE My_Cursor CURSOR --定义游标
FOR SELECT * FROM #t --查出需要的集合放到游标中
OPEN My_Cursor; --打开游标
FETCH NEXT FROM My_Cursor INTO @name ; --读取第一行数据
WHILE @@FETCH_STATUS = 0
    BEGIN
		print '\
		
		
		正在读取文件' + @name
		BEGIN TRY
		set @query='Insert into [' + @name + '] select * from OPENROWSET(''Microsoft.ACE.OLEDB.12.0'',''Excel 5.0;HDR=NO;IMEX=1;DATABASE=D:\test\' + @name + ''',sheet1$)'
		exec (@query)
		END TRY
		BEGIN CATCH
		set @query='Insert into [' + @name + '] select * from OPENROWSET(''Microsoft.ACE.OLEDB.12.0'',''Text;HDR=NO;DATABASE=D:\test;Extensions=csv,txt;'',''SELECT * FROM [' + @name + ']'')'
				exec (@query)
		END CATCH
		print '执行SQL代码：' + @query

		print '读取文件完毕' + @name
        FETCH NEXT FROM My_Cursor INTO @name ; --读取下一行数据
    END
CLOSE My_Cursor; --关闭游标
DEALLOCATE My_Cursor; --释放游标


---扫尾
IF object_id('tempdb..#t', 'u') IS NOT NULL
    DROP TABLE #t
GO
-- 使用以下代码禁用xp_cmdshell选项：
exec sp_configure 'xp_cmdshell', 0; 
go 
reconfigure; 
go
