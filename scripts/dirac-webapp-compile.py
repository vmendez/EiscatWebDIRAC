#!/usr/bin/env python

import sys
from DIRAC.Core.Base import Script

class Params:

  appNameTarget = False

  def setAppNameTarget( self, args ):
    self.appNameTarget = args
    return DIRAC.S_OK()

  def registerCLISwitches( self ):
    Script.registerSwitch( "a:", "appName=", "Application name to compile", self.setAppNameTarget )

params = Params()
params.registerCLISwitches()

Script.setUsageMessage( '\n'.join( [ 'Usage:',
                                     '  %s [option] ' % Script.scriptName,
                                     'Arguments:' ]))

Script.parseCommandLine( ignoreErrors = True )

from DIRAC import gLogger
from EiscatWebDIRAC.Lib.Compiler import Compiler

if __name__ == "__main__":
  if not params.appNameTarget:
    result = Compiler().run()
  else:
    result = Compiler().run(appNameTarget=params.appNameTarget)

  if not result[ 'OK' ]:
    gLogger.fatal( result[ 'Message' ] )
    sys.exit(1)
  sys.exit(0)

