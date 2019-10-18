
from setuptools import setup, find_packages

setup(
    # general meta
    name='test-dotcom',
    version='0.0.1',
    author='David Dilley',
    author_email='dilley.david@gmail.com',
    description='dilley.david@gmail.com',
    platforms='any',
    url='127.0.0.1:5000',

    # packages
    packages=find_packages(),

    # dependencies
    install_requires = [
        'Flask==1.0',
        'Flask-Assets==0.8',
        'Flask-Login==0.2.11',
        'Flask-PyMongo==0.3.1',
        'Jinja2==2.6',
        'Werkzeug==0.8.3',
        'healthcheck==1.0.0',
        'jsmin==2.0.2-1',
        'cssmin==0.2.0',
        'urllib3==1.5'
    ],
    # additional files to include
    include_package_data=True,

    classifiers=['Intended Audience :: Technicolor']
)
