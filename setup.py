import setuptools

setuptools.setup(
    name="fractal-style-schema",
    version="0.0.1",
    author="Carlo Minotti",
    author_email="carlo.minotti@revolut.com",
    description="Fractal style code folder structure for large schemas, gql based",
    long_description="",
    include_package_data=True,
    url="https://github.com/minottic/fractal-style-schema",
    packages=setuptools.find_packages(),
    install_requires=['Django==1.8.14',
                      'graphene==2.0',
                      'graphene-django==2.0',
                      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
