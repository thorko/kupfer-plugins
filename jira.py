__kupfer_name__ = _("Jira")
__kupfer_actions__ = ("JiraSearch", )
__description__ = _("Search your jira for issue")
__version__ = "2021-10"
__author__ = "thorko"

import http.client

from kupfer.objects import Action, TextLeaf
from kupfer import utils, plugin_support


__kupfer_settings__ = plugin_support.PluginSettings(
        {
            "key": "jira_url",
            "label": _("Your Jira URL"),
            "type": str,
            "value": "https://jira.org",
        }
)


class JiraSearch (Action):
    def __init__(self):
        Action.__init__(self, _("Jira"))

    def activate(self, leaf):
        search_url = __kupfer_settings__["jira_url"]
        query_url = search_url + "/browse/" + leaf.object
        utils.show_url(query_url)

    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search your jira for issue")

    def get_icon_name(self):
        return "web-browser"
