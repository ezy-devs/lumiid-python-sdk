from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="lumiid",
    version="0.1.0",
    description="Python SDK for the LumiID Identity Verification API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Emmanuel Nzorov",                                        # your real name
    author_email="nzorovemmanue@gmail.com",                            # your real email
    url="https://github.com/ezy-devs/lumiid-python-sdk",      # your actual repo URL
    packages=find_packages(exclude=["tests*"]),                # exclude tests from package
    install_requires=["requests>=2.28.0"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="lumiid identity verification KYC KYB anti-fraud NIN BVN CAC Nigeria",
)