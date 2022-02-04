from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="mypackage",
        description="this is mypackage description",
        license="MIT",
        url="https://github.com/SebastianBelmonte95/mypackage",
        version="0.0.1",
        author="Sebastian Belmonte",
        author_email="sebastian@email.com",
        long_description=open("README.md").read(),
        packages=find_packages(),
        zip_safe=False,
        install_requires=[],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
        ],
    )
