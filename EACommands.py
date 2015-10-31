# -*- coding: utf-8 -*-
# FreeCAD Exploded Assembly Animation Workbench
# (c) 2014 Javier Martínez García

#***************************************************************************
#*   (c) Javier Martínez García 2014                                       *   
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU General Public License (GPL)            *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This macro is distributed in the hope that it will be useful,         *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        * 
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        * 
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************/

import sys
from PySide import QtGui, QtCore
import Part
import FreeCAD
from FreeCAD import Gui
import time
App = FreeCAD
AAD = App.ActiveDocument


def NewFolders():
  ProjectFolder = FreeCAD.ActiveDocument.getObject( "ExplodedAnimation" )
  try:
    ProjectFolder.Label
    
  except:
    ProjectFolder = FreeCAD.ActiveDocument.addObject( "App::DocumentObjectGroup", "ExplodedAnimation" )
    AnimationData =  FreeCAD.ActiveDocument.addObject( "App::DocumentObjectGroup", "EA_Data" )
    AnimationRoutes = FreeCAD.ActiveDocument.addObject( "App::DocumentObjectGroup", "EA_Routes" )
    ProjectFolder.addObject( AnimationData )
    ProjectFolder.addObject( AnimationRoutes )


def NewRoute():
  def createSketch():
    chD.close()
    try:
      SelObjNameData = "Dt_" + FreeCAD.Gui.Selection.getSelection()[0].Label
      # ADD ROUTE DATA
      class TrajectoryData:
       def __init__(self, obj):
          obj.addProperty("App::PropertyString",
                          "ObjectName",
                          "Trajectory Data",
                          "Moving Object Name")
          obj.addProperty("App::PropertyPlacement",
                          "BasePlacement",
                          "Trajectory Data",
                          "Base placement for rotation" )
          
          obj.addProperty("App::PropertyString",
                          "RouteName",
                          "Trajectory Data",
                          "Trajectory Object Name")
          
          obj.addProperty("App::PropertyVector",
                          "COM",
                          "Trajectory Data",
                          "Vector")

          obj.addProperty("App::PropertyVector",
                          "FirstPoint",
                          "Trajectory Data",
                          "Vector")
          
          obj.addProperty("App::PropertyFloat",
                          "StepSize",
                          "Trajectory Data",
                          "Step size").StepSize = 0.5
          
          obj.addProperty("App::PropertyFloat",
                          "LinearSpeed",
                          "Trajectory Data",
                          "Linear speed").LinearSpeed = 10.0
          
          obj.addProperty("App::PropertyFloat",
                          "Pitch",
                          "Trajectory Data",
                          "Rotation turns").Pitch = 0.0
          
          obj.addProperty("App::PropertyInteger",
                          "SyncGroup",
                          "Trajectory Data",
                          "Sync movement within parts").SyncGroup = -1                     
          obj.Proxy = self
       
       def onChanged(self, fp, prop):
           return
       
       def execute(self, fp):
          return

      
      TD = FreeCAD.ActiveDocument.addObject( "App::FeaturePython", SelObjNameData )
      dataFolder = FreeCAD.ActiveDocument.getObject( "EA_Data" )
      dataFolder.addObject( TD )
      TrajectoryData( TD )
      TD.ObjectName = FreeCAD.Gui.Selection.getSelection()[0].Name
      TD.COM = FreeCAD.Gui.Selection.getSelection()[0].Shape.Placement.Base
      TD.FirstPoint = FreeCAD.Gui.Selection.getSelectionEx()[0].SubObjects[0].CenterOfMass
      TD.BasePlacement = FreeCAD.Gui.Selection.getSelection()[0].Shape.Placement
      # ADD ROUTE SKETCH
      SelObjName = "Rt_" + FreeCAD.Gui.Selection.getSelection()[0].Label
      SelFace = FreeCAD.Gui.Selection.getSelectionEx()[0].SubObjects[0]
      faceCom = SelFace.CenterOfMass
      P_A = SelFace.Edges[0].valueAt( 0.0 )
      V_0 = ( P_A - faceCom ).normalize()
      NewRoute = FreeCAD.ActiveDocument.addObject("Sketcher::SketchObject", SelObjName)
      TD.RouteName = NewRoute.Name
      RouteFolder = FreeCAD.ActiveDocument.getObject( "EA_Routes" )
      RouteFolder.addObject( NewRoute )
      NewRoute.Placement = FreeCAD.Placement( faceCom , App.Rotation( V_0, 0 ) )
      NewRoute.ViewObject.LineColor = ( 1.0, 1.0, 0.0 )
      NewRoute.ViewObject.PointColor = ( 1.0, 1.0, 0.0 )
      NewRoute.ViewObject.DrawStyle = "Dotted"
      FreeCAD.Gui.ActiveDocument.setEdit(NewRoute.Label)
      FreeCAD.Gui.activateWorkbench( "PartDesignWorkbench" )

    
    except: #clean is something went terribly wrong
      FreeCAD.Console.PrintError("Wrong selection!" )
      try:
        FreeCAD.ActiveDocument.removeObject( TD.Label )
        FreeCAD.ActiveDocument.removeObject( NewRoute.Label )
        
      except:
        pass
     
      
        

  def fromWire():
    chD.close()
    try:
      SelObjNameData = "Dt_" + FreeCAD.Gui.Selection.getSelection()[0].Label
      class TrajectoryData:
       def __init__(self, obj):
          obj.addProperty("App::PropertyString",
                          "ObjectName",
                          "Trajectory Data",
                          "Moving Object Name")
          
          obj.addProperty("App::PropertyPlacement",
                          "BasePlacement",
                          "Trajectory Data",
                          "Base placement for rotation" )
          
          obj.addProperty("App::PropertyString",
                          "RouteName",
                          "Trajectory Data",
                          "Trajectory Object Name")
          
          obj.addProperty("App::PropertyVector",
                          "COM",
                          "Trajectory Data",
                          "Vector")

          obj.addProperty("App::PropertyVector",
                          "FirstPoint",
                          "Trajectory Data",
                          "Vector")
          
          obj.addProperty("App::PropertyFloat",
                          "StepSize",
                          "Trajectory Data",
                          "Step size").StepSize = 0.5
          
          obj.addProperty("App::PropertyFloat",
                          "LinearSpeed",
                          "Trajectory Data",
                          "Linear speed").LinearSpeed = 10.0
          
          obj.addProperty("App::PropertyFloat",
                          "Pitch",
                          "Trajectory Data",
                          "Rotation turns").Pitch = 0.0
          
          obj.addProperty("App::PropertyInteger",
                          "SyncGroup",
                          "Trajectory Data",
                          "Sync movement within parts").SyncGroup = -1                     
          obj.Proxy = self
       
       def onChanged(self, fp, prop):
           return
       
       def execute(self, fp):
          return


      TD = FreeCAD.ActiveDocument.addObject( "App::FeaturePython", SelObjNameData )
      dataFolder = FreeCAD.ActiveDocument.getObject( "EA_Data" )
      dataFolder.addObject( TD )
      TrajectoryData( TD )
      TD.ObjectName = FreeCAD.Gui.Selection.getSelection()[0].Name
      TD.COM = FreeCAD.Gui.Selection.getSelection()[0].Shape.Placement.Base
      TD.FirstPoint = FreeCAD.Gui.Selection.getSelection()[0].Shape.Vertexes[0].Point
      TD.RouteName = FreeCAD.Gui.Selection.getSelection()[1].Name
      TD.BasePlacement = FreeCAD.Gui.Selection.getSelection()[0].Shape.Placement
      FreeCAD.Gui.Selection.getSelection()[1].ViewObject.LineColor = (1.000,1.000,0.000)
      FreeCAD.Gui.Selection.getSelection()[1].ViewObject.DrawStyle = "Dotted"
      # ADD WIRE AS ROUTE
      routeWire = FreeCAD.Gui.Selection.getSelection()[1]
      routeWire.Label = "Rt_" + FreeCAD.Gui.Selection.getSelection()[0].Label
      routeFolder = FreeCAD.ActiveDocument.getObject( "EA_Routes" )
      routeFolder.addObject( routeWire )
      
    except: #clean is something went terribly wrong
      FreeCAD.Console.PrintError("Wrong selection!" )
      try:
        FreeCAD.ActiveDocument.removeObject( TD.Label )
        FreeCAD.ActiveDocument.removeObject( NewRoute.Label )
        
      except:
        pass
    pass


  # Dialog
  chD = QtGui.QWidget()
  QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
  Label = QtGui.QLabel( "Create new route from: ", chD)
  Btn_createSketch = QtGui.QPushButton('Sketch', chD)
  Btn_fromWire = QtGui.QPushButton('Wire', chD )
  Btn_createSketch.setToolTip('Create a new route using sketcher')
  Btn_fromWire.setToolTip('Create a new route from an existing wire')
  Label.move( 35, 10 )
  Btn_createSketch.move( 20, 30 )
  Btn_fromWire.move( 110, 30 )
  chD.setGeometry(150,150, 220, 70)
  chD.setWindowTitle('NewRoute')    
  Btn_createSketch.clicked.connect( createSketch )
  Btn_fromWire.clicked.connect( fromWire )
  chD.show()

