<h1 align="center">Automated data collection system for convolutional neural networks</h1>
<h2 align="center">

## Description

**Example of how the package works**

![Снимок экрана (1)](https://user-images.githubusercontent.com/56004530/104139822-043e9000-53bf-11eb-867a-125cbee6dd3e.png)

## The package provides three sets of datasets for working with neural networks:

**We will have a data/train/ directory for the training dataset, data/test/ for the holdout test dataset and a data/validation/**

![1git](https://user-images.githubusercontent.com/56004530/104139462-bf195e80-53bc-11eb-8667-56d7592c8c4e.jpg)

**Images of red cars and blue cars would then be placed in the appropriate class directory.**

![2git](https://user-images.githubusercontent.com/56004530/104139536-32bb6b80-53bd-11eb-87ac-95a47d927487.jpg)

After completing the package, you get three folders for testing, training, and validation

data/ </p>
data/train/</p>
data/train/red/</p>
data/train/blue/</p>
data/test/</p>
data/test/red/</p>
data/test/blue/</p>
data/validation/</p>
data/validation/red/</p>
data/validation/blue/</p>

## How to use package

- **Install** with - ```pip install imagedataset_v1```
- **Import** package - ```import imagedataset.core```
- **Get download images** - ```find_and_separate("computer book horse", 100, "C:\\Users\\user\\Pictures", 40, 50) ```

## About the project

All program code works together with the Google driver, selenium and urllib libraries.The package is designed to download a set of images from Google and use them in the future for training neural networks .

**Technologies used:**
* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/about/)
* [Requests](https://requests.readthedocs.io/en/master/)
* [ChromeDriver](https://chromedriver.chromium.org/)
* [Shutil](https://github.com/enthought/Python-2.7.3/blob/master/Lib/shutil.py)

## Example of filling in attributes

- **```imagedataset_v1.core.find_and_separate("red car,blue car", 10, "C:\\Users\\Red_Fox\\Pictures")```** - main module
- **theme** Enter keywords to create a set of images Ex. ```find_and_separate("cat,dog",...) ```
- **quantity** This is the number of images per topic that you want to getEx. ```find_and_separate("cats,dogs", 200,...)```
- **path** This is the path to where you want to save the image sets Ex. ```find_and_separate("cats,dogs", 200, "C:\\Users\\user_name\\Pictures")```


