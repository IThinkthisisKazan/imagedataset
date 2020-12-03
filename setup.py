import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chrome-dataset",
    version="0.0.2",
    author="Ayar Tokoev",
    author_email="ayartokoev3@gmail.com",
    description="Package for download image from chrome",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IThinkthisisKazan/Python/tree/main/project_kurs/version_3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

from distutils.core import setup
setup(
  name = 'imagedataset',         # How you named your package folder (MyLib)
  packages = ['imagedataset'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Package for download image from chrome',   # Give a short description about your library
  author = 'Ayar Tokoev',                   # Type in your name
  author_email = 'ayartokoev3@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/IThinkthisisKazan/imagedataset',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'urllib',
          'selenium',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
  ],
)