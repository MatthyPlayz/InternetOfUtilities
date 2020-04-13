import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="internet-of-utilities-matthyno", # Replace with your own username
    version="1.0.0",
    author="matthyno",
    author_email="cjmatthy200@gmail.com",
    description="A utility package with various things in it.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/cjmatthy200/InternetOfUtilities/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
