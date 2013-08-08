# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1375979754.809021
_enable_loop = True
_template_filename = u'themes/default/templates/index.tmpl'
_template_uri = u'index.tmpl'
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

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        date_format = context.get('date_format', UNDEFINED)
        disqus = _mako_get_namespace(context, 'disqus')
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        def content():
            return render_content(context.locals_(__M_locals))
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 22
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        disqus = _mako_get_namespace(context, 'disqus')
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        def content():
            return render_content(context)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        for post in posts:
            # SOURCE LINE 7
            __M_writer(u'        <div class="postbox">\n        <h1><a href="')
            # SOURCE LINE 8
            __M_writer(unicode(post.permalink()))
            __M_writer(u'">')
            __M_writer(unicode(post.title()))
            __M_writer(u'</a>\n        <small>&nbsp;&nbsp;\n             ')
            # SOURCE LINE 10
            __M_writer(unicode(messages("Posted")))
            __M_writer(u': <time class="published" datetime="')
            __M_writer(unicode(post.date.isoformat()))
            __M_writer(u'">')
            __M_writer(unicode(post.formatted_date(date_format)))
            __M_writer(u'</time>\n        </small></h1>\n        <hr>\n        ')
            # SOURCE LINE 13
            __M_writer(unicode(post.text(teaser_only=index_teasers)))
            __M_writer(u'\n')
            # SOURCE LINE 14
            if not post.meta('nocomments'):
                # SOURCE LINE 15
                __M_writer(u'            ')
                __M_writer(unicode(disqus.html_disqus_link(post.permalink()+"#disqus_thread", post.base_path)))
                __M_writer(u'\n')
            # SOURCE LINE 17
            __M_writer(u'        </div>\n')
        # SOURCE LINE 19
        __M_writer(u'    ')
        __M_writer(unicode(helper.html_pager()))
        __M_writer(u'\n    ')
        # SOURCE LINE 20
        __M_writer(unicode(disqus.html_disqus_script()))
        __M_writer(u'\n    ')
        # SOURCE LINE 21
        __M_writer(unicode(helper.mathjax_script(posts)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


