Attribute VB_Name = "MOD_1"
'==============================================================================
' 模块名称: MOD_1
' 功能描述: Excel VBA 批量将多个工作表另存为单独的工作簿文件
' 作者: 小尧
' 创建日期: 2024-01-01
' 版本: 1.0
'==============================================================================

'------------------------------------------------------------------------------
' 过程名称: SaveSheetAsWorkbook
' 功能描述: 将当前选中的所有工作表分别另存为独立的 Excel 文件
'           每个工作表保存为一个单独的 .xls 文件，文件名为"原路径_工作表名.xls"
' 参数说明: 无
' 返回值: 无
' 异常处理: 使用 On Error GoTo 语句捕获错误，出错时跳转到 Line1 标签
' 注意事项:
'   - 需要确保原工作簿已保存，以便获取正确的路径
'   - 保存格式为 xlNormal (Excel 97-2003 工作簿格式)
'------------------------------------------------------------------------------
Sub SaveSheetAsWorkbook()
    ' 声明变量
    Dim theName As String  ' 存储保存文件的完整路径和名称
    
    ' 启用错误处理，出错时跳转到 Line1 标签
    On Error GoTo Line1
    
    ' 遍历当前窗口中选中的所有工作表
    For Each sht In ActiveWindow.SelectedSheets
        ' 复制当前工作表到新工作簿
        sht.Copy
        
        ' 构造保存路径：原工作簿路径 + "_" + 工作表名 + ".xls"
        theName = ThisWorkbook.Path & "_" & sht.Name & ".xls"
        
        ' 保存新工作簿，使用标准 Excel 格式
        ActiveWorkbook.SaveAs Filename:=theName, FileFormat:=xlNormal
        
        ' 关闭新工作簿的窗口
        ActiveWindow.Close
    Next
    
' 错误处理标签
Line1:
    ' 错误处理结束，过程正常结束或出错后都会执行到这里
End Sub
