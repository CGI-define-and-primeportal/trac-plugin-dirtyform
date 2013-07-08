# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 Logica
#

from trac.web.api import IRequestFilter, ITemplateStreamFilter
from trac.core import Component, implements
from trac.web.chrome import ITemplateProvider, add_script, add_stylesheet

from pkg_resources import resource_filename

class DirtyFormModule(Component):
    implements(IRequestFilter, ITemplateProvider, ITemplateStreamFilter)

    # IRequestFilter methods
    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, content_type):
        return (template, content_type)

    def post_process_request(self, req, template, data, content_type):
        return (template, data, content_type)

    # ITemplateProvider methods

    def get_htdocs_dirs(self):
        return [('dirtyform', resource_filename(__name__, 'htdocs'))]

    def get_templates_dirs(self):
        return []
    
    ## ITemplateStreamFilter
    
    def filter_stream(self, req, method, filename, stream, data):
        if filename == "ticket.html":
            add_stylesheet(req, "dirtyform/css/dirtyform.css")
            add_script(req, "dirtyform/js/jquery.dirtyform.js")
            add_script(req, "dirtyform/js/stoppers.js")

            add_script(req, "dirtyform/js/ticket.js")
        elif filename == "wiki_edit.html":
            add_stylesheet(req, "dirtyform/css/dirtyform.css")
            add_script(req, "dirtyform/js/jquery.dirtyform.js")
            add_script(req, "dirtyform/js/stoppers.js")
            
            add_script(req, "dirtyform/js/wiki.js")

        return stream
  
