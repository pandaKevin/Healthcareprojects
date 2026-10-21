
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for fhir.resources."""

import platform

from setuptools import find_namespace_packages, setup


# Python version detection
PY_VERSION_TUPLE = platform.python_version_tuple()
PY_MAJOR = int(PY_VERSION_TUPLE[0])
PY_MINOR = int(PY_VERSION_TUPLE[1])

PY_VERSION_9_OR_EARLIER = PY_MAJOR == 3 and PY_MINOR <= 9
PY_VERSION_10_OR_LATER = PY_MAJOR == 3 and PY_MINOR >= 10


# Read project documentation
with open("README.rst", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst", encoding="utf-8") as history_file:
    history = history_file.read()


# Core dependencies
requirements = [
    "fhir-core>=1.1.9",
]

if PY_VERSION_9_OR_EARLIER:
    requirements.append("eval-type-backport")


# Setup dependencies
setup_requirements = [
    "pytest-runner",
]


# Optional dependencies
yaml_requirements = [
    "PyYAML>=5.4.1",
]

xml_requirements = [
    "lxml",
]


# Testing dependencies
test_requirements = [
    "coverage",
    "pytest>5.4.0;python_version>='3.6'",
    "pytest-cov>=2.10.0;python_version>='3.6'",
    "requests==2.32.4",
    "black>=23.0,<24.0;python_version>='3.7'",
    "mypy",
    "types-PyYAML",
    "types-simplejson",
    "types-requests",
    "setuptools==65.6.3;python_version>='3.7'",
]

if PY_VERSION_10_OR_LATER:
    test_requirements.extend(
        [
            "flake8==7.3.0",
            "flake8-isort>=6.0.0",
            "flake8-bugbear>=22.12.6",
            "isort>=5.11.4",
            "importlib-metadata>=5.2.0",
        ]
    )
else:
    test_requirements.extend(
        [
            "flake8==5.0.4;python_version<'3.10'",
            "flake8-isort==4.2.0;python_version<'3.10'",
            "flake8-bugbear==20.1.4;python_version<'3.10'",
            "isort==4.3.21",
        ]
    )


# Development dependencies
development_requirements = [
    "Jinja2==3.1.6",
    "MarkupSafe==2.1.5",
    "colorlog==2.10.0",
    "certifi",
    "fhirspec>=0.6.0",
    "zest-releaser[recommended]",
    "twine==6.1.0",
]


# Package configuration
setup(
    name="fhir.resources",
    version="8.3.1.dev0",
    description="FHIR Resources as Model Class",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    author="Md Nazrul Islam",
    author_email="email2nazrul@gmail.com",
    license="BSD license",
    url="https://github.com/pandaKevin/Healthcareprojects",
    project_urls={
        "GitHub: issues": (
            "https://github.com/pandaKevin/"
            "Healthcareprojects/issues"
        ),
        "GitHub: repo": (
            "https://github.com/pandaKevin/"
            "Healthcareprojects"
        ),
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    keywords="fhir, resources, python, hl7, health IT, healthcare",
    packages=find_namespace_packages(
        include=["fhir*"],
        exclude=[
            "ez_setup",
            "tests",
            "fhir-parser*",
            "fhir.resources.tests",
            "fhir.resources.STU3.tests",
            "fhir.resources.R4B.tests",
        ],
    ),
    package_data={
        "fhir.resources": ["py.typed"],
    },
    include_package_data=True,
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    test_suite="tests",
    extras_require={
        "yaml": yaml_requirements,
        "xml": xml_requirements,
        "test": (
            test_requirements
            + setup_requirements
            + yaml_requirements
            + xml_requirements
        ),
        "dev": test_requirements + development_requirements,
        "all": yaml_requirements + xml_requirements,
    },
    python_requires=">=3.8",
    zip_safe=False,
)
