Attribute VB_Name = "MOD_1"
'==============================================================================
' 模块名称: MOD_1
' 功能描述: Excel VBA 创建数据透视表
' 作者: 小尧
' 创建日期: 2024-01-01
' 版本: 1.0
'==============================================================================

'------------------------------------------------------------------------------
' 过程名称: A1_NewPivotSets
' 功能描述: 从原始数据创建数据透视表，按日期、版本、供应商分组，
'           汇总结算金额和结算分成额
' 参数说明: 无
' 返回值: 无
' 前置条件:
'   - 活动工作表中 A:L 列包含原始数据
'   - 数据必须包含"日期"、"版本"、"供应商"、"结算金额"、"结算分成额"等字段
' 数据透视表配置:
'   - 行字段: 日期、版本、供应商
'   - 数据字段: 收入额(结算金额求和)、结算分成(结算分成额求和)
'   - 显示方式: 表格形式，重复显示标签
'------------------------------------------------------------------------------
Sub A1_NewPivotSets()
    ' 创建新工作表用于存放数据透视表
    Set sh = Sheets.Add
    With sh
        .Name = "汇总_透视"
    End With
    
    ' 创建数据透视表缓存和透视表
    ' SourceType:=xlDatabase - 数据源类型为 Excel 数据库
    ' SourceData:="A:L" - 数据源范围为 A 到 L 列
    ' TableDestination:="R3C1" - 透视表放置在第3行第1列（即A3单元格）
    ' TableName:="给客户的明细数据透视表" - 透视表名称
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "A:L", Version:=6).CreatePivotTable TableDestination:= _
        "R3C1", TableName:="给客户的明细数据透视表", DefaultVersion:=6
    
    ' 选中透视表起始单元格
    Cells(3, 1).Select
    
    ' 配置"日期"字段为行字段
    With ActiveSheet.PivotTables("给客户的明细数据透视表").PivotFields("日期")
        .Orientation = xlRowField
        .Position = 1
    End With
    
    ' 配置"版本"字段为行字段
    With ActiveSheet.PivotTables("给客户的明细数据透视表").PivotFields("版本")
        .Orientation = xlRowField
        .Position = 1
    End With
    
    ' 配置"供应商"字段为行字段
    With ActiveSheet.PivotTables("给客户的明细数据透视表").PivotFields("供应商")
        .Orientation = xlRowField
        .Position = 1
    End With
    
    ' 添加"结算金额"字段到数据区域，汇总方式为求和，显示名称为"收入额"
    ActiveSheet.PivotTables("给客户的明细数据透视表").AddDataField ActiveSheet.PivotTables("给客户的明细数据透视表" _
        ).PivotFields("结算金额"), "收入额", xlSum
    
    ' 添加"结算分成额"字段到数据区域，汇总方式为求和，显示名称为"结算分成"
    ActiveSheet.PivotTables("给客户的明细数据透视表").AddDataField ActiveSheet.PivotTables("给客户的明细数据透视表" _
        ).PivotFields("结算分成额"), "结算分成", xlSum
    
    ' 选中 A6 单元格
    Range("A6").Select
    
    ' 关闭"日期"字段的小计显示
    ActiveSheet.PivotTables("给客户的明细数据透视表").PivotFields("日期").Subtotals = Array(False, _
        False, False, False, False, False, False, False, False, False, False, False)
    
    ' 调整透视表显示方式为表格形式
    ActiveSheet.PivotTables("给客户的明细数据透视表").RowAxisLayout xlTabularRow
    
    ' 设置重复显示标签（使每个行字段值都显示）
    ActiveSheet.PivotTables("给客户的明细数据透视表").RepeatAllLabels xlRepeatLabels
End Sub
