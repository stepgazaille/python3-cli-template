from setuptools import setup, find_packages

setup(name='program',
      version='0.1',
      description='Program description',
      author='Stephane Gazaille',
      author_email='author@domain.com',
      url='https://github.com/stepgazaille/program',
      packages=find_packages(exclude=['tests']),
      zip_safe=True,
      install_requires=[
        'requests>=2.11.1',
        ],
      scripts=['bin/program-cli'],
      )
