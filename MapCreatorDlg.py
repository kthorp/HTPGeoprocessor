'''
Created on Feb 25, 2014

@author: kthorp
'''
from __future__ import absolute_import
from builtins import str
from builtins import range
import os
from qgis.PyQt.QtCore import QFileInfo, Qt, QVariant, pyqtSlot
from qgis.PyQt.QtWidgets import QDialog, QFileDialog, QApplication, QMessageBox 
from qgis.core import QgsVectorLayer, QgsGeometry, QgsField, QgsFields, QgsPointXY
from qgis.core import QgsFeature, QgsVectorFileWriter
from .Ui_MapCreatorDlg import Ui_MapCreatorDlg

class MapCreatorDlg(QDialog): 
    def __init__(self, iface): 
        QDialog.__init__(self) 
        # Set up the user interface from Designer. 
        self.ui = Ui_MapCreatorDlg()
        self.ui.setupUi(self)
        self.ui.ProgressBar.setValue(0)
        self.iface = iface
        
        self.inputfile = ''
        self.outputfile = ''

    @pyqtSlot()
    def on_btnBrowse1_clicked(self):            
        f, __ = QFileDialog.getOpenFileName(self,
                                        'Select Input Coordinate File:',
                                        os.getcwd(),
                                        '*.csv') 
        
        if f != '':
            self.inputfile = f
            self.ui.tbxInput.setText(self.inputfile)
            os.chdir(os.path.dirname(str(f)))
        
    @pyqtSlot()
    def on_tbxInput_textEdited(self):
        self.inputfile = self.ui.tbxInput.text() 

    @pyqtSlot()
    def on_btnBrowse2_clicked(self):                   
        f, __ = QFileDialog.getSaveFileName(self,
                                        'Specify Output Shapefile:',
                                        os.getcwd(),
                                        '*.shp') 
        
        if f != '':
            self.outputfile = f
            self.ui.tbxOutput.setText(self.outputfile)
            os.chdir(os.path.dirname(str(f)))
        
    @pyqtSlot()
    def on_tbxOutput_textEdited(self):
        if os.path.exists(self.ui.tbxOutput.text()):
            f = os.path.basename(str(self.ui.tbxOutput.text())) 
            res = QMessageBox.question(self,
                                       'Confirm Save As',
                                       f + ' already exists\n' +
                                       'Do you want to replace it?',
                                       QMessageBox.Yes,
                                       QMessageBox.No)
            if res == QMessageBox.Yes:
                self.outputfile = self.ui.tbxOutput.text()
            else:
                self.ui.tbxOutput.setText(self.outputfile)

    @pyqtSlot()
    def on_btnRun_clicked(self):
                
        if self.inputfile == '':
            QMessageBox.critical(self,'Map Creator',
                                 'Please specify input coordinate file.')
            return
        
        if self.outputfile == '':
            QMessageBox.critical(self,'Map Creator',
                                 'Please specify output shapefile.')
            return
        
        self.setCursor(Qt.WaitCursor)

        #Open coordinate input file
        f = open(self.inputfile, 'r')
        lines = f.readlines()
        f.close()
        header = lines[0].split(',')[0]
        totfeat = len(lines) - 1
        lines.pop(0)
        lines.reverse() 
        
        #Create vector layer
        basename = os.path.basename(self.outputfile)
        vlayer = QgsVectorLayer("Polygon", basename, "memory")
        vprovider = vlayer.dataProvider()
        fld = QgsField(header,QVariant.String)
        flds = QgsFields()
        flds.append(fld)
        vprovider.addAttributes([fld])
        vlayer.startEditing()
                
        hull = []
        for cnt, line in enumerate(lines):
            line = line.rstrip().split(',')
            numcoords = int((len(line) - 1) / 2)
            hull[:] = []
            geom = QgsGeometry()
            feat = QgsFeature()
            feat.setFields(flds)
            for i in range(numcoords):
                hull.append(QgsPointXY(float(line[i*2+1]),float(line[i*2+2])))
            geom = geom.fromMultiPointXY(hull)
            geom = geom.convexHull()
            feat.setGeometry(geom)
            feat.setAttribute(header,str(line[0]))
            result = vlayer.addFeature(feat)
            if not result:
                self.setCursor(Qt.ArrowCursor)
                QMessageBox.critical(self,'Map Creator', 'Processing error.')
                return
            self.ui.ProgressBar.setValue(float(cnt+1)/float(totfeat) * 100.0)
            QApplication.processEvents()  
        vlayer.commitChanges()
        vlayer.updateExtents()
        
        #Write the output shapefile
        if os.path.exists(self.outputfile):
            QgsVectorFileWriter.deleteShapeFile(self.outputfile)
        voptions = QgsVectorFileWriter.SaveVectorOptions()
        voptions.driverName = 'ESRI Shapefile'
        voptions.fileEncoding = 'utf-8'
        result = QgsVectorFileWriter.writeAsVectorFormat(vlayer, 
                                                         self.outputfile, 
                                                         voptions)

        if result[0] != 0:
            QMessageBox.critical(self,'Map Creator','Error creating shapefile.')
        else: #Ask to add shapfile to map
            name = QFileInfo(self.outputfile).completeBaseName()
            result = QMessageBox.question(self,'Map Creator',
                                          'Add shapefile to map?',
                                          QMessageBox.Yes,
                                          QMessageBox.No)
            if result == QMessageBox.Yes:
                self.iface.addVectorLayer(self.outputfile, name, 'ogr')
                
        self.setCursor(Qt.ArrowCursor)
    
    @pyqtSlot()
    def on_btnExit_clicked(self):
        self.close()
