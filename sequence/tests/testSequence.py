##############################################################################
# 
# Zope Public License (ZPL) Version 1.0
# -------------------------------------
# 
# Copyright (c) Digital Creations.  All rights reserved.
# 
# This license has been certified as Open Source(tm).
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions in source code must retain the above copyright
#    notice, this list of conditions, and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions, and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
# 
# 3. Digital Creations requests that attribution be given to Zope
#    in any manner possible. Zope includes a "Powered by Zope"
#    button that is installed by default. While it is not a license
#    violation to remove this button, it is requested that the
#    attribution remain. A significant investment has been put
#    into Zope, and this effort will continue if the Zope community
#    continues to grow. This is one way to assure that growth.
# 
# 4. All advertising materials and documentation mentioning
#    features derived from or use of this software must display
#    the following acknowledgement:
# 
#      "This product includes software developed by Digital Creations
#      for use in the Z Object Publishing Environment
#      (http://www.zope.org/)."
# 
#    In the event that the product being advertised includes an
#    intact Zope distribution (with copyright and license included)
#    then this clause is waived.
# 
# 5. Names associated with Zope or Digital Creations must not be used to
#    endorse or promote products derived from this software without
#    prior written permission from Digital Creations.
# 
# 6. Modified redistributions of any form whatsoever must retain
#    the following acknowledgment:
# 
#      "This product includes software developed by Digital Creations
#      for use in the Z Object Publishing Environment
#      (http://www.zope.org/)."
# 
#    Intact (re-)distributions of any official Zope release do not
#    require an external acknowledgement.
# 
# 7. Modifications are encouraged but must be packaged separately as
#    patches to official Zope releases.  Distributions that do not
#    clearly separate the patches from the original work must be clearly
#    labeled as unofficial distributions.  Modifications which do not
#    carry the name Zope may be packaged in any form, as long as they
#    conform to all of the clauses above.
# 
# 
# Disclaimer
# 
#   THIS SOFTWARE IS PROVIDED BY DIGITAL CREATIONS ``AS IS'' AND ANY
#   EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#   PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL DIGITAL CREATIONS OR ITS
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
#   USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#   ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#   OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
#   OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
#   SUCH DAMAGE.
# 
# 
# This software consists of contributions made by Digital Creations and
# many individuals on behalf of Digital Creations.  Specific
# attributions are listed in the accompanying credits file.
# 
##############################################################################

import sys
sys.path.insert(0, '.')
try:
    import Testing
except ImportError:
    sys.path[0] = '../../'
    import Testing

import unittest
from SortEx import *
from ztestlib import *
from results import *


class TestCase( unittest.TestCase ):
    """
        Test SortEx .
    """

    def setUp( self ):
        """
        """

    def tearDown( self ):
        """
        """
           
    def test1( self ):
        "test1"
        assert res1==SortEx(wordlist)

    def test2( self ):
        "test2"
        assert res2==SortEx(wordlist, (("key",),), mapping=1)

    def test3( self ):
        "test3"
        assert res3==SortEx(wordlist, (("key", "cmp"),), mapping=1)
        
    def test4( self ):
        "test4"
        assert res4==SortEx(wordlist, (("key", "cmp", "desc"),), mapping=1)

    def test5( self ):
        "test5"
        assert res5==SortEx(wordlist, (("weight",), ("key",)), mapping=1)

    def test6( self ):
        "test6"
        assert res6==SortEx(wordlist, (("weight",), ("key", "nocase", "desc")), mapping=1)


    def test7(self):
        "test7"

        def myCmp(s1, s2):
           return -cmp(s1, s2)

        # Create namespace...
        from DocumentTemplate.DT_Util import TemplateDict
        md = TemplateDict()

        #... and push out function onto the namespace
        md._push({"myCmp" : myCmp})

        assert res7==SortEx(wordlist, (("weight",), ("key", "myCmp", "desc")), md, mapping=1)


def test_suite():
    return unittest.makeSuite( TestCase )

def debug():
    return test_suite().debug()

def pdebug():
    import pdb
    pdb.run('debug()')

def main():
    unittest.TextTestRunner().run( test_suite() )

if __name__ == '__main__':
   if len(sys.argv) > 1:
      globals()[sys.argv[1]]()
   else:
      main()