################ ANIMATION  ENGINE #############################################

def RunAnimation( reverse = False ):
  EA_DataGroup = FreeCAD.ActiveDocument.getObject( "EA_Data" ).Group
  if reverse:
    EA_DataGroup = EA_DataGroup[::-1]
  for dataItem in EA_DataGroup:
    routeItem = FreeCAD.ActiveDocument.getObject( dataItem.RouteName )
    routePoints = []
    for point in routeItem.Shape.Vertexes:
      routePoints.append( point.Point )
    
    RouteStartPoint_0 = routePoints[0]
    RouteStartPoint_1 = routePoints[1]
    V_RotLength = ( routePoints[1] - routePoints[0]).Length    
    V_RotDir = ( routePoints[1] - routePoints[0] ).normalize()
    if reverse:
      routePoints = routePoints[::-1]   
    
    object = FreeCAD.ActiveDocument.getObject( dataItem.ObjectName )
    stepSize = dataItem.StepSize
    delayTime = 0.01 / ( dataItem.LinearSpeed + 1.0 )
    V_Correction = dataItem.COM - routePoints[0]
    if reverse:
      V_Correction = dataItem.COM - routePoints[-1]
    for n in range( len( routePoints ) - 1 ):
      P_a = routePoints[n]
      P_b = routePoints[n+1]
      V_Dir = ( P_b - P_a ).normalize()
      stepNumber = (P_b - P_a).Length / stepSize
      rotStep = V_RotLength*dataItem.Pitch / stepNumber*360.0
      for i in range( int(stepNumber) ):
        #object.Placement.Base = P_a + V_Dir*stepSize*i + V_Correction
        if P_a == RouteStartPoint_0 and not(reverse):
          rot = object.Placement.Rotation
          object.Placement.Rotation = rot.multiply( FreeCAD.Rotation( V_RotDir , rotStep*-i ) )
          object.Placement.Base = P_a + V_Dir*stepSize*i + V_Correction
        if P_a == RouteStartPoint_1 and reverse:
          rot = object.Placement.Rotation
          object.Placement.Rotation = rot.multiply( FreeCAD.Rotation( V_RotDir , rotStep*i ) )
          object.Placement.Base = P_a + V_Dir*stepSize*i + V_Correction
        
        else:
          object.Placement.Base = P_a + V_Dir*stepSize*i + V_Correction
        
        time.sleep( delayTime )
        FreeCAD.Gui.updateGui()
      
      object.Placement.Base = P_b + V_Correction
      object.Placement.Rotation = dataItem.BasePlacement.Rotation
      FreeCAD.Gui.updateGui()
      time.sleep( delayTime )
    
    if reverse:
      object.Placement.Base = dataItem.COM
      object.Placement.Rotation = dataItem.BasePlacement.Rotation
  

