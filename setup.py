from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='wss_extract',
      version='0.1.0',
      description='Gets sentiment from online tools',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Andrew Moore',
      author_email='andrew.p.moore94@gmail.com',
      license='MIT',
      install_requires=[
          'Werkzeug==0.11.11',
          'reppy>=0.4.14',
          'robobrowser==0.5.3',
          'notebook>=6.4.10',
          'pytest==3.6.1'
      ],
      python_requires='>=3.6',
      packages=find_packages())
