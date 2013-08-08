# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1375979754.754872
_enable_loop = True
_template_filename = u'themes/default/templates/disqus_helper.tmpl'
_template_uri = u'disqus_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_disqus_link', 'html_disqus', 'html_disqus_script']


# SOURCE LINE 2

import json
translations = {
    'es': 'es_ES',
}


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n\n\n')
        # SOURCE LINE 43
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_disqus_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        disqus_forum = context.get('disqus_forum', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n    <p>\n')
        # SOURCE LINE 33
        if disqus_forum:
            # SOURCE LINE 34
            __M_writer(u'        <a href="')
            __M_writer(unicode(link))
            __M_writer(u'" data-disqus-identifier="')
            __M_writer(unicode(identifier))
            __M_writer(u'">Comments</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_disqus(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        disqus_forum = context.get('disqus_forum', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer(u'\n')
        # SOURCE LINE 9
        if disqus_forum:
            # SOURCE LINE 10
            __M_writer(u'        <div id="disqus_thread"></div>\n        <script type="text/javascript">\n        var disqus_shortname ="')
            # SOURCE LINE 12
            __M_writer(unicode(disqus_forum))
            __M_writer(u'";\n')
            # SOURCE LINE 13
            if url:
                # SOURCE LINE 14
                __M_writer(u'            var disqus_url="')
                __M_writer(unicode(url))
                __M_writer(u'";\n')
            # SOURCE LINE 16
            __M_writer(u'        var disqus_title=')
            __M_writer(unicode(json.dumps(title)))
            __M_writer(u';\n        var disqus_identifier="')
            # SOURCE LINE 17
            __M_writer(unicode(identifier))
            __M_writer(u'";\n        var disqus_config = function () {\n            this.language = "')
            # SOURCE LINE 19
            __M_writer(unicode(translations.get(lang, lang)))
            __M_writer(u'";\n        };\n        (function() {\n            var dsq = document.createElement(\'script\'); dsq.type = \'text/javascript\'; dsq.async = true;\n            dsq.src = \'http://\' + disqus_shortname + \'.disqus.com/embed.js\';\n            (document.getElementsByTagName(\'head\')[0] || document.getElementsByTagName(\'body\')[0]).appendChild(dsq);\n        })();\n    </script>\n    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_disqus_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        disqus_forum = context.get('disqus_forum', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n')
        # SOURCE LINE 40
        if disqus_forum:
            # SOURCE LINE 41
            __M_writer(u'       <script type="text/javascript">var disqus_shortname="')
            __M_writer(unicode(disqus_forum))
            __M_writer(u'";(function(){var a=document.createElement("script");a.async=true;a.type="text/javascript";a.src="http://"+disqus_shortname+".disqus.com/count.js";(document.getElementsByTagName("HEAD")[0]||document.getElementsByTagName("BODY")[0]).appendChild(a)}());</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


