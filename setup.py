# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os

import setuptools
from setuptools import setup, find_packages

name = "google-cloud-audit-log"
description = "Google Cloud Audit Protos"
version = "0.2.0"
release_status = "Development Status :: 4 - Beta"
dependencies = ["protobuf >= 3.6.0", "googleapis-common-protos >= 1.52.0"]

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.md")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()


setuptools.setup(
    name=name,
    version=version,
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    description=description,
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=dependencies,
    license="Apache-2.0",
    packages=find_packages(),
    package_data={"": ["*.proto"]},
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    namespace_packages=["google", "google.cloud"],
    url="https://github.com/googleapis/python-audit-log",
    include_package_data=True,
)
