#!/usr/bin/env python
# vim:set fileencoding=utf8:

from sniputil import bsnip
from sniputil import wsnip

###########
# General #
###########

wsnip('lc', 'List comprehension', r'''
[${1:x} for ${2:x} in ${3:iter}]
''')

bsnip('def', 'Define function', r'''
def ${1:func_name}(${2:args}):
    ${3:pass}
''')

##########
# Django #
##########
bsnip('setUpTestData', 'Django testing setUpTestData', r'''
@classmethod
def setUpTestData(cls):
    super(${1:classname}, cls).setUpTestData()
    ${2:setup}
''', aliases=['setuptestdata'])

bsnip('setUp', 'Django testing setUp', r'''
def setUp(self):
    super(${1:class}, self).setUp()
    ${2:setup}
''')

wsnip('filter', 'Django filter objects', r'''
${1:model}.objects.filter(${2:fields})
''')

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
    ${2:pass}
''', aliases=['t', 'tc'])
