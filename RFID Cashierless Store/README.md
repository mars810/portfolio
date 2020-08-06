# RFID Cashierless Store 

## Overview

This was my senior year capstone project. This project aims to create a cashierless store where a user can register to the database by uploading their image and information to a database. The customer image encoding is done using Adrian Rosebrock's encoding package: https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/. When the customer stands in front of the camera, the shopping loop begins. The customer can then take items off a shelf and put them into a basket equipped with an RFID reader. Each grocery item has an RFID tag to be identified when in proximity of the RFID reader. The Raspberry Pi takes this RFID of the item and queries the database to get information about the item such as name and price. Once the customer has finished picking items, they can stand in front of the camera again. Once their face is recognized, the shopping loop ends and a receipt is sent to their phone with their purchased items and total. The shop.py file I wrote demonstrates the shopping loop process.


## Technologies

-Raspberry Pi
-Python
-Twilio
-mySQL
-OpenCV
-RFID Reader/Tags

