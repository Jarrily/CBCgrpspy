from setuptools import setup, find_packages

setup(
    name='CBCgrpspy',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'numpy==1.26.4',
        'pandas',
        'scipy',
        'openpyxl'
    ],
    description='Statistical Group Comparison Tool',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Jarrily',
    author='Jinhui Liu',
    author_email='ljh18620847741@gmail.com',
    classifiers=[
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows :: Windows 11'
    ],
    python_requires='~=3.10',
)
