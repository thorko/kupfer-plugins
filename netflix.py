__kupfer_name__ = _("Netflix")
__kupfer_sources__ = ("Netflix",)
__kupfer_actions__ = ("Watch", )
__description__ = _("Search Netflix")
__version__ = "2018-9"
__author__ = "thorko"

import os
from kupfer.obj import Action, TextLeaf, Source
from kupfer import launch, plugin_support, config

_ALTERNATIVES = (
        "google-chrome-stable",
        "chromium",
        "firefox",
        "vivaldi-stable",
)

__kupfer_settings__ = plugin_support.PluginSettings(
        {
            "key" : "browser_type",
            "label": _("Your browser to use"),
            "type": str,
            "value": "google-chrome-stable",
            "alternatives": _ALTERNATIVES,
        },
        {
            "key": "config_file",
            "label": _("Your netflix series file"),
            "type": str,
            "value": "~/netflixseries"
        }
)

class Netflix (Source):
    source_use_cache = False
    source_user_reloadable = True
    def __init__(self):
        super().__init__(__kupfer_name__)
        self.mark_for_update()

    def finalize(self):
        pass

    def is_dynamic(self):
        return True

    def get_items(self):
        series = {}
        netflix_config = os.path.expanduser(__kupfer_settings__['config_file'])
        file = open(netflix_config, "r")
        for x in file.readlines():
            s = x.split("=")
            series[s[0]] = s[1].strip("\n")
        return[Series(value,key) for key, value in series.items()]
        #return[TextLeaf(value, name=key) for key, value in series.items()]

    def provides(self):
        yield TextLeaf

    def get_gicon(self):
        return "visibility"

    def description(self):
        return __description__

    def get_icon_name(self):
        return "visibility"


class Series (TextLeaf):
    def __init__(self, value, key):
        TextLeaf.__init__(self, value, name=key)

    def get_icon_name(self):
        return "geany-build"


class Watch (Action):
    def __init__(self):
        Action.__init__(self, _("Watch"))

    def activate(self, leaf):
        browser_type = __kupfer_settings__["browser_type"]
        searchnetflix = [browser_type, 'https://www.netflix.com/%s' % leaf.object]
        launch.spawn_async(searchnetflix)
#
    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search netflix with your browser")

    def get_icon_name(self):
        return "visibility"
