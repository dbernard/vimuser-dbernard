#!/usr/bin/env python
# vim:set fileencoding=utf8:

from sniputil import bsnip


#############
# MagicMock #
#############
bsnip('patch', 'MagicMock @patch', r'''
@patch('${1:object}')
''')

###########
# Testing #
###########
bsnip('test', 'def test_...(self)', r'''
def test_${1:funcname}(self):
    pass
''', aliases=['t', 'tc'])
