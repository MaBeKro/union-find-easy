import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="union-find-easy-nikanj",
    version="0.0.1",
    description="implementation of the union find data structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaBeKro/union-find-easy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # this does not work nicely, use tox instead
    # tests_require=["pytest"],
    # test_suite="tests",
    python_requires='>=3.6',
)