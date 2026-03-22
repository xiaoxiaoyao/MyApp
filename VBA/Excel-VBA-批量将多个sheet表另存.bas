Attribute VB_Name = "MOD_1"
Sub SaveSheetAsWorkbook()
' �����������й��������Ϊ�������ļ���Excel VBA-���������sheet�����Ϊ�����Ĺ������ļ�
    Dim theName As String
    On Error GoTo Line1
    For Each sht In ActiveWindow.SelectedSheets
        sht.Copy
        ' ·��Ϊԭ������·�����ļ���Ϊ��������
        theName = ThisWorkbook.Path & "_" & sht.Name & ".xls"
        ActiveWorkbook.SaveAs Filename:=theName, FileFormat:=xlNormal
        ActiveWindow.Close
    Next
Line1:
End Sub
