
# Environment Setup

These docs support OSX and Debian based OS's only from Debian 8 Jessie onwards (this would include Ubuntu 14.04LTS onwards), but instructions should map easily to other distrubutions.

## Dev Environment Requirements

### OSX

These are only necessary for OS X devs. You will need Xcode, Xcode command line
tools, and brew.

For some completely unfathomable reason, OS X does not ship with the GCC
compiler installed. And for further unfathomable reasons, it is bundled with
XCode, which is over a GB in size and not installed by default. The upshot is,
to get [brew](http://mxcl.github.io/homebrew/) to work, you need both Xcode and
[Xcode command line
tools](http://stackoverflow.com/questions/9329243/xcode-4-4-command-line-tools)
installed. Start the Xcode download early, it can take an hour or more
depending on your connection!

Next, install [brew](http://mxcl.github.io/homebrew/)!

Install the `wget` tool, which is not installed on OS X by default:

- `brew install wget`

## Python

Ensure you have python3 installed and ready to use. All `python` commands below assume `python3`.

### OSX

`brew install pyenv`
`pyenv install <latest>` (where latest is the latest version, can be determined running `pyenv install -l`)
`pyenv global <latest>` (set global version default)
`pyenv version` (to verify it worked)

add the following to your `.zshrc` or `.bash_profile`

```
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
fi
```

## Pip and Virtualenv

Pip is Python's package manager, and virtualenv is a tool that lets you create
self-contained environments for sets of python libraries.

Each virtualenv contains its own install of pip, but you need pip to be
installed globally in order to install virtualenv and virtualenvwrapper (or, at
least, this is the easiest way to get those dependencies).

Install pip following instructions at https://pip.pypa.io/en/latest/installation/.

optionally verify your install
- `pip --version`

Decide on a virtual environment manager. python 3.3+ includes `venv` by
default. alternatively, you can also use `virtualenv` and (if you want to stay
sane) `virtualenvwrapper`.

## Node

### OSX

Install Node and NPM from https://nodejs.org/en/download/

### Debian
Install npm e.g. as per https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-debian-

## Required Libs:

### Debian

(Possibly deprecated??)

`sudo apt-get install python-dev libxslt-dev libxml2-dev node-less`

## Supporting Services

### PostgreSQL

OSX: `brew update; brew install postgresql`

Debian: `sudo apt-get install postgresql libpq-dev`

## Hooray!

Now you can follow the directions in [how-to-run](how-to-run.md)
