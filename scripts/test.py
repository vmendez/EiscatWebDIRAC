#!/usr/bin/env python

import sys
from DIRAC.Core.Base import Script

Script.parseCommandLine()

import tempfile
import os
import subprocess
import gzip
import shutil

from DIRAC import gLogger, S_OK, S_ERROR, rootPath
from DIRAC.ConfigurationSystem.Client.Helpers.CSGlobals import getInstalledExtensions
from EiscatWebDIRAC.Lib.SessionData import SessionData
from EiscatWebDIRAC.Core.HandlerMgr import HandlerMgr
from EiscatWebDIRAC.Lib.CompilerHelper import CompilerHelper

class Test(object):

  def __init__( self ):
    self.__extVersion = SessionData.getExtJSVersion()
    self.staticPaths = []
    for ext in HandlerMgr().getPaths( "static" ):
      if "WebAppDIRAC" in ext:
        continue
      self.staticPaths.append( ext )
    #self.extensions = getInstalledExtensions()
    self.extensions = []
    for ext in getInstalledExtensions():
      if ext == "WebAppDIRAC":
        continue
      self.extensions.append( ext )


test = Test()
print "extensions"
print test.extensions 
print "staticPaths"
print test.staticPaths 
webAppPath = os.path.dirname( test.staticPaths[-1] )
print "webAppPath"
print webAppPath
