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

import os
import FreeCAD, FreeCADGui
import EACommands as EAC
App = FreeCAD

__dir__ = os.path.dirname(__file__)	
####### CREATE ROUTE ####################################
class CreateRoute:
  def GetResources(self):
    return {'Pixmap' : __dir__ + '/icons/icon_createroute.png', 'MenuText': 'Create Route', 'ToolTip': 'Create a new route'}
  
  def IsActive(self):
    if FreeCADGui.ActiveDocument:
      return True
    
    else:
      return False
   
  def Activated(self):
    EAC.NewFolders()
    EAC.NewRoute()
    return

class RunForward:
  def GetResources(self):
    return {'Pixmap' : __dir__ + '/icons/icon_forward.png', 'MenuText': 'Run Forward', 'ToolTip': 'Run the animation forwards'}
  
  def IsActive(self):
    if FreeCADGui.ActiveDocument:
      return True
    
    else:
      return False
   
  def Activated(self): 
    EAC.RunAnimation(False)
    return

class RunBackward:
  def GetResources(self):
    return {'Pixmap' : __dir__ + '/icons/icon_backward.png', 'MenuText': 'Run Backward', 'ToolTip': 'Run the animation backwards'}
  
  def IsActive(self):
    if FreeCADGui.ActiveDocument:
      return True
    
    else:
      return False
   
  def Activated(self): 
    EAC.RunAnimation(True)
    return


class ResetStart:
  def GetResources(self):
    return {'Pixmap' : __dir__ + '/icons/icon_start.png', 'MenuText': 'Reset Assembly', 'ToolTip': 'Assembled position'}
  
  def IsActive(self):
    if FreeCADGui.ActiveDocument:
      return True
    
    else:
      return False
   
  def Activated(self): 
    EAC.ResetStart()
    return

class ResetEnd:
  def GetResources(self):
    return {'Pixmap' : __dir__ + '/icons/icon_end.png', 'MenuText': 'Reset Assembly', 'ToolTip': 'Exploded position'}
  
  def IsActive(self):
    if FreeCADGui.ActiveDocument:
      return True
    
    else:
      return False
   
  def Activated(self): 
    EAC.ResetEnd()
    return

if FreeCAD.GuiUp:
  FreeCADGui.addCommand('CreateRoute', CreateRoute() )
  FreeCADGui.addCommand('RunForward', RunForward() )
  FreeCADGui.addCommand('RunBackward', RunBackward() )
  FreeCADGui.addCommand('ResetStart', ResetStart() )
  FreeCADGui.addCommand('ResetEnd', ResetEnd() )
