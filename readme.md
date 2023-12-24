# Python template repository

## Configure

### Rename

1. Change code folder name from `new_python/` to `your_project_name`;  (snake_case_lowercase)
2. In `pyproject.toml`, change`name` under `tool.poetry` to `your-project-name`; (kebab-case-lowercase)
3. (**Optional**) Change Python version in `pyproject.toml` under `tool.poetry.dependencies.python` to your desired version.

## Installation

### Python runtime - PyEnv

```sh
brew install pyenv
pyenv install 3.12.1 # (or your desired version)
```

### Package Management - Poetry

#### HomeBrew

```sh
brew install poetry
```

#### pipx

```sh
brew install pipx
pipx ensurepath
pipx install poetry
```

#### Install poetry dependencies and `.venv`

```sh
# in project root
poetry install
```
