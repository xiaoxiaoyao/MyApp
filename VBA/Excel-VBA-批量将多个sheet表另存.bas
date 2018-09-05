Attribute VB_Name = "MOD1"
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
