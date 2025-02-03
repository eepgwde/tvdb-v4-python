from setuptools import find_packages, setup

VERSION = "0.9.0"
DESCRIPTION = "Unofficial tvdb api v5 package"
LONG_DESCRIPTION = "Unofficial python package for using the tvdb v4 api"

# Setting up
setup(
    name="tvdb_v5_unofficial",
    version=VERSION,
    author="Walter Eaves",
    author_email="<walter.eaves@gmx.de",
    url="https://github.com/eepgwde/tvdb-v4-python",
    description="tvdb-api-v4 utility package",
    long_description="Unofficial python client for the tvdb api v4",
    packages=find_packages(),
    install_requires=[],
    py_modules=["tvdb_v5_unofficial", "tvdb_v4_unofficial"],
    keywords=["python", "tvdb"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir={"tvdb_v5_unofficial": "tvdb_v5_unofficial", "tvdb_v4_unofficial" : "tvdb_v4_unofficial" },
    # tests_require=["pytest"],
    test_suite="tests",
    scripts=["tvdb_v5_unofficial/fetch0.py"],
)
