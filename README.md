<h1 align="center">IMAGEDATASET</h1>
<h2 align="center">

## Description

**Example of how the package works and how attributes are filled in**

![qxZVmKWq_2g](https://user-images.githubusercontent.com/56004530/101323835-55b4a600-387a-11eb-88c7-78e51804db35.jpg)

This code is for creating datasets.
Which he will receive by request in the Chroome browser and then save them in the specified folder

![screenshot](https://user-images.githubusercontent.com/56004530/101624363-e8944280-3a2a-11eb-9d56-f352b0336ca9.jpg)

At the end of the module, you get folders that contain images on the subject of the request. And a separate folder that contains a common set of images and two folders are folders that contain the percentage of images

## How to use package

- **Install** with - ```pip install imagedataset_v1```
- **Import** package - ```import imagedataset.core```
- **Get download images** - ```find_and_separate("computer book horse", 100, "C:\\Users\\user\\Pictures", 40, 50) ```

## Tools and enviroment
- **Windows 8, Windows 10**
- **Chroome browser version '''87.0.4280.88'''**

## About the project

The entire program code works together with the Google driver and the selenium and urllib libraries.The package is intended for downloading a set of images from Google and using them in the future to train neural networks to recognize objects.

## Example of filling in attributes

- **```find_and_separate(theme, quantity, path, separate one, separate two)```** - main module
- **theme** these are the data sets you want to get Ex. ```find_and_separate("cat dog",...) ```
- **quantity** this is the number of images on a single topic that you want to get Ex. ```find_and_separate("cats dogs", 200,...)```
- **path** this is the path to the place where you want to save the image sets Ex. ```find_and_separate("cats dogs", 200, "C:\\Users\\user_name\\Pictures")```
- **separate one** and **separate two** this is the ratio by which you want to divide the total set of images.
The amount must not exceed or be less than 100 Ex.```find_and_separate("cats dogs", 200, "C:\\Users\\user_name\\Pictures", 40, 60)```
