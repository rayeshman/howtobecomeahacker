# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1375979754.831622
_enable_loop = True
_template_filename = u'themes/default/templates/gallery.tmpl'
_template_uri = u'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'disqus', context._clean_inheritance_tokens(), templateuri=u'disqus_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'disqus')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        folders = context.get('folders', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context.locals_(__M_locals))
        def content():
            return render_content(context.locals_(__M_locals))
        crumbs = context.get('crumbs', UNDEFINED)
        text = context.get('text', UNDEFINED)
        images = context.get('images', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        disqus = _mako_get_namespace(context, 'disqus')
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        # SOURCE LINE 4
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 31
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        folders = context.get('folders', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        title = context.get('title', UNDEFINED)
        text = context.get('text', UNDEFINED)
        def content():
            return render_content(context)
        crumbs = context.get('crumbs', UNDEFINED)
        images = context.get('images', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        disqus = _mako_get_namespace(context, 'disqus')
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n    <ul class="breadcrumb">\n')
        # SOURCE LINE 8
        for link, crumb in crumbs:
            # SOURCE LINE 9
            __M_writer(u'            <li><a href="')
            __M_writer(unicode(link))
            __M_writer(u'">/ ')
            __M_writer(unicode(crumb))
            __M_writer(u'</a>\n')
        # SOURCE LINE 11
        __M_writer(u'    </ul>\n')
        # SOURCE LINE 12
        if text:
            # SOURCE LINE 13
            __M_writer(u'    <p>\n        ')
            # SOURCE LINE 14
            __M_writer(unicode(text))
            __M_writer(u'\n    </p>\n')
        # SOURCE LINE 17
        __M_writer(u'    <ul>\n')
        # SOURCE LINE 18
        for folder in folders:
            # SOURCE LINE 19
            __M_writer(u'        <li><a href="')
            __M_writer(unicode(folder))
            __M_writer(u'"><i class="icon-folder-open"></i>&nbsp;')
            __M_writer(unicode(folder))
            __M_writer(u'</a>\n')
        # SOURCE LINE 21
        __M_writer(u'    </ul>\n    <ul class="thumbnails">\n')
        # SOURCE LINE 23
        for image in images:
            # SOURCE LINE 24
            __M_writer(u'            <li><a href="')
            __M_writer(unicode(image[0]))
            __M_writer(u'" class="thumbnail image-reference" ')
            __M_writer(unicode(image[2]))
            __M_writer(u'>\n                <img src="')
            # SOURCE LINE 25
            __M_writer(unicode(image[1]))
            __M_writer(u'" /></a>\n')
        # SOURCE LINE 27
        __M_writer(u'    </ul>\n')
        # SOURCE LINE 28
        if enable_comments:
            # SOURCE LINE 29
            __M_writer(u'    ')
            __M_writer(unicode(disqus.html_disqus(None, permalink, title)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


