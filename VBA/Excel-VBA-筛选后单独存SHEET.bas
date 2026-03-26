Attribute VB_Name = "MOD_1"
'==============================================================================
' 模块名称: MOD_1
' 功能描述: Excel VBA 根据供应商筛选数据并生成结算单
' 作者: 小尧
' 创建日期: 2024-01-01
' 版本: 1.0
'==============================================================================

'------------------------------------------------------------------------------
' 过程名称: A3_filters
' 功能描述: 根据 CP_sheet 工作表中的供应商列表，为每个供应商生成独立的结算单
'           包括：筛选数据、复制模板、设置打印区域和页面格式
' 参数说明: 无
' 返回值: 无
' 前置条件:
'   - 工作簿中必须包含 "CP_sheet" 工作表（包含供应商名称列表，无表头）
'   - 工作簿中必须包含 "CP_0" 工作表（包含原始数据）
'   - 工作簿中必须包含 "template" 工作表（结算单模板）
' 异常处理: 无显式错误处理，依赖 VBA 默认错误处理机制
'------------------------------------------------------------------------------
Sub A3_filters()
    ' 声明变量
    Dim CP_Name As String  ' 存储当前处理的供应商名称
    Dim c As Integer       ' 循环计数器
    
    ' 遍历 CP_sheet 工作表中的所有行
    For c = 1 To Worksheets("CP_sheet").UsedRange.Rows.Count
        ' 获取当前行的供应商名称
        CP_Name = CStr(Worksheets("CP_sheet").Cells(c, 1).Value)
        Debug.Print CP_Name  ' 在立即窗口输出供应商名称（用于调试）
        
        ' 创建新工作表用于存放筛选结果
        Set sh = Sheets.Add
        
        ' 使用 With 语句设置新工作表的属性
        With sh
            ' 设置筛选条件区域
            .Range("a1") = "供应商"
            .Range("a2") = CP_Name
            
            ' 使用高级筛选将 CP_0 工作表的数据复制到新工作表
            ' CriteriaRange: 筛选条件区域
            ' CopyToRange: 复制目标区域
            Sheets("CP_0").UsedRange.AdvancedFilter Action:=xlFilterCopy, _
                CriteriaRange:=.Range("A1:A2"), CopyToRange:=.Range("A3"), Unique:=False
            
            ' 设置工作表名称
            .Name = CP_Name + "_2018.8"
            
            ' 从模板复制结算单汇总（第1-16行）
            Worksheets("template").Rows("1:16").Copy
            
            ' 粘贴汇总模板并调整格式
            Rows("1:1").Select
            Selection.Insert Shift:=xlDown
            
            ' 设置列宽
            Columns("A:A").ColumnWidth = 27
            Columns("C:C").ColumnWidth = 10.25
            Columns("D:D").EntireColumn.AutoFit
            Columns("G:G").ColumnWidth = 27
            
            ' 设置打印区域
            Range("A1:G16").Select
            Application.CutCopyMode = False
            ActiveSheet.PageSetup.PrintArea = "$A$1:$G$16"
            
            ' 设置页面格式（以下代码由系统录制生成）
            Application.PrintCommunication = False
            With ActiveSheet.PageSetup
                .PrintTitleRows = ""
                .PrintTitleColumns = ""
            End With
            Application.PrintCommunication = True
            ActiveSheet.PageSetup.PrintArea = "$A$1:$G$16"
            Application.PrintCommunication = False
            With ActiveSheet.PageSetup
                .LeftHeader = ""
                .CenterHeader = ""
                .RightHeader = ""
                .LeftFooter = ""
                .CenterFooter = ""
                .RightFooter = ""
                .LeftMargin = Application.InchesToPoints(0.708661417322835)
                .RightMargin = Application.InchesToPoints(0.708661417322835)
                .TopMargin = Application.InchesToPoints(0.748031496062992)
                .BottomMargin = Application.InchesToPoints(0.748031496062992)
                .HeaderMargin = Application.InchesToPoints(0.31496062992126)
                .FooterMargin = Application.InchesToPoints(0.31496062992126)
                .PrintHeadings = False
                .PrintGridlines = False
                .PrintComments = xlPrintNoComments
                .CenterHorizontally = False
                .CenterVertically = False
                .Orientation = xlLandscape
                .Draft = False
                .PaperSize = xlPaperA4
                .FirstPageNumber = xlAutomatic
                .Order = xlDownThenOver
                .BlackAndWhite = False
                .Zoom = 100
                .PrintErrors = xlPrintErrorsDisplayed
                .OddAndEvenPagesHeaderFooter = False
                .DifferentFirstPageHeaderFooter = False
                .ScaleWithDocHeaderFooter = True
                .AlignMarginsHeaderFooter = True
                .EvenPage.LeftHeader.Text = ""
                .EvenPage.CenterHeader.Text = ""
                .EvenPage.RightHeader.Text = ""
                .EvenPage.LeftFooter.Text = ""
                .EvenPage.CenterFooter.Text = ""
                .EvenPage.RightFooter.Text = ""
                .FirstPage.LeftHeader.Text = ""
                .FirstPage.CenterHeader.Text = ""
                .FirstPage.RightHeader.Text = ""
                .FirstPage.LeftFooter.Text = ""
                .FirstPage.CenterFooter.Text = ""
                .FirstPage.RightFooter.Text = ""
            End With
            Application.PrintCommunication = True
        End With
        
        ' 可选：调用 SaveSheetAsWorkbook 保存当前工作表
        ' Call SaveSheetAsWorkbook(CP_Name)
    Next
End Sub

'------------------------------------------------------------------------------
' 过程名称: SaveSheetAsWorkbook
' 功能描述: 将当前选中的所有工作表分别另存为独立的 Excel 文件
' 参数说明: 无
' 返回值: 无
' 异常处理: 使用 On Error GoTo 语句捕获错误
'------------------------------------------------------------------------------
Sub SaveSheetAsWorkbook()
    Dim theName As String
    On Error GoTo Line1
    For Each sht In ActiveWindow.SelectedSheets
        sht.Copy
        theName = ThisWorkbook.Path & "_" & sht.Name & ".xls"
        ActiveWorkbook.SaveAs Filename:=theName, FileFormat:=xlNormal
        ActiveWindow.Close
    Next
Line1:
End Sub
