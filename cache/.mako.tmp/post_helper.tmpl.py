# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1375979754.734794
_enable_loop = True
_template_filename = u'themes/default/templates/post_helper.tmpl'
_template_uri = u'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_title', 'html_tags', 'html_pager', 'twitter_card_information', 'html_translations', 'mathjax_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n\n\n')
        # SOURCE LINE 19
        __M_writer(u'\n\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 65
        __M_writer(u'\n\n')
        # SOURCE LINE 71
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        link = context.get('link', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n    <h1>')
        # SOURCE LINE 3
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n')
        # SOURCE LINE 4
        if link:
            # SOURCE LINE 5
            __M_writer(u"            <p><a href='")
            __M_writer(unicode(link))
            __M_writer(u"'>")
            __M_writer(unicode(messages("Original site")))
            __M_writer(u'</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 23
        if post.tags:
            # SOURCE LINE 24
            __M_writer(u'        &nbsp;&nbsp;|&nbsp;&nbsp;')
            __M_writer(unicode(messages("More posts about")))
            __M_writer(u'\n')
            # SOURCE LINE 25
            for tag in post.tags:
                # SOURCE LINE 26
                __M_writer(u'            <a class="tag" href="')
                __M_writer(unicode(_link('tag', tag)))
                __M_writer(u'"><span class="badge badge-info">')
                __M_writer(unicode(tag))
                __M_writer(u'</span></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n    <ul class="pager">\n')
        # SOURCE LINE 33
        if post.prev_post:
            # SOURCE LINE 34
            __M_writer(u'        <li class="previous">\n            <a href="')
            # SOURCE LINE 35
            __M_writer(unicode(post.prev_post.permalink()))
            __M_writer(u'">&larr; ')
            __M_writer(unicode(messages("Previous post")))
            __M_writer(u'</a>\n')
        # SOURCE LINE 37
        if post.next_post:
            # SOURCE LINE 38
            __M_writer(u'        <li class="next">\n            <a href="')
            # SOURCE LINE 39
            __M_writer(unicode(post.next_post.permalink()))
            __M_writer(u'">')
            __M_writer(unicode(messages("Next post")))
            __M_writer(u' &rarr;</a>\n')
        # SOURCE LINE 41
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n')
        # SOURCE LINE 45
        if twitter_card and twitter_card['use_twitter_cards']:
            # SOURCE LINE 46
            __M_writer(u'        <meta name="twitter:card" content="')
            __M_writer(unicode(twitter_card.get('card', 'summary')))
            __M_writer(u'">\n        <meta name="og:url" content="')
            # SOURCE LINE 47
            __M_writer(unicode(post.permalink(absolute=True)))
            __M_writer(u'">\n')
            # SOURCE LINE 48
            if 'site:id' in twitter_card:
                # SOURCE LINE 49
                __M_writer(u'            <meta name="twitter:site:id" content="')
                __M_writer(unicode(twitter_card['site:id']))
                __M_writer(u'">\n')
                # SOURCE LINE 50
            elif 'site' in twitter_card:
                # SOURCE LINE 51
                __M_writer(u'            <meta name="twitter:site" content="')
                __M_writer(unicode(twitter_card['site']))
                __M_writer(u'">\n')
            # SOURCE LINE 53
            if 'creator:id' in twitter_card:
                # SOURCE LINE 54
                __M_writer(u'            <meta name="twitter:creator:id" content="')
                __M_writer(unicode(twitter_card['creator:id']))
                __M_writer(u'">\n')
                # SOURCE LINE 55
            elif 'creator' in twitter_card:
                # SOURCE LINE 56
                __M_writer(u'            <meta name="twitter:creator" content="')
                __M_writer(unicode(twitter_card['creator']))
                __M_writer(u'">\n')
            # SOURCE LINE 58
            __M_writer(u'        <meta name="og:title" content="')
            __M_writer(unicode(post.title()[:70]))
            __M_writer(u'">\n')
            # SOURCE LINE 59
            if post.description():
                # SOURCE LINE 60
                __M_writer(u'            <meta name="og:description" content="')
                __M_writer(unicode(post.description()[:200]))
                __M_writer(u'">\n')
                # SOURCE LINE 61
            else:
                # SOURCE LINE 62
                __M_writer(u'            <meta name="og:description" content="')
                __M_writer(unicode(post.text(strip_html=True)[:200]))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11
        if len(translations) > 1:
            # SOURCE LINE 12
            for langname in translations.keys():
                # SOURCE LINE 13
                if langname != lang and post.is_translation_available(langname):
                    # SOURCE LINE 14
                    __M_writer(u'                &nbsp;&nbsp;|&nbsp;&nbsp;\n                <a href="')
                    # SOURCE LINE 15
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'">')
                    __M_writer(unicode(messages("Read in English", langname)))
                    __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 67
        __M_writer(u'\n')
        # SOURCE LINE 68
        if post.is_mathjax:
            # SOURCE LINE 69
            __M_writer(u'        <script src="/assets/js/mathjax.js" type="text/javascript"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


