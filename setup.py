from setuptools import find_packages, setup

setup(
    name="aoc19",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author='Gabriel Reis',
    author_email='gabrielcnr@gmail.com',
    description='Advent of Code 2019 solutions',
    license='MIT',
    python_requires=">=3.8",
)
