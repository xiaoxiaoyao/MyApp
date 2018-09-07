Attribute VB_Name = "MOD_1"
Sub A2_NewSheet()
    Columns("A:E").Select
    Selection.Copy
Set sh = Sheets.Add
With sh
.Name = "CP_0"
End With
    Selection.PasteSpecial Paste:=xlPasteValuesAndNumberFormats, Operation:= _
        xlNone, SkipBlanks:=False, Transpose:=False
    Rows("1:1").Select
    Selection.Delete Shift:=xlUp
    Selection.Delete Shift:=xlUp
End Sub