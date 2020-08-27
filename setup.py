from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as f:
    readme = f.read()

setup(name="color_pallete",
    author="SnowballSH, one-wq, 12944qwerty",
    version="0.0",
    description="A color palette module",
    long_description=readme,
    long_description_content_type="text/md",
    install_requires=requirements,
    python_requires=">=3.6"
)
