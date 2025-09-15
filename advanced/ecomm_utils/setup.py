from setuptools import setup, find_packages

setup(
    name="ecomm-utils",  # 🔹 this is the pip package name
    version="0.1.0",
    description="E-commerce helper package for discounts, carts, and orders",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Arun",
    author_email="csemanit2015@gmail.com",
    url="https://github.com/yourgithub/ecomm-utils",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",        
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