def ResetStart():
  EA_DataGroup = FreeCAD.ActiveDocument.getObject( "EA_Data" ).Group
  for dataItem in EA_DataGroup:
    routeName = "Rt_" + dataItem.Label[3:]
    routeItem = FreeCAD.ActiveDocument.getObject( routeName )
    object = FreeCAD.ActiveDocument.getObject( dataItem.ObjectName )
    object.Placement.Base = dataItem.COM
    object.Placement.Rotation = dataItem.BasePlacement.Rotation
    FreeCAD.Gui.updateGui()

def ResetEnd():
  EA_DataGroup = FreeCAD.ActiveDocument.getObject( "EA_Data" ).Group
  for dataItem in EA_DataGroup:
    routeItem = FreeCAD.ActiveDocument.getObject( dataItem.RouteName )
    routePoints = []
    for point in routeItem.Shape.Vertexes:
      routePoints.append( point.Point )
    
    routePoints = routePoints[::-1]
    V_Correction = dataItem.COM - dataItem.FirstPoint
    object = FreeCAD.ActiveDocument.getObject( dataItem.ObjectName )
    object.Placement.Base = routePoints[0] + V_Correction
    object.Placement.Rotation = dataItem.BasePlacement.Rotation
    FreeCAD.Gui.updateGui()
