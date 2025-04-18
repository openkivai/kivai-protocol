from setuptools import setup, find_packages

setup(
    name="kivai-validator",
    version="0.1",
    packages=find_packages(),
    install_requires=["jsonschema"],
    description="Validator for Kivai JSON-based command schemas",
    author="OpenKivai Community",
    license="MIT",
    keywords=["kivai", "validator", "jsonschema", "iot", "commands"],
)
