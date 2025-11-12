from setuptools import setup, find_packages

setup(
    name = 'amberNPS',
    packages = find_packages(where="amberNPS"),
    version = '0.1.0',
    license='MIT',
    description = 'A python api to make lethal blood concentrations using amberNPS',
    long_description="""amberNPS is a streamlit web application developed by Tascisio Nascimento Correa 
    https://github.com/nutof-pefoce/ambernps/blob/main/amberNPS.py. See publication at 
    https://www.sciencedirect.com/science/article/pii/S2667118224000151.
    """,
    author = 'Daniel Pasin',
    author_email = 'daniel.j.pasin@outlook.com',
    url = 'https://github.com/dpasin/amberNPS-api',
    keywords = ['amberNPS', 'chemistry', 'toxicology'],
    install_requires=['numpy', 'pandas', 'rdkit', 'mordredcommunity', 'scikit-learn==1.6.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)