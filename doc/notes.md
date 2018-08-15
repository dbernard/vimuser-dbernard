## Useful Packages

Until I try to hack together some setup script that will do this for me, this is
just a useful list of additional deps for this setup. Note that this is not an
extensive list, just the tools I find myself using out of all of the great tools
included in this Vim setup. This list will grow as I take advantage of more of
the plugins in this setup.

### Ubuntu
 - wmctrl
 - vim-gnome
 - exuberant-ctags

### Python
 - `python2 -m pip install flake8`

## TODO QoL Updates
 - Vim on both my Macbook and my Ubuntu 16.04 machine seems to like to come with
   +python3 support rather than +python support. This breaks stuff in UltiSnips,
   namely the import of `vim` in `AugmentPythonPath()` which lives in
   `~/.vim/vimrc`.
 - It might be useful to write something that builds Vim via drmikehenry's
   buildtool in `vimfiles`. That buildtool makes some assumptions about what
   directories are available and where the Vim source code is installed.

### Process for the above
 1. Uninstall system vim:
  - `sudo apt remove vim vim-runtime gvim`
  - `sudo apt remove vim-tiny vim-common vim-gui-common vim-nox`
 2. Create dirs assumed by `buildtool`:
  - `mkdir ~/download/programming`
  - `mkdir ~/build`
 3. Clone Vim source:
  - `git clone https://github.com/vim/vim.git ~/download/programming/`
 4. Run `buildtool`:
  - `~/.vim/buildtool update`
  - `~/.vim/buildtool build`
 5. Install the final tarball:
  - `sudo tar -C / -xf vim-8.1.0287/vim-8.1.0287.x86_64.tar.gz`

