"""
Module: Barcode Printer URLS
Project: Adlibre DMS
Copyright: Adlibre Pty Ltd 2012
License: See LICENSE for license information
"""

from django.conf.urls.defaults import *

import mdtui.views

urlpatterns = patterns('bcp.views',
    url(r'^(?P<barcode_type>(Standard39|Code128))/(?P<code>[\w-]+)$', 'generate', name='bcp-generate'),
    url(r'^(?P<barcode_type>(Standard39|Code128))/(?P<code>[\w-]+)/print$', 'print_barcode', name='bcp-print'),
    url(r'^(?P<barcode_type>(Standard39|Code128))/(?P<code>[\w-]+)/test', 'print_barcode_embed_example', name='bcp-embed-example'),

)