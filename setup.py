""" Setup for Data Science application

The setup script defines the modules required to build DS projects
"""
import setuptools

with open("README.md") as fp:
    long_description = fp.read()

requirements = [
    "pandas",
    "s3fs",
    "numpy",
    "jupyter",
    "boto3",
    "pyyaml",
]

dev_requirements = [
    "autopep8",
    "pylint",
    "pytest",
    "pytest-dotenv",
    "pytest-cov",
    "pre-commit",
    "flake8",
    "coverage",
    "click",
]

setuptools.setup(
    name="uks-project",
    version="1.0.0",
    description="<< Short description of your project >>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="<< Author >>",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: Development",
        "Intended Audience :: Development Team",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
