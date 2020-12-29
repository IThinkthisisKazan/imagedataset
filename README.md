<h1 align="center">IMAGEDATASET</h1>
<h2 align="center">

## Description

**Example of how the package works**

![qxZVmKWq_2g](https://user-images.githubusercontent.com/56004530/101323835-55b4a600-387a-11eb-88c7-78e51804db35.jpg)

The package is designed to create a set of images.
Images are downloaded from the Chrome browser and saved in the folder you specify

![screenshot](https://user-images.githubusercontent.com/56004530/101624363-e8944280-3a2a-11eb-9d56-f352b0336ca9.jpg)

After completing the package, you get three folders for testing, training, and validation

## How to use package

- **Install** with - ```pip install imagedataset_v1```
- **Import** package - ```import imagedataset.core```
- **Get download images** - ```find_and_separate("computer book horse", 100, "C:\\Users\\user\\Pictures", 40, 50) ```

## Tools and enviroment
- **Windows 8, Windows 10**
- **Chroome browser version '''87.0.4280.88'''**

## About the project

All program code works together with the Google driver, selenium and urllib libraries.The package is designed to download a set of images from Google and use them in the future for training neural networks .

## Example of filling in attributes

- **```imagedataset_v1.core.find_and_separate("red car,blue car", 10, "C:\\Users\\Red_Fox\\Pictures")```** - main module
- **theme** these are the data sets you want to get Ex. ```find_and_separate("cat dog",...) ```
- **quantity** this is the number of images on a single topic that you want to get Ex. ```find_and_separate("cats dogs", 200,...)```
- **path** this is the path to the place where you want to save the image sets Ex. ```find_and_separate("cats dogs", 200, "C:\\Users\\user_name\\Pictures")```


