Attribute VB_Name = "MOD_1"
'==============================================================================
' 模块名称: MOD_1
' 功能描述: Excel VBA 复制数据透视表并去除格式
' 作者: 小尧
' 创建日期: 2024-01-01
' 版本: 1.0
'==============================================================================

'------------------------------------------------------------------------------
' 过程名称: A2_NewSheet
' 功能描述: 将数据透视表的内容复制到新工作表，并去除格式只保留值和数字格式
'           用于生成 CP_0 工作表，供后续筛选使用
' 参数说明: 无
' 返回值: 无
' 前置条件:
'   - 活动工作表中 A:E 列包含数据透视表数据
' 处理流程:
'   1. 复制 A:E 列的数据
'   2. 创建新工作表 CP_0
'   3. 粘贴为值和数字格式（去除透视表格式）
'   4. 删除多余的表头行
' 注意事项:
'   - 此过程会删除工作表中的第1行两次，确保去除透视表的表头
'------------------------------------------------------------------------------
Sub A2_NewSheet()
    ' 选中 A:E 列
    Columns("A:E").Select
    
    ' 复制选中的列
    Selection.Copy
    
    ' 创建新工作表
    Set sh = Sheets.Add
    With sh
        .Name = "CP_0"
    End With
    
    ' 粘贴为值和数字格式（去除原格式，只保留数值和数字格式）
    ' Paste:=xlPasteValuesAndNumberFormats - 只粘贴值和数字格式
    ' Operation:=xlNone - 不进行任何运算
    ' SkipBlanks:=False - 不跳过空单元格
    ' Transpose:=False - 不转置
    Selection.PasteSpecial Paste:=xlPasteValuesAndNumberFormats, Operation:= _
        xlNone, SkipBlanks:=False, Transpose:=False
    
    ' 选中第1行
    Rows("1:1").Select
    
    ' 删除第1行（删除透视表的表头）
    Selection.Delete Shift:=xlUp
    
    ' 再次删除第1行（确保去除所有表头信息）
    Selection.Delete Shift:=xlUp
End Sub
