from distutils.core import setup
setup(
    name='devops.lib.python-logstash',
    packages=['logstash'],
    version='2.0.0',
    description='SAJ DevOps Python logging handler for Logstash.',
    long_description=open('README.rst').read(),
    license='MIT',
    author='Jordan Mance',
    author_email='jordan.mance@snagajob.com',
    url='https://github.com/Snagajob/devops.lib.python-logstash',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
    ]
)
