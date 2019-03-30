from setuptools import setup, find_packages


setup(
    name = "pinax-utils",
    version = "1.0b1.dev3",
    author = "Brian Rosner",
    author_email = "brosner@gmail.com",
    description = "a Pinax utility app",
    long_description = open("README.md").read(),
    license = "MIT",
    url = "http://github.com/pinax/pinax-utils",
    packages = find_packages(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)