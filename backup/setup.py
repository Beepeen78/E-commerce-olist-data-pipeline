from setuptools import setup, find_packages

setup(
    name="ecommerce_oltp",
    version="0.1",
    packages=find_packages(include=['ecommerce_oltp*']),
    package_dir={"": "."},
    install_requires=[
        'sqlalchemy>=2.0.0',
        'pandas>=1.5.0', 
        'streamlit>=1.15.0'
    ],
    python_requires=">=3.8"
)
