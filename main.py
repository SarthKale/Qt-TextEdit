from gui import Ui_TextEditor 
import sys 
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import * 
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo, Qt, QTime, QDate
from PyQt5.QtGui import QFont 

class EditorWindow(QtWidgets.QMainWindow, Ui_TextEditor):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("SkEdit")
        self.setupUi(self) 
        self.show() 
        self.handleButtons() 
        self.toggleB = False
        self.toggleI = False
        self.toggleU = False

    def handleButtons(self):
        self.actionNew.triggered.connect(self.fileNew) 
        self.actionOpen.triggered.connect(self.openFile) 
        self.actionSave.triggered.connect(self.fileSave) 
        self.actionPrint.triggered.connect(self.printfile) 
        self.actionExport_PDF.triggered.connect(self.exportPdf) 
        self.actionClose.triggered.connect(self.close)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionCut.triggered.connect(self.cut) 
        self.actionUndo.triggered.connect(self.textEdit.undo) 
        self.actionRedo.triggered.connect(self.textEdit.redo) 
        self.actionFont.triggered.connect(self.fontDialog) 
        self.actionColor.triggered.connect(self.colorDialog)
        self.actionBold.triggered.connect(self.bold) 
        self.actionItalic.triggered.connect(self.italic) 
        self.actionUnderline.triggered.connect(self.underline) 
        self.actionLeft.triggered.connect(self.leftAlign) 
        self.actionRight.triggered.connect(self.rightAlign) 
        self.actionCenter.triggered.connect(self.centerAlign) 
        self.actionJustify.triggered.connect(self.justify) 
        self.actionDate.triggered.connect(self.date) 
        self.actionTime.triggered.connect(self.time) 
        self.actionText_Highlight.triggered.connect(self.hightlight) 

    def fileNew(self):
        self.textEdit.clear() 
        print("New Document ") 

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, "Open File", "C:\\Users\\SarthK\\Desktop") 
        if filename[0]: 
            with open(filename[0], "r") as f: 
                data = f.read() 
                self.textEdit.setText(data) 
                f.close() 
            print("File Open") 
    
    def fileSave(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        if filename[0]:
            with open(filename[0], 'w') as f:
                text = self.textEdit.toPlainText()
                f.write(text)
                QMessageBox.about(self, "Saved File", "File Saved Successfully")
                f.close()

    def printfile(self): 
        printer = QPrinter(QPrinter.HighResolution) 
        dialog = QPrintDialog(printer, self) 
        if dialog.exec_() == QPrintDialog.Accepted: 
            self.textEdit.print_(printer) 

    def exportPdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf) ;; All Files") 
        if fn != "": 
            if QFileInfo(fn).suffix() == "": fn += '.pdf' 
            printer = QPrinter(QPrinter.HighResolution) 
            printer.setOutputFormat(QPrinter.PdfFormat) 
            printer.setOutputFileName(fn) 
            self.textEdit.document().print_(printer) 

    def close(self):
        self.close() 

    def copy(self):
        cursor = self.textEdit.textCursor() 
        selected = cursor.selectedText() 
        self.copied = selected 

    def paste(self):
        self.textEdit.append(self.copied) 

    def cut(self):
        cursor = self.textEdit.textCursor() 
        selected = cursor.selectedText() 
        self.copied = selected 
        self.textEdit.cut() 

    def fontDialog(self): 
        font, ok = QFontDialog.getFont() 
        if ok:
            self.textEdit.setFont(font)  

    def colorDialog(self):
        color = QColorDialog.getColor() 
        self.textEdit.setTextColor(color) 

    def bold(self):
        self.toggleB = True
        font = QFont() 
        font.setBold(True) 
        font.setPointSize(14)
        self.textEdit.setFont(font) 
    
    def italic(self):
        font = QFont() 
        font.setItalic(True) 
        font.setPointSize(14)
        self.textEdit.setFont(font) 

    def underline(self): 
        font = QFont() 
        font.setUnderline(True) 
        font.setPointSize(14)
        self.textEdit.setFont(font) 

    def leftAlign(self):
        self.textEdit.setAlignment(Qt.AlignLeft) 

    def centerAlign(self):
        self.textEdit.setAlignment(Qt.AlignHCenter)  

    def rightAlign(self):
        self.textEdit.setAlignment(Qt.AlignRight)  

    def justify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)   

    def date(self):
        d = QDate.currentDate() 
        self.textEdit.append(d.toString(Qt.DefaultLocaleLongDate)) 

    def time(self):
        t = QTime.currentTime()
        self.textEdit.append(t.toString(Qt.DefaultLocaleLongDate)) 

    def hightlight(self): 
        color = QColorDialog.getColor() 
        self.textEdit.setTextBackgroundColor(color)  

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    editor = EditorWindow() 
    sys.exit(app.exec()) 

