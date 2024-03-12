__kupfer_name__ = _("Search My Notes")
__kupfer_actions__ = (
        "SearchNotes",
    )
__description__ = _("Search my notes and logs")
__version__ = ""
__author__ = "thorko"

import subprocess

from kupfer.obj import Action, Source, TextLeaf, FileLeaf
from kupfer import icons, plugin_support
from kupfer.support import kupferstring

__kupfer_settings__ = plugin_support.PluginSettings(
        {
            "key": "paths_to_search",
            "label": _("paths to search seperated by space"),
            "type": str,
            "value": "",
        }
)

class SearchNotes (Action):
    def __init__(self):
        Action.__init__(self, _("Search my notes"))

    def is_factory(self):
        return True
    def activate(self, leaf):
        return SearchMyNotes(leaf.object)
    def item_types(self):
        yield TextLeaf

    def get_description(self):
        return _("Search my notes")
    def get_gicon(self):
        return icons.ComposedIcon("gnome-terminal", self.get_icon_name())
    def get_icon_name(self):
        return "edit-find"

class SearchMyNotes (Source):
    def __init__(self, query):
        Source.__init__(self, name=_('Results for "%s"') % query)
        self.query = query

    def repr_key(self):
        return self.query

    def get_items(self):
        paths = __kupfer_settings__["paths_to_search"]
        grep_command = ("/usr/bin/grep -liER '%s' %s" % (self.query, paths))
        p1 = subprocess.Popen(grep_command, shell=True, stdout=subprocess.PIPE)

        def get_locate_output(proc, offset=0):
            out, ignored_err = proc.communicate()
            return (FileLeaf(kupferstring.fromlocale(f)) for f in out.split(b'\n')[offset:-1])

        for F in get_locate_output(p1, 0):
            yield F

    def get_gicon(self):
        return icons.ComposedIcon("gnome-terminal", self.get_icon_name())
    def get_icon_name(self):
        return "edit-find"
