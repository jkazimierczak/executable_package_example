# Objective
The goal of this project is to:
* learn basic of packaging
* create an installable and executable package
* include other files (like configs, or other data)

# How to create a package from existing project
The example package is simple:
* read content of YAML file (config.yml)
* parse it with external package `pyyaml`
* output parsed YAML to console

This is our existing project structure. We will make it **installable** and 
**executable** for everyone, who has Python installed on their system.
```
packaging_example
│   Pipfile
│   Pipfile.lock
│   README.md
│
└───src
    └───my_pkg
        │   config.yml
        │   __init__.py
        │   __main__.py
```
> This project is located in /src subdirectory. If you want to see
> an example where my_pkg is located directly in the project root,
> take a look at `no_src_dir` branch. The only difference is in 
> `setup.py` and it's very minimal compared to below instructions.

> A `Pipfile` and it's `.lock` files are present as I'm using pipenv 
> for managing dependencies. A standard equivalent of it is a 
> `requirements.txt`. These files are not necessary for creating an
> installable python package.

## Create essentials files
To create an installable package we need following files: 
* `setup.py` - contains metadata about our package
* `pyproject.toml` - although it's optional, docs state it is better 
  to be explicit and create this file

These files are optional, but it's nice to add them: 
* `README.md` - a long description of our program
* `LICENSE` - a file containing license information

## Configuring metadata
> This section, as well as my `setup.py` is based on [this](https://github.com/pypa/sampleproject/blob/main/setup.py)
> `setup.py`

To give `setuptools` some information about our project it's necessary
to create a `setup.py` or `setup.cfg`. This guide covers the former,
but the latter is preferred in [docs](https://packaging.python.org/tutorials/packaging-projects/#configuring-metadata).

### Absolute minimum
`setup.py` expects us to provide at least name, version and packages:
```python
from setuptools import find_packages, setup

setup(
    name="example_package",
    version="0.0.1",
    packages=find_packages(where="src")
)
```
`name` is what pip/pipx will search for - both during installation,
listing or uninstalling.
### We need more metadata 
Of course this bare minimum is too little to create an installable,
runnable package. We need a little more "metadata":
```python
# Add this to setup()
package_dir={"": "src"},
package_data={
    "my_pkg": ["config.yml"],
},
install_requires=["pyyaml"],
entry_points={
    "console_scripts": [
        "example_package=my_pkg.__main__:main",
    ],
}
```
Let's explain this line by line:
1. `package_dir` - it's necessary to specify, as our package code is in
   a subdirectory under the project root.
2. `package_data` - it tells `setuptools` which files from our package,
   that aren't python files, should be included in final installation.
3. `install_requires` - here we specify dependencies necessary for our
   package to work. Package names are the same as in `requirements.txt`
   or `Pipfile`.
4. `entry_points` - it's used to specify executable scripts, that will
   be available for end user after installation. Basically - it's an 
   entry point to our program. 
   
> `entrypoints` command names can be different from `name`. In my 
> opinion though, it can lead to unnecessary confusion.
   
### Add short and long description
It would be nice if someone knew what our program does by reading it's
description. In `setup.py` we can add these fields:
```python
from pathlib import Path

here = Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

# Add this to setup()
description="A packaging example",
long_description=long_description
```

### Add license
This one is rather self-explainable.
```python
# Add this to setup()
license='MIT'
```

### Accessing resources (files, data etc.)
When using packages, it's best to use [`ResourceManager API`](https://setuptools.readthedocs.io/en/latest/pkg_resources.html#resourcemanager-api),
as paths are no longer "that predictable":

That's why in `__main__.py` you will see this code:
```python
def main():
    config_file = pkg_resources.resource_filename(__name__, 'config.yml')
    with open(config_file) as f:
        config = yaml.safe_load(f)
        print(config)
```
Instead of this:
```python
def main():
    with open('src/my_pkg/config.yml') as f:
        config = yaml.safe_load(f)
        print(config)
```
The latter won't work and will result in `FileNotFoundError`:
```
FileNotFoundError: [Errno 2] No such file or directory: 'src/my_pkg/config.yml'
```

# How to install
After taking necessary steps, you can finally install your package.
As it's an executable package with its own dependency (`pyyaml`), to
avoid possible conflicts, I will use `pipx` for installation.
```bash
# Install directly from project directory root
pipx install .

# Install From GitHub repository
pipx install git+https://github.com/jakubkazimierczak/executable_package_example.git
```
After the installation of my example, you will be able to run the
script from your console by issuing `example_package` command (that's
the name we used in `setup.py` in `entry_points`).
```bash
$ example_package
{'spam': 'eggs'}
```
## How to uninstall
To uninstall a package, we refer to the `name` specified in `setup.py`:
```bash
pipx uninstall example_package
```
