import setuptools

requires = [
    'requests>=2.22.0',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="For-MySentry-pkg-Artem2k", # Replace with your own username
    version="0.0.1",
    author="Artem2k",
    author_email="Artem2k@gamil.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)