
__doc__='''Conditional insertion

       Conditional insertion is performed using 'if' and 'else'
       commands.

       To include text when an object is true using the EPFS
       format, use::

          %(if name)[
               text 
          %(if name)]

       To include text when an object is true using the HTML
       format, use::

          <!--#if name-->
               text 
          <!--#/if name-->

       where 'name' is the name bound to the object.

       To include text when an object is false using the EPFS
       format, use::

          %(else name)[
               text 
          %(else name)]

       To include text when an object is false using the HTML
       format, use::

          <!--#else name-->
               text 
          <!--#/else name-->

       Finally to include text when an object is true and to
       include different text when the object is false using the
       EPFS format, use::

          %(if name)[
               true text 
          %(if name)]
          %(else name)[
               false text 
          %(else name)]

       and to include text when an object is true and to
       include different text when the object is false using the
       HTML format, use::

          <!--#if name-->
               true text 
          <!--#else name-->
               false text 
          <!--#/if name-->

       Notes:

       - if a variable is nor defined, it is considered to be false.

       - A variable if only evaluated once in an 'if' tag.  If the value
         is used inside the tag, including in enclosed tags, the
         variable is not reevaluated.

''' 

############################################################################
#     Copyright 
#
#       Copyright 1996 Digital Creations, L.C., 910 Princess Anne
#       Street, Suite 300, Fredericksburg, Virginia 22401 U.S.A. All
#       rights reserved.  Copyright in this software is owned by DCLC,
#       unless otherwise indicated. Permission to use, copy and
#       distribute this software is hereby granted, provided that the
#       above copyright notice appear in all copies and that both that
#       copyright notice and this permission notice appear. Note that
#       any product, process or technology described in this software
#       may be the subject of other Intellectual Property rights
#       reserved by Digital Creations, L.C. and are not licensed
#       hereunder.
#
#     Trademarks 
#
#       Digital Creations & DCLC, are trademarks of Digital Creations, L.C..
#       All other trademarks are owned by their respective companies. 
#
#     No Warranty 
#
#       The software is provided "as is" without warranty of any kind,
#       either express or implied, including, but not limited to, the
#       implied warranties of merchantability, fitness for a particular
#       purpose, or non-infringement. This software could include
#       technical inaccuracies or typographical errors. Changes are
#       periodically made to the software; these changes will be
#       incorporated in new editions of the software. DCLC may make
#       improvements and/or changes in this software at any time
#       without notice.
#
#     Limitation Of Liability 
#
#       In no event will DCLC be liable for direct, indirect, special,
#       incidental, economic, cover, or consequential damages arising
#       out of the use of or inability to use this software even if
#       advised of the possibility of such damages. Some states do not
#       allow the exclusion or limitation of implied warranties or
#       limitation of liability for incidental or consequential
#       damages, so the above limitation or exclusion may not apply to
#       you.
#  
#
# If you have questions regarding this software,
# contact:
#
#   Jim Fulton, jim@digicool.com
#
#   (540) 371-6909
#
############################################################################ 
__rcs_id__='$Id: DT_If.py,v 1.9 1998/04/02 17:37:35 jim Exp $'
__version__='$Revision: 1.9 $'[11:-2]

from DT_Util import *
import sys

class If:
    blockContinuations='else','elif'
    name='if'
    elses=None
    expr=''

    def __init__(self, blocks):

	tname, args, section = blocks[0]
	args=parse_params(args, name='', expr='')
	name,expr=name_param(args,'if',1)
	self.__name__= name
	if expr is None: cond=name
	else: cond=expr.eval
	sections=[cond, section.blocks]

	if blocks[-1][0]=='else':
	    tname, args, section = blocks[-1]
	    del blocks[-1]
	    args=parse_params(args, name='')
	    if args:
		ename,expr=name_param(args,'else',1)
		if ename != name:
		    raise ParseError, ('name in else does not match if', 'in')
	    elses=section.blocks
	else: elses=None

	for tname, args, section in blocks[1:]:
	    if tname=='else':
		raise ParseError, (
		    'more than one else tag for a single if tag', 'in')
	    args=parse_params(args, name='', expr='')
	    name,expr=name_param(args,'elif',1)
	    if expr is None: cond=name
	    else: cond=expr.eval
	    sections.append(cond)
	    sections.append(section.blocks)

	if elses is not None: sections.append(elses)

	self.simple_form=tuple(sections)

class Unless:
    name='unless'
    blockContinuations=()

    def __init__(self, blocks):
	tname, args, section = blocks[0]
	args=parse_params(args, name='', expr='')
	name,expr=name_param(args,'unless',1)
	if expr is None: cond=name
	else: cond=expr.eval
	self.simple_form=(cond,None,section.blocks)

class Else(Unless):
    # The else tag is included for backward compatibility and is deprecated.
    name='else'


##########################################################################
#
# $Log: DT_If.py,v $
# Revision 1.9  1998/04/02 17:37:35  jim
# Major redesign of block rendering. The code inside a block tag is
# compiled as a template but only the templates blocks are saved, and
# later rendered directly with render_blocks.
#
# Added with tag.
#
# Also, for the HTML syntax, we now allow spaces after # and after end
# or '/'.  So, the tags::
#
#   <!--#
#     with spam
#     -->
#
# and::
#
#   <!--#
#     end with
#     -->
#
# are valid.
#
# Revision 1.8  1998/01/14 18:23:42  jim
# Added expr to unless.
#
# Revision 1.7  1998/01/14 18:03:25  jim
# Added Unless tag as replacement for else tag.
#
# Revision 1.6  1997/12/31 20:32:11  jim
# If and else blocks now cache variables.
#
# Revision 1.5  1997/11/07 17:08:11  jim
# Changed so exception is raised if a sequence cannot be gotten during
# rendering.
#
# Revision 1.4  1997/09/25 18:56:38  jim
# fixed problem in reporting errors
#
# Revision 1.3  1997/09/22 14:42:49  jim
# added expr
#
# Revision 1.2  1997/09/08 15:35:40  jim
# Fixed bug that caused else blocks to render if blocks.
#
# Revision 1.1  1997/08/27 18:55:42  jim
# initial
#
