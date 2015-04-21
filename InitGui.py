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

class ExplodedAnimation(Workbench):
	Icon = """
/* XPM */
static char *dummy[]={
"16 16 3 1",
". c None",
"# c #0000ff",
"a c #ffff00",
"................",
".##.........###.",
".##.........###.",
".##.........###.",
".##..####...a...",
"...a.####..a....",
"...a.####.a.....",
"....a####a......",
"...##########...",
"...##########...",
"...##a..........",
"...##.a.........",
"...##..########.",
"...##..########.",
".......########.",
"................"};"""
	
	MenuText = "Exploded Animation"
	ToolTip = "Animated assembly explosion"

	def GetClassName( self ): 
		return "Gui::PythonWorkbench"
	
	def Initialize( self ):
		import ExplodedAnimation

		self.tools=[ "CreateRoute",
		             "ResetStart",
		             "RunBackward",
		             "RunForward",
		             "ResetEnd" ]
						

		FreeCAD.t=self.appendToolbar("ExplodedAnimation",self.tools)
	
		self.appendMenu('ExplodedAnimation',self.tools)
		
  	Log ('Exploded animation workbench loaded\n')

	def Activated(self):
		pass
				
	def Deactivated(self):
	  pass


FreeCADGui.addWorkbench(ExplodedAnimation)


