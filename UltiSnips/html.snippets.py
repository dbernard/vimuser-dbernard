#!/usr/bin/env python
# vim:set fileencoding=utf8: #

from sniputil import wsnip

####################
# Django Templates #
####################
wsnip('{{', 'Django template var', r'''
{{ ${1:variable} }}
''')

wsnip('{%', 'Django logic tag', r'''
{% ${1:expression} %}
''')

wsnip('{{|', 'Django filter', r'''
{{ ${1:variable}|${2:filter} }}
''')
