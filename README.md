# Secure-Data-Transmission-using-Steganography-in-IOT
A secure system was developed to transfer secret data from one point to another by making use of the technique called Image Steganography based on the live images captured from an IOT environment. The IOT environment consisted of a PIR motion detection sensor which was connected with an ESP32-Cam to capture images. 

This project consists of both hardware and software parts. The steps followed are :-

# Hardware Part
1. Create a new bot in telegram.
2. In arduinoCode.ino file, replace the ssid and password with your wifi name and wifi password.
3. In arduinoCode.ino file, replace the token and chat_id values which were generated at the time of creating a bot.
4. Program the ESP32 board with FTDI 232 USB to Serial Interface Board. The circuit diagram for this is available in the ProjectReport.pdf file of this repository.
5. To start capturing the live images, build a circuit with the programmed ESP32 cam, PIR motion detector sensor, LED, resistors, NPN transistor and jumper cables. The circuit diagram for this is available in the ProjectReport.pdf file of this repository.
6. Upon providing the power supply and if any motion is detected, ESP32 cam starts capturing the images and these images get stored in the bot which was created for this project.

# Software Part
1. Save the images stored in the telegram's bot to your local device to perform image steganography.
2. The code to perform image steganography is in imageSteganography.py file of this repository.
3. The software part involves
   -> embedding the captured image behind a cover image. The resulting image is called hidden image. (Sender Side)
   -> encoding the secret message inside the hidden image. The resulting image is called stego image  (Sender Side)
   -> decoding the stego image by entring the secret password (Receiver Side)
4. The screenshots of this part can be found in ProjectReport.pdf file of this repository. 
