from setuptools import setup

setup(
    name='uhome',
    version='0.1.0',
    packages=['venv.Lib.distutils', 'venv.Lib.encodings', 'venv.Lib.site-packages.pip',
              'venv.Lib.site-packages.pip._vendor', 'venv.Lib.site-packages.pip._vendor.idna',
              'venv.Lib.site-packages.pip._vendor.pep517', 'venv.Lib.site-packages.pip._vendor.pytoml',
              'venv.Lib.site-packages.pip._vendor.certifi', 'venv.Lib.site-packages.pip._vendor.chardet',
              'venv.Lib.site-packages.pip._vendor.chardet.cli', 'venv.Lib.site-packages.pip._vendor.distlib',
              'venv.Lib.site-packages.pip._vendor.distlib._backport', 'venv.Lib.site-packages.pip._vendor.msgpack',
              'venv.Lib.site-packages.pip._vendor.urllib3', 'venv.Lib.site-packages.pip._vendor.urllib3.util',
              'venv.Lib.site-packages.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip._vendor.colorama', 'venv.Lib.site-packages.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treebuilders', 'venv.Lib.site-packages.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip._vendor.progress', 'venv.Lib.site-packages.pip._vendor.requests',
              'venv.Lib.site-packages.pip._vendor.packaging', 'venv.Lib.site-packages.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip._vendor.webencodings', 'venv.Lib.site-packages.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip._internal', 'venv.Lib.site-packages.pip._internal.cli',
              'venv.Lib.site-packages.pip._internal.req', 'venv.Lib.site-packages.pip._internal.vcs',
              'venv.Lib.site-packages.pip._internal.utils', 'venv.Lib.site-packages.pip._internal.models',
              'venv.Lib.site-packages.pip._internal.commands', 'venv.Lib.site-packages.pip._internal.operations',
              'venv.Lib.site-packages.wheel', 'venv.Lib.site-packages.wheel.cli', 'venv.Lib.site-packages.setuptools',
              'venv.Lib.site-packages.setuptools.extern', 'venv.Lib.site-packages.setuptools._vendor',
              'venv.Lib.site-packages.setuptools._vendor.packaging', 'venv.Lib.site-packages.setuptools.command',
              'venv.Lib.site-packages.pkg_resources', 'venv.Lib.site-packages.pkg_resources.extern',
              'venv.Lib.site-packages.pkg_resources._vendor', 'venv.Lib.site-packages.pkg_resources._vendor.packaging',
              'uhome'],
    url='https://github.com/almirdelkic/uhome',
    license='GNU GPLv3',
    author='Almir Delkic',
    author_email='',
    description='Wrapper for communication with Uponor Smatrix Wave PLUS Smart Home Gateway R-167 aka U@home.'
)