import platform
from setuptools import setup, find_packages
import os

# Define package metadata
package_name = "CRMS2Map"
version = "1.0"
description = "A package for CRMS2Map data processing and analysis"
long_description = open("README.md").read()
url = "https://github.com/jinikeda/CRMS2Map"
author = "Jin Ikeda"
license_type = "MIT License"
install_requires = [
    "gdal",
    "numpy",
    "pandas",
    "geopandas",
    "rasterio",
    "scipy",
    "matplotlib-base",
    "seaborn",
    "basemap",
    "rioxarray",
    "click",
]

# ## Determine the platform and make platform-specific adjustments
# if platform.system() in ['Darwin', 'Linux', 'Ubuntu']:
#     # Proper installation for Mac and Linux
#     crms_script = 'src.bin.crms'
# elif platform.system() == 'Windows':
#     import shutil
#     crms_script = 'src.bin.crms_script'
#     crms_win_script = 'src.bin.crms_win'
#     shutil.copyfile(crms_script.replace('.', '/'), crms_win_script.replace('.', '/') + '.py')
#     crms_script = crms_win_script
# else:
#     raise OSError(f"Unsupported platform: {platform.system()}")

# Ensure README.md is present
if not os.path.exists("README.md"):
    long_description = description  # Fallback if README.md is missing

# Setup configuration
setup(
    name=package_name,
    version=version,
    packages=find_packages(include=['src', 'tests']),  # Include both src and tests packages
    package_dir={
        "tests": "tests",  # Map the tests package to the tests directory
        "src": "src",  # Map the src package to the src directory
    },
    install_requires=install_requires,
    # tests_require=['pytest'],
    # test_suite='tests',
    entry_points={
        "console_scripts": [
            "CRMS2Map=src.click_main:click_main",
        ],
    },
    author=author,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    license=license_type,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
