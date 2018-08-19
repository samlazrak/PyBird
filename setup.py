from setuptools import setup

setup(name='PyBird',
      version='0.1',
      description='Python Wrapper Library for eBird 2.0',
      url='http://github.com/samlazrak/PyBird',
      author='Sam Lazrak',
      author_email='samlazrak@outlook.com',
      license='MIT',
      packages=['PyBird'],
      install_requires=[
        'requests'
      ],
      zip_safe=False)
