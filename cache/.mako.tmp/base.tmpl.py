# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1375979754.765901
_enable_loop = True
_template_filename = u'themes/site/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink', u'belowtitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x317d510', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x317d510')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x317d510')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        late_load_js = _import_ns.get('late_load_js', context.get('late_load_js', UNDEFINED))
        html_head = _import_ns.get('html_head', context.get('html_head', UNDEFINED))
        html_social = _import_ns.get('html_social', context.get('html_social', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def content():
            return render_content(context.locals_(__M_locals))
        analytics = _import_ns.get('analytics', context.get('analytics', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context.locals_(__M_locals))
        html_translations = _import_ns.get('html_translations', context.get('html_translations', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context.locals_(__M_locals))
        html_sidebar_links = _import_ns.get('html_sidebar_links', context.get('html_sidebar_links', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        def extra_head():
            return render_extra_head(context.locals_(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n<!DOCTYPE html>\n<html lang="')
        # SOURCE LINE 5
        __M_writer(unicode(lang))
        __M_writer(u'">\n<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(html_head()))
        __M_writer(u'\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 10
        __M_writer(u'\n    ')
        # SOURCE LINE 11
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n</head>\n<body>\n<!-- Menubar -->\n<div class="navbar navbar-fixed-top">\n    <div class="navbar-inner">\n        <div class="container">\n\n        <!-- .btn-navbar is used as the toggle for collapsed navbar content -->\n        <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n        </a>\n\n            <a class="brand" href="')
        # SOURCE LINE 26
        __M_writer(unicode(abs_link('/')))
        __M_writer(u'">\n            ')
        # SOURCE LINE 27
        __M_writer(unicode(blog_title))
        __M_writer(u'\n            </a>\n            <!-- Everything you want hidden at 940px or less, place within here -->\n            <div class="nav-collapse collapse">\n                <ul class="nav">\n                    ')
        # SOURCE LINE 32
        __M_writer(unicode(html_sidebar_links()))
        __M_writer(u'\n                </ul>\n')
        # SOURCE LINE 34
        if search_form:
            # SOURCE LINE 35
            __M_writer(u'                    ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n')
        # SOURCE LINE 37
        __M_writer(u'                <ul class="nav pull-right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        # SOURCE LINE 42
        __M_writer(u'\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        # SOURCE LINE 43
        __M_writer(u'\n                </ul>\n            </div>\n        </div>\n    </div>\n</div>\n<!-- End of Menubar -->\n<div class="container-fluid" id="container-fluid">\n    <!--Body content-->\n    <div class="row-fluid">\n    <div class="span2"></div>\n    <div class="span8">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 55
        __M_writer(u'\n    </div>\n    </div>\n    <!--End of body content-->\n</div>\n<div class="footerbox">\n    ')
        # SOURCE LINE 61
        __M_writer(unicode(content_footer))
        __M_writer(u'\n</div>\n')
        # SOURCE LINE 63
        __M_writer(unicode(html_social()))
        __M_writer(u'\n')
        # SOURCE LINE 64
        __M_writer(unicode(late_load_js()))
        __M_writer(u'\n')
        # SOURCE LINE 65
        __M_writer(unicode(analytics))
        __M_writer(u'\n    <script type="text/javascript">jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"80%",maxHeight:"80%",scalePhotos:true});</script>\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x317d510')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x317d510')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x317d510')._populate(_import_ns, [u'*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u' ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x317d510')._populate(_import_ns, [u'*'])
        def belowtitle():
            return render_belowtitle(context)
        html_translations = _import_ns.get('html_translations', context.get('html_translations', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 38
        __M_writer(u'\n')
        # SOURCE LINE 39
        if len(translations) > 1:
            # SOURCE LINE 40
            __M_writer(u'                    <li>')
            __M_writer(unicode(html_translations()))
            __M_writer(u'</li>\n')
        # SOURCE LINE 42
        __M_writer(u'                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


