# Raspberry Pi Plant Monitor

## Description

For CSCI 43300, each group was tasked with creating a project that would be used as the final assessment of what was learned throughout the CSCI 43300 course. For their project Caleb Kirby and Jason Hampshire created a plant monitoring system. This system is created by attaching a variety of sensors to a plant pot and a raspberry pi device. The Internet of Things device takes readings of the various sensors and uses this information to inform a user of the status of the connected plant.

The container for this project ended up being a 3D printed model that was attached to the pot with epoxy. Chemical epoxy was used instead of regular glue to be sure there was a good seal between the electronics and the potentially wet soil. The 3D print was modeled and exported to another student who then printed the model.

The project was met with positive reception. The final presentation of the development of the plant monitoring project can be found [here](/plantMonitorPresentation.pdf).

For more details on the implementation and project results, plase see the [project writeup](/plantMonitorFinalWriteup.pdf).

## Hardware Used

- [HW-080 Soil Hygrometer](https://components101.com/modules/soil-moisture-sensor-module)
- [CCS811 Gas Sensor](https://components101.com/sensors/ccs811-air-quality-gas-sensor-module)
- [DHT11 Temp/Humid Sensor](https://components101.com/sensors/dht11-temperature-sensor)
- [Photoresistor](https://components101.com/resistors/ldr-datasheet)
- [Raspberry Pi 4](https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf)
- Plant Pot
- 3D Printed Compartment
    
## Software

The python code was written on the raspberry pi in a [Rasbian](https://www.raspberrypi.com/software/) installation

## Installation

To install rasbian, follow the offical Raspberry Pi guide found on the [Rasbian](https://www.raspberrypi.com/software/) installation page or follow the video tutorial found [here](https://youtu.be/ntaXWS8Lk34).

## Imagery

### 3d Print ###

STL File:  
![stlFile](/3dPrint/potback.png)  

Final Print:  
![finalPrint](/3dPrint/finalPrint.jpg)  

Assembled 3D Print with Pot:  
![assembled](/3dPrint/assembled.jpg)

### Project Schematic ###

![schematic](/projectImages/schematic.png)

### Board Layout ###

![boardLayout](/projectImages/board.png)

### Functional Demo ###



## Roadmap

This project will be continued by Caleb Kirby in a seperate, private repository.

## Authors & Acknowledgments

The project was done jointly between Jason Hampshire and Caleb Kirby

## Project Status

This repository is **Discontinued** and will not see any further work. Work will be continued by Caleb Kirby privatley.