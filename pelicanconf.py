AUTHOR = 'Fei Zhao'
SITENAME = 'FeiGeek'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Categories", "https://feigeek.com/categories.html"),
    ("All of the articles", "https://feigeek.com/archives.html"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/zhaofei2048"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# Basic settings
LOAD_CONTENT_CACHE = False
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
DELETE_OUTPUT_DIRECTORY = False
ARTICLE_PATHS = ['posts']
DISPLAY_CATEGORIES_ON_MENU = True
OUTPUT_PATH = 'docs/'
STATIC_PATHS = [
    "images",
    "extras",
    "pdfs"
]
EXTRA_PATH_METADATA = {
    "extras/CNAME": {"path": "CNAME"},
    "extras/favicon.ico": {"path": "favicon.ico"},
}
DEFAULT_DATE = 'fs'

# Order
PAGE_ORDER_BY = 'date'


# Themes
GITHUB_URL = "https://github.com/zhaofei2048"
SITESUBTITLE = "The more I share, the more I learn"
MENUITEMS = [
        ("Home", "https://feigeek.com"),
        ]
LINKS_WIDGET_NAME = "Browse"
SOCIAL_WIDGET_NAME = "Contact"
THEME = "themes/notmyidea_modified"


# Simulatine, 11 May 2020 - Added guess_lang: False to stop Markdown trying
# to incorrectly guess the language in code blocks. (https://github.com/simulatine)
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'guess_lang':False,},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}