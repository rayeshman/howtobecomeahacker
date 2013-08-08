# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1375979754.705939
_enable_loop = True
_template_filename = u'themes/default/templates/story.tmpl'
_template_uri = u'story.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


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
    return runtime._inherit_from(context, u'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context.locals_(__M_locals))
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        disqus = _mako_get_namespace(context, 'disqus')
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 12
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        disqus = _mako_get_namespace(context, 'disqus')
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        if title:
            # SOURCE LINE 6
            __M_writer(u'    <h1>')
            __M_writer(unicode(title))
            __M_writer(u'</h1>\n')
        # SOURCE LINE 8
        __M_writer(u'    ')
        __M_writer(unicode(post.text()))
        __M_writer(u'\n')
        # SOURCE LINE 9
        if enable_comments and not post.meta('nocomments'):
            # SOURCE LINE 10
            __M_writer(u'        ')
            __M_writer(unicode(disqus.html_disqus(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


