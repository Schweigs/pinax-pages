import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="",
    author_email="",
    description="",
    name="pinax-pages",
    long_description=read("README.rst"),
    version="0.4.2",
    url="http://pinax-pages.rtfd.org/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "pages": []
    },
    test_suite="runtests.runtests",
    tests_require=[
    ],
    install_requires=[
        "django-appconf>=1.0.1",
        "django-reversion>=1.10",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
