from setuptools import setup, find_packages

setup(
    name='apy',
    version='0.6.0',
    license='MIT',
    author='Andrew McCloud',
    author_email='andrew@amccloud.com',
    url='http://github.com/amccloud/apy/',
    packages=find_packages(exclude=['tests']),
    install_requires=open('requirements.txt').readlines(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
