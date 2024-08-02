"""

Copyright 2024 mr_fortuna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
from setuptools import find_packages, setup

setup(
    name='django-discord-oauth2',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License 2.0',
    description='Django application for secure user authorisation using Discord OAuth2',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mrf0rtuna4/django-discord-oauth2',
    author='mr_f0rtuna4',
    author_email='heypers.team@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Communications :: Chat',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=2.2',
        'requests',
    ],
    tests_require=[
        'django-setuptest>=0.2.1',
        'mock',
    ],
    entry_points={
        'console_scripts': [
            'django-discord-oauth2=discord_oauth2:main',
        ],
    },
)
