"""
Setup script for installing SEA-RAFT as a package
"""

from setuptools import setup, find_packages

setup(
    name="sea_raft",
    version="0.1.0",
    description="Scene Flow Estimation using SEA-RAFT",
    author="SEA-RAFT Team",
    packages=find_packages(),
    install_requires=[
        "torch>=1.7.0",
        "numpy",
        "opencv-python",
        "matplotlib",
        "open3d",
        "pyyaml",
    ],
    python_requires=">=3.7",
)