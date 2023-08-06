![head](https://media.licdn.com/dms/image/C5112AQFmcRLriAsYmg/article-cover_image-shrink_720_1280/0/1565072249072?e=2147483647&v=beta&t=R-WU4XXIhw-wlAOMQIc27OcIU-NNoxqy4o7MMJfSkT8)
# Fire Detection using Webcam

The aim of this project is to notify and protect people from accidents related to fire. Fire is very dangerous and can cause great loss of life and property. Thousands of fire accidents happen worldwide each year due to power failure, accidental fires, and natural lightning. To control fire, various systems are developed and being developed.

We propose the design and initial implementation of a fire & human detection system using image processing and Machine Learning. Fire detection systems could improve the security of organizations and public places. The proposed system aims to create a reliable, safe, and smart system to reduce limitations and faults like false alarms, which cause panic among people and even the loss of money. The use of new technology can make places safe from hazardous fires.

Lately, fire outbreaks are a common issue happening anywhere, and the damage caused by these types of incidents is tremendous towards nature and human interest. Due to this, the need for applications for fire & human detection has increased in recent years. In this system, we proposed a fire detection algorithm based on image processing techniques that are compatible with surveillance devices like CCTV, wireless cameras, and UAVs. The algorithm uses the RGB color model to detect the color of the fire, mainly comprehended by the intensity of the component R, which is the red color. The growth of fire is detected using Sobel edge detection. Finally, a color-based segmentation technique was applied based on the results from the first and second techniques to identify the region of interest (ROI) of the fire. After analyzing 50 different fire scenarios images, the final accuracy obtained from testing the algorithm was 93.61%, and the efficiency was 80.64%.

## Introduction

Fire, especially fire in buildings, can spread quickly and cause great loss of life and property. Therefore, early fire detection and warning is imperative. Fire detectors, smoke detectors, and temperature detectors have been widely used to protect property and give warning of fires. However, smoke and temperature detection is slower than light detection, which is the substantive detection method proposed in this project. Furthermore, to cover the entire area potentially subject to fire, many smoke or temperature fire detectors are required. In order to facilitate earlier detection of fire and to monitor the spread of the fire, we propose a fire detection system based on light detection, as distinct from smoke or heat detection.

This system acquires video input from any video camera, such as a web camera. The system will trigger an audible alarm and provide visual images of the fire as a red box superimposed over the image of the fire flame in the video sequences. Our proposed method is a real-time processing method and uses simple algorithms based on color conditions and fire growth checking.

### 1.1 Motivation

- In the 21st century, we use a lot of electronic gadgets in our life on a daily basis because the global warming temperature of the earth is increasing day-by-day, and sometimes gadgets get heated or become the reason for fires, which are the greatest evils.
- They are a key motivation factor in the development of systems for early prevention and detection of urban area fire.

### 1.2 Need for the new system

- To detect early fires.
- To notify people if a fire exists.
- To detect how many people are stuck in fire accidents.

### 1.3 Objectives

- To detect the occurrence of humans and fire.
- To alert the control panel and proper authorities.
- To notify the occupants to take action.

### 1.4 Application

- Smart Home
- Home Automation System
- Detect Fire and Control that Situation in Public Places like Hospitals, Colleges, Schools, etc.

## Hardware Requirements

- Windows PC with 4GB RAM and 128GB HDD/SSD
- CCTV Camera
- Alert System

## Software

- Python 3.6
- Pycharm IDE
- Packages:
  - Flask
  - Opencv
  - Tensorflow & Keras
