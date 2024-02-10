# Local Machine installation

## Prerequisites

### Python runtime setup- PyEnv

#### Linux/MacOS/WSL -> (Homebrew)

[pyenv](https://github.com/pyenv/pyenv)

```sh
brew install pyenv
```

##### Windows -> (winget)

[pyenv-win](https://pyenv-win.github.io/pyenv-win/)

```sh
winget install pyenv-win
```

### Python version

List all Python runtimes and versions. (anaconda3, jython graalpy, pypy, etc.)

```sh
pyenv install --list
```

Install Python version

```sh
pyenv install 3.11.1 # (or your desired version)
```

### Python venv

Create a virtual environment in the project's root directory.
This will isolate the project's dependencies from the system's python installation.

```zsh
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate # bash/zsh

# confirm the virtual environment is active
$ which python
/absolute/path/to/project_root/.venv/bin/python

$ which pip
/absolute/path/to/project_root/.venv/bin/pip
```

For more information on venv, see [Python venv](https://docs.python.org/3/library/venv.html)
[How venv works](https://docs.python.org/3/library/venv.html#how-venvs-work)

### Add dependencies

install dependecies and my_module in .
this allows for importing the module from tools refencing the virtual environment.

```sh
pip install -e ".[dev,test]" #install dependencies and dev and test optional-dependencies
```

`--editable .` installs `my-module` with [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html). This allows for changes to the package to be reflected in the virtual environment without re-installing the package.

the command's output generate a `.egg-info` directory in the project root. `git` will ignore this directory.

setup test
 2 passing tests, one handles an exception, the other is a simple assert.

## Activate git hooks for project

[autohooks](https://github.com/greenbone/autohooks) taps into git's lifecycle events to run scripts.
This allows for running scripts before or after git commands.
See pyproject.toml

```sh
$ autohooks check
 × autohooks pre-commit hook not active. Please run 'autohooks activate'.

#activate
autohooks activate

#confirm
$ autohooks check
 ✓ autohooks pre-commit hook is active.
 ✓ autohooks pre-commit hook is up-to-date.
 ℹ Using autohooks mode "pythonpath".
 ✓ Plugin "autohooks.plugins.black" active and loadable.
 ✓ Plugin "autohooks.plugins.isort" active and loadable.
 ✓ Plugin "autohooks.plugins.pytest" active and loadable.
 ✓ Plugin "autohooks.plugins.ruff" active and loadable.
```
