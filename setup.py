from setuptools import find_packages, setup

print(find_packages(where="src"))

setup(
    name="types-h5py",
    author="Nicholas Devenish",
    version="3.3.0",
    packages=[
        "h5py-stubs",
    ],
    package_dir={"": "src"},
)
