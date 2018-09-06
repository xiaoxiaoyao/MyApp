Sub NewPivotSets()
'
' NewPivotSets 宏
' 业务代码，从原始数据生成数据透视表。
'

' 选中工作表中矩形数据，可以直接这样：
    ActiveSheet.Range("a1", ActiveSheet.Range("a1").End(xlDown).End(xlToRight).Offset(1, 0)).Select
' 新建数据透视表
    ActiveWorkbook.Sheets.Add Before:=Worksheets(Worksheets.Count), Count:=1
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "A:E", Version:=6).CreatePivotTable TableDestination:= _
        "R3C1", TableName:="数据透视_结算", DefaultVersion:=6
' 选中数据透视表
    Cells(3, 1).Select
' 添加行和列
    With ActiveSheet.PivotTables("数据透视_结算").PivotFields("日期")
        .Orientation = xlRowField
        .Position = 1
    End With
' 日期列按月汇总
    Cells(4, 1).Select
    Selection.Group Start:=True, End:=True, Periods:=Array(False, False, False, _
        False, True, False, False)
    With ActiveSheet.PivotTables("数据透视_结算").PivotFields("供应商")
        .Orientation = xlRowField
        .Position = 1
    End With
    With ActiveSheet.PivotTables("数据透视_结算").PivotFields("平台")
        .Orientation = xlRowField
        .Position = 2
    End With
    ActiveSheet.PivotTables("数据透视_结算").AddDataField ActiveSheet.PivotTables( _
        "数据透视_结算").PivotFields("销售金额(点数)"), "求和项:销售金额(点数)", xlSum
    ActiveSheet.PivotTables("数据透视_结算").AddDataField ActiveSheet.PivotTables( _
        "数据透视_结算").PivotFields("折扣(点数)"), "求和项:折扣(点数)", xlSum
' 调整表格显示方式
    ActiveSheet.PivotTables("数据透视_结算").RowAxisLayout xlTabularRow
End Sub
Sub Piv()

  Dim PvTable As PivotTable
  Dim PvField As PivotField
  Dim PvItem As PivotItem

  Set PvTable = ActiveSheet.PivotTables("数据透视_结算")
  Set PvField = PvTable.RowFields(1)

    ReDim dataArray(1 To PvTable.RowFields.Count)
    ReDim dummyArray(1 To PvTable.RowFields(1).PivotItems.Count)

End Sub