Attribute VB_Name = "MOD_1"
Sub A3_filters()

For c = 1 To Worksheets("CP_sheet").UsedRange.Rows.Count
   CP_Name = CStr(Worksheets("CP_sheet").Cells(c, 1).Value)
   Debug.Print CP_Name
        Set sh = Sheets.Add
        With sh
            .Range("a1") = "供应商"
            .Range("a2") = CP_Name
            Sheets("CP_0").UsedRange.AdvancedFilter Action:=xlFilterCopy, _
                CriteriaRange:=.Range("A1:A2"), CopyToRange:=.Range("A3"), Unique:=False
            .Name = CP_Name + "_明细"
            .Rows("1:2").EntireRow.Delete
        End With
        Call SaveSheetAsWorkbook
Next
End Sub

Sub SaveSheetAsWorkbook()
' 将工作簿所有工作表另存为单独的文件。Excel VBA-批量将多个sheet表另存为单独的工作薄文件
    Dim theName As String
    On Error GoTo Line1
    For Each sht In ActiveWindow.SelectedSheets
        sht.Copy
        ' 路径为原工作簿路径，文件名为工作表名
        theName = ThisWorkbook.Path & "_" & sht.Name & ".xls"
        ActiveWorkbook.SaveAs Filename:=theName, FileFormat:=xlNormal
        ActiveWindow.Close
    Next
Line1:
End Sub