from setuptools import setup, find_packages

with open('README.rst') as f:
    README = f.read()


classifiers = ["Programming Language :: Python",
               "License :: OSI Approved :: Apache Software License",
               "Development Status :: 1 - Planning"]


setup(name='django-bypass-auth',
      version='0.1',
      packages=find_packages(),
      description='Backend and Middleware for bypassing django authentication completely',
      long_description=README,
      author="Ivan Vigasin",
      author_email="ivigasin@gmail.com",
      include_package_data=True,
      zip_safe=False,
      classifiers=classifiers)
