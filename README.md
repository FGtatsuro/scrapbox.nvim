scrapbox.nvim
==================================================

Neovim plugin to access Scrapbox(<https://scrapbox.io/>).

Requirements
------------

The dependencies on other softwares/libraries for this project. 
This software may work even if these requirements aren't met, but the behavior on that case can't be supported officially.

- Neovim (>= 0.3.x)
- Python (>= 3.7.x)

How to
------

1. Set an URL of your Scrapbox project to a variable `g:scrapbox#project_url`.

```vim
let g:scrapbox#project_url = "https://scrapbox.io/your_project_url"
```

2. Access a scrapbox page via `ScrapboxAccessPage` command.
   The page with given name is opend via Webbrowser.

```
# In Neovim
# With title
:ScrapboxAccessPage vim

# With title and body
:ScrapboxAccessPage vim 本文
```

Development
-----------

1. Start Neovim with a config file and an environment variable `SCRAPBOX_PROJECT_URL` to load a plugin of this project.

```bash
# FYI: https://github.com/neovim/python-client/blob/master/docs/usage/remote-plugins.rst
$ SCRAPBOX_PROJECT_URL='https://scrapbox.io/your_project_url' nvim -u tests/vimrc
```

2. Update the remote plugin manifest, and check futures of your plugin.

```
# In Neovim
:UpdateRemotePlugins
:(Run plugin's command/function/mapping and so on)
```
