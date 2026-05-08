from setuptools import setup, find_packages

# Explicit package discovery for compatibility with older setuptools (<61)
# that do not support PEP 621 auto-discovery from pyproject.toml src layout.
setup(
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
        "shibuya": [
            "theme/**/*",
            "locale/*/LC_MESSAGES/*",
        ],
    },
)
