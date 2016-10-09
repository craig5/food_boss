#!/usr/bin/env python3
"""
Setup for food_boss (python3).
"""
from __future__ import print_function
# core python libraries
import distutils
import distutils.cmd
import distutils.core
import os
import setuptools
# third party libraries
import versioneer
# custom libraries


# Basic info.
_PACKAGE_NAME = 'food_boss'
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_LIB_DIR = 'lib'
setup_args = {}
setup_args['name'] = _PACKAGE_NAME
setup_args['packages'] = setuptools.find_packages(exclude=['tests'])
setup_args['version'] = versioneer.get_version()
setup_args['test_suite'] = 'nose.collector'
setup_args['setup_requires'] = ['nose>=1.0']
setup_args['author'] = 'Craig Sebenik'
setup_args['author_email'] = 'craig5@users.noreply.github.com'
setup_args['description'] = 'Food Boss - recipe manager'
setup_args['url'] = 'http://www.friedserver.com/'
setup_args['keywords'] = ['food', 'recipes']
setup_args['license'] = 'Apache License 2.0'


class InfoCommand(distutils.cmd.Command):
    """Get info about this project."""
    description = 'Get info about this project (e.g. setup args).'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Info about this project."""
        print('Setup args:')
        data = []
        data.append({'title': 'Version', 'value': setup_args['version']})
        for cur in data:
            print('  {title}: {value}'.format(**cur))


setup_args['cmdclass'] = versioneer.get_cmdclass()
setup_args['cmdclass']['info'] = InfoCommand
setup_args['package_dir'] = {'': _LIB_DIR}
setup_args['entry_points'] = {
    'console_scripts': [
        'food_boss = food_boss.scripts:cli'
    ]
}


if __name__ == '__main__':
    # Stupid distutils doesn't support 'entry_points'.
    setuptools.setup(**setup_args)
# End of file.
