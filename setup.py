from setuptools import find_packages, setup
from pathlib import Path

here = Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="example_package",
    version="0.0.1",
    packages=find_packages(where="src"),  # Required

    # Although license is not necessary, it's good to add one
    # Don't forget to include the license in MANIFEST.in
    license='MIT',

    # Below are optional metadata, but in case of this package it's necessary
    author="Jakub Kazimierczak",  # Optional
    description="A packaging example",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Required for all formats except .rst
    python_requires=">=3.6",

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={"": "src"},  # Optional

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={  # Optional
        "my_pkg": ["config.yml"],
    },

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    install_requires=["pyyaml"],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    entry_points={  # Optional
        "console_scripts": [
            "example_package=my_pkg.__main__:main",
        ],
    },
)