Attribute VB_Name = "MOD_1"
Sub A1_NewPivotSets()
'
' NewPivotSets 宏
' 业务代码，从原始数据生成数据透视表。
'
Set sh = Sheets.Add
With sh
.Name = "汇总_透视"
End With
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "A:L", Version:=6).CreatePivotTable TableDestination:= _
        "R3C1", TableName:="给客户的明细数据透视表", DefaultVersion:=6
    Cells(3, 1).Select
    With ActiveSheet.PivotTables("给客户的明细数据透视表").PivotFields("日期")
        .Orientation = xlRowField
        .Position = 1
    End With
    With ActiveSheet.PivotTables("给客户的明细数据透视表").PivotFields("版本")
        .Orientation = xlRowField
        .Position = 1
    End With
    With ActiveSheet.PivotTables("给客户的明细数据透视表").PivotFields("供应商")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("给客户的明细数据透视表").AddDataField ActiveSheet.PivotTables("给客户的明细数据透视表" _
        ).PivotFields("结算金额"), "收入额", xlSum
    ActiveSheet.PivotTables("给客户的明细数据透视表").AddDataField ActiveSheet.PivotTables("给客户的明细数据透视表" _
        ).PivotFields("结算分成额"), "结算分成", xlSum
    Range("A6").Select
    ActiveSheet.PivotTables("给客户的明细数据透视表").PivotFields("日期").Subtotals = Array(False, _
        False, False, False, False, False, False, False, False, False, False, False)
        ' 调整表格显示方式
    ActiveSheet.PivotTables("给客户的明细数据透视表").RowAxisLayout xlTabularRow
    ActiveSheet.PivotTables("给客户的明细数据透视表").RepeatAllLabels xlRepeatLabels
End Sub