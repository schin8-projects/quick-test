

# template_python_basic

Basic Python Config for re-use



## Getting Started

### Setup bash/zsh

add these to your startup script

```bash
alias npm-exec='PATH=$(npm bin):$PATH'
export AWS_PROFILE="dev"
```

The alias npm-exec will to install and run npm installed modules from the working directory

### [optional] using virtual environments

Initial prep

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Before coding

```bash
source venv/bin/activate
```

Leaving the virtual env

```bash
deactivate
```

## AWS SSO
There is an auto timeout depending on your Role (1 hr for admins)

```bash
aws sso login --profile $AWS_PROFILE
# or
export AWS_PROFILE=dev && aws sso login --profile $AWS_PROFILE
```

## Visual Studio Code

### Extentions

- Python Test Explorer for Visual Studio Code

### Debugging

Add a Launch configuration in the `.vscode` folder

Examples

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Python: management_account.app",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/management_account/app.py",
            "cwd": "${workspaceFolder}/management_account",
            "console": "integratedTerminal"
        }
    ]
}
```

## Code Beautify

Open your VSCode settings, by going 'Code -> Preferences -> Settings'.</br>
Search for "python formatting provider" and select  the formatter you prefer from the dropdown menu:

The requirements.txt file installs `yapf`, so you can use that if you want.

### Linting

From The  vscode `Command Pallet` select "Python: Select linter" and select pylons.

## Testing

#### Pytest

Use pylint from the command line

```bash
pytest -o log_cli=true
```

**Pytest config file**

Adding the options to a configuration file

pyproject.toml

```toml
[tool.pytest.ini_options]
log_cli = true
log_cli_level = "INFO"
log_cli_format = "%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)"
log_cli_date_format = "%Y-%m-%d %H:%M:%S"
```

**Using Nodemon**

```bash
nodemon --ext py --exec "pytest test"
```

## Recovery

### Cleanup

```bash
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

