Attribute VB_Name = "MOD_1"
Sub A3_filters()
'
' filters()宏
' 用来生成具体结算单的业务代码,粘贴,按不同 CP 方分开粘贴明细,注意CP_sheet这个表格不需要表头.修改结算单相关的代码需要写在 WITH sh 里面
' 还有，设置了一下打印区域。
' 
For c = 1 To Worksheets("CP_sheet").UsedRange.Rows.Count
Dim CP_Name As String
   CP_Name = CStr(Worksheets("CP_sheet").Cells(c, 1).Value)
   Debug.Print CP_Name
        Set sh = Sheets.Add
        With sh
            .Range("a1") = "供应商"
            .Range("a2") = CP_Name
            Sheets("CP_0").UsedRange.AdvancedFilter Action:=xlFilterCopy, _
                CriteriaRange:=.Range("A1:A2"), CopyToRange:=.Range("A3"), Unique:=False
            .Name = CP_Name + "_2018.8"
               '''以下开始从模板复制结算单汇总
                 Worksheets("template").Rows("1:16").Copy
                '''复制结束
               '''粘贴汇总模板并且调整格式,设置页面格式和打印区域
                Rows("1:1").Select
                Selection.Insert Shift:=xlDown
                Columns("A:A").ColumnWidth = 27
                Columns("C:C").ColumnWidth = 10.25
                Columns("D:D").EntireColumn.AutoFit
                Columns("G:G").ColumnWidth = 27
                Range("A1:G16").Select
                Application.CutCopyMode = False
                ActiveSheet.PageSetup.PrintArea = "$A$1:$G$16"
                 '''设置打印区域的代码，以下这一堆是系统录制出来的
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
                 '''设置打印区域的代码，录制结束
        End With
''''        Call SaveSheetAsWorkbook(CP_Name)
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
