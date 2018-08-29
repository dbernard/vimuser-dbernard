#!/usr/bin/env python
# vim:set fileencoding=utf8:

from sniputil import bsnip

##########
# Django #
##########
bsnip('setUpTestData', 'Django testing setUpTestData', r'''
@classmethod
def setUpTestData(cls)
    super(${1:classname}, cls).setUpTestData()
    ${2:setup}
''', aliases=['setuptestdata'])

bsnip('setUp', 'Django testing setUp', r'''
def setUp(self):
    super(${1:class}, self).setUp()
    ${2:setup}
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
    pass
''', aliases=['t', 'tc'])
