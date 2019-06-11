### My Kupfer Plugins

#### Internet Search
this plugin searches the internet with your favorite search engine

#### Vivaldi Bookmarks
the plugin will import your Vivaldi Bookmarks to Kupfer

#### RecollIndex
Install recollindex and use this plugin to query recoll

#### KDE5 Session Management
This plugin will add Restart, Suspend, Save Session... for KDE Plasma to Kupfer

#### SSH Yakuake Session
This plugin starts a new SSH sessin in yakuake

Set your config file in the plugin settings

```
<hostname>
<hostname>
# or
<shortname>=<hostname>
tk=thorko.de
```

#### Dict.cc Translation
This plugin will translate text german<->english

#### Amazon search
This plugin lets you search amazon directly

#### Netflix
Watch your favorite series on netflix

Set your config file in the plugin settings

```
<serie>=<url after netflix.com/>
Bugs Bunny=title/2392229
```

### Installation
put these files to kupfer/plugin directory and restart kupfer

normally this would be $HOME/.local/share/kupfer/plugins

enable them in the preference window

#### Kli
grep a path for pattern and display files which contain
this pattern
paths_to_search = your search path to use grep for
will be used in grep
```
grep -ilR "<pattern>" /home/thorko/tmux/*.log
```
