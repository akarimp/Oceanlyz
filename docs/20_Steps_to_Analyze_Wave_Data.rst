Steps to Analyze Wave Data Measurements
=======================================
Correct Measured Data by Pressure Sensors for Atmospheric Pressure

Wave data commonly measured in either these two method:
# Measure water surface elevation (such as using wave staff gauge)
# Measure water pressure using pressure sensor

To calculate wave properties from measured data, these steps need to be followed.

Steps to Calculate Wave Properties from Water Level Measurements
----------------------------------------------------------------

Here are general steps to calculate wave characteristics from water level data:

1. Clean measured time-series data for outliers, missing values, etc.
2. Remove a trend from the measurements (detrend data) burst by burst.
3. Use zero-crossing or spectral methods to calculate wave characteristics from the water level time-series, burst by burst.

| If you use Oceanlyz, it will handle steps 3 to 7 for you.
| You can use `ScientiMate <https://github.com/akarimp/ScientiMate>`_ to clean the data.

Steps to Calculate Wave Properties from Water Pressure Measurements
-------------------------------------------------------------------

Here are general steps to calculate wave characteristics from pressure data:

1. Clean measured time-series data for outliers, missing values, etc.
2. Remove atmospheric pressure from data.

    To collect pressure data, recording should begin while the pressure sensor is still on land (perhaps a couple of hours before deployment), and then it will be deployed in the water. This will capture the initial offset (which includes atmospheric pressure).

    To remove atmospheric pressure, two scenarios might occur:

    * If atmospheric pressure is relatively constant during deployment (such as during short deployment with no weather change), subtract the initial sensor reading taken on the land from all pressure measurements.
    * If atmospheric pressure varies during deployment (such during a passage of weather front, tropical storm, etc.), first subtract the initial sensor reading taken on land from all pressure measurements and then correct underwater pressure readings for changes in atmospheric pressure with respect to atmospheric pressure when the sensor was initially on the land.

3. Convert pressure data to water height.
4. Remove a trend from the measurements (detrend data) burst by burst.
5. Separate the resulting water height, burst by burst, into water depth time-series (due to hydrostatic pressure) and water surface elevation time-series (due to dynamic pressure).
6. Correct the water surface elevation time-series to account for pressure attenuation in water depth, burst by burst.
7. Use zero-crossing or spectral methods to calculate wave characteristics from the water level time-series, burst by burst.

| If you use Oceanlyz, it will handle steps 3 to 7 for you.
| You can use `ScientiMate <https://github.com/akarimp/ScientiMate>`_ to clean the data.
