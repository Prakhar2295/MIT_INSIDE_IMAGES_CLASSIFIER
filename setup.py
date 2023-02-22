from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Prakhar2295",
    description="A small package for dvc dl pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Prakhar2295/DVC_TENSORFLOW_1",
    author_email="prakhar.kumar5@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
       "boto3==1.18.58",
       "botocore==1.21.58",
       "dvc",
       "matplotlib==3.4.3",
       "pandas==1.3.3",
       "PyYAML==5.4.1",
       "tensorflow==2.5",
       "tqdm==4.62.3",
       "joblib==1.1.0",
       "scipy==1.7.1",
       "scikit-learn==1.0",
       "Flask==1.1.1",
       "gevent==1.4.0",
       "h5py==3.1.0",
       "numpy==1.19.5",
       "Pillow==8.3.2",
       "Werkzeug==2.0.1",
       "itsdangerous==1.1.0",
       "Jinja2==2.11.1"

    ]
)