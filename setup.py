from setuptools import setup, find_packages

setup(

    # general meta
    name='pressed-python',
    version='0.0.1',
    author='dev@pressedjuicery.com',
    author_email='dev@pressedjuicery.com',
    description='dev@pressedjuicery.com',
    platforms='any',
    url='https://www.pressedjuicery.com',

    # packages
    packages=find_packages(),

    # dependencies
    install_requires = [
        'Flask==0.9',
        'Flask-Assets==0.8',
        'Jinja2==2.6',
        'pymysql==0.5',
        'SQLAlchemy==0.7.9',
        'WTForms==1.0.2',
        'Werkzeug==0.8.3',
        'paython==0.0.3',
        'alembic==0.4.1',
        'boto==2.8.0',
        'dogpile.cache==0.4.0',
        'fedex==1.0.14',
        'fpdf==1.7',
        'ipython==0.13.1',
        'python-memcached==1.48',
        'nose==1.2.1',
        'pyScss==1.1.5',
        'python-money==0.5',
        'jsmin==2.0.2-1',
        'cssmin==0.2.0',
        'suds==0.4',
        'yuicompressor==2.4.7',
        'urllib3==1.5',
        'reportlab==2.7',
        'async==0.6.1'
    ],
    # additional files to include
    include_package_data=True,

    # wut?
    classifiers=['Intended Audience :: Gods and Demons']
)
