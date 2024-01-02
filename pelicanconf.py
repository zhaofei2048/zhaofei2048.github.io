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
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/zhaofei2048"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# Basic settings
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


# Themes
GITHUB_URL = "https://github.com/zhaofei2048"
SITESUBTITLE = "The more I share, the more I learn"
MENUITEMS = [
        ("Home", "https://feigeek.com"),
        ("Categories", "https://feigeek.com/categories.html"),
        ("All", "https://feigeek.com/archives.html")
        ]

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