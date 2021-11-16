import setuptools

import hello_world

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name=hello_world.__name__,
    version=hello_world.__version__,
    author=hello_world.__author__,
    author_email="13816347+rajendrakumaryadav@users.noreply.github.com",
    description="Hello World message",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajendrakumaryadav/hello_world",
    # packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "hello_world"},
    # packages=setuptools.find_packages(where="hello_world"),
    python_requires=">=3.7",
)
