from setuptools import setup

setup(name='cryptotik',
      version='0.32.1',
      description='Standardized common API for several cryptocurrency exchanges.',
      url='https://github.com/peerchemist/cryptotik',
      author='Peerchemist',
      author_email='peerchemist@protonmail.ch',
      license='BSD',
      packages=['cryptotik'],
      install_requires=['requests', 'six', 'dateutil'],
      tests_require=['pytest'],
      zip_safe=False)
