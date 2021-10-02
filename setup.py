import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="torchps",
    version="1.0.1",
    author="Niklas Götz",
    author_email="goetz.niklas@protonmail.com",
    description="Phase Space Sampling with PyTorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NGoetz/TorchPS",
    project_urls={
        "Bug Tracker": "https://github.com/NGoetz/TorchPS/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires = ['torch==1.6', 'numpy==1.19.1','python-dateutil']
)
