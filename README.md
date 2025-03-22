# unified-btc-reverse

This repository contains tools, source file, hand patches, and documentation for the (nearly) complete flow for adding new features, written in C, to Browning Trail Cameras via semi-automatically generated firmware update files.  Supported cameras are BTC-7A, BTC{7,8}{E, E-HP4, E-HP5}.  That is, Browning Recon Force Advantage, and Recon Force  and Spec Ops line of cameras, models Edge, Elite HP4, and Elite HP5.

## Most Recent Releases
2025-03-02: 

A major release, including new functions, and generalization of  previous functions. 

I have also updated the firmare for the HP5 cameras so that they are based on the more recent factory firmware, version "M06170F." I'm not sure what's new in this factory release, although I don't believe it addresses the "corrupt SD card" bug.  My fix for this bug remains in place.

I added support for the BTC-7A (Recon Force Advantage) model.  This firmware is based on the more recent model for the BTC-7E, and thus inherits the "capture timer" feature Bronwning introduced with the "Elite" models.

I added Several new features, described in more detail below.  These include: 

* Saving and Restoring Custom Settings

* Native Photo Quality

* External Trigger

I have also removed the "Extended SD Card" menu.  This was a lightly used, and likely obsolete function, and I needed to retire it to make room for the custom configuration code, above.

As of 2025-03-18, there is a known issue that prevents certain newer HP5 cameras from downloading this firmware (or Browning firmware, for that matter).  If the "YES" option isn't available in the "FW UPGRADE" menu, you may have one of these cameras. 

See notes below for a description of how these new features might be used.  


## Feature Description
See also articles describing features at [New Optional Features for Browning HP5 Trail Cameras](https://winterberrywildlife.ouroneacrefarm.com/2022/12/19/new-optional-features-for-browning-hp5-trail-cameras/)
and 
[Adding Features to Browning Elite HP5 Firmware](https://winterberrywildlife.ouroneacrefarm.com/2022/11/14/adding-features-to-browning-elite-hp5-firmware/)

## Released Firmware Images
If you are here for RELEASE'd firmware images themselves, you can find them below:
| Camera Model | Factory Baseline  | Current WBWL | Version  | Build Date |
|--------------|-------------------|--------------|----------|------------|
| BTC-7A | [brnbtc70.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7a/factory-firmware-images/BTC7E_2021_10_07/brnbtc70.BRN) | [brnbtc70.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7a/created-burn-images/RELEASE/brnbtc70.BRN) | WWL7A_250321R | 2025-03-21 |
| BTC-7E | [brnbtc70.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e/factory-firmware-images/BTC7E_2021_10_07/brnbtc70.BRN) | [brnbtc70.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e/created-burn-images/RELEASE/brnbtc70.BRN) | WWL7E_250321R | 2025-03-21 |
| BTC-8E | [brnbtc80.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e/factory-firmware-images/BTC8E_2021_10_07/brnbtc80.BRN) | [brnbtc80.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e/created-burn-images/RELEASE/brnbtc80.BRN) | WWL8E_250321R | 2025-03-21 |
| BTC-7E-HP4 | [brnbtc71.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e-hp4/factory-firmware-images/2023-02-01-ns/brnbtc71.BRN) | [brnbtc71.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e-hp4/created-burn-images/RELEASE/brnbtc71.BRN) | WWL7EH4_250321R | 2025-03-21 |
| BTC-8E-HP4 | [brnbtc81.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e-hp4/factory-firmware-images/2023-02-01-ns/brnbtc81.BRN) | [brnbtc81.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e-hp4/created-burn-images/RELEASE/brnbtc81.BRN) | WWL8EH4_250321R | 2025-03-21 |
| BTC-7E-HP5 | [brnbtc72.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e-hp5/factory-firmware-images/BTC7EH5_M06170F/brnbtc72.BRN) | [brnbtc72.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e-hp5/created-burn-images/RELEASE/brnbtc72.BRN) | WWL7EH5_250321R | 2025-03-21 |
| BTC-8E-HP5 | [brnbtc82.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e-hp5/factory-firmware-images/BTC8EH5_M06170F/brnbtc82.BRN) | [brnbtc82.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e-hp5/created-burn-images/RELEASE/brnbtc82.BRN) | WWL8EH5_250321R | 2025-03-21 |

## Download Instructions
- Find the copy of brnbtc7x.BRN (Recon Force) or brnbtc8x.BRN (Spec Ops) file for your camera above
- Click "Download Raw".  Resulting file should be approximateley 4-6 MBytes in length.  
- Copy this file onto an SD card at the "top level" (not into a folder on SD card).  
- Note -- the file must be named "brnbtc7x.BRN" (for Recon Force) or "brnbtc8x.BRN" (for Spec Ops), where "x" is model dependent.  Sometimes downloading from your browser will add extra characters to distinguish it from previous downloads -- e.g. "brnbtc72(1).BRN".  If this happens, rename file to eliminate the extra character. In this case, to  "brnbtc72.BRN". 

## FW install Instructions

Before installing new firmware, make sure you have batteries that will easily power the camera for the several minutes it takes for firmware upgrade. Losing power during firmware upgrade is bad, requiring that the camera be reprogrammed by the manufacturer.  

On the Camera:
- Press "Mode" button 
- Select "CAMERA SETUP"
- Select "FW UPGRADE"
- Select "YES"

Display should show "UPGRADING".  Loading the firmware should take about 20 seoconds. DO NOT TURN OFF OR REMOVE BATTERIES DURING THIS TIME! (this will "brick" the camera).  

Camera will then "Reboot" with new firmware.

Note that updating firmware resets the camera configuration settings, including the date and time. 

## Reinstalling Factory Firmware
If, for any reason, you want to get back to the factory firmware, choose the "Factory Baseline" entry in the table above to get the baseline factory image, and install that.

Note that in order to restore the factory firmware to a BTC-7A camera, it is necessary to install the factory firmware twice, in succession, in order to work around incompatiblities between the firmware loader original to the BTC-7A, and that of the BTC-7E (which I used as the baseline for the custom BTC-7A firmware).  



## Feature Summary
 * Custom Ribbon: In "Playback" menu, the date and time of the photo/video are shown is larger font at the bottom of the playback screen, making it easier to tell when the image was taken when reviewing in the field. 
 * Night Video Limit: The default manufacturer firmware limits night time (flash illuminated) videos to 20 Seconds.  This option removes that limit, allowing illuminated videos of the same duration as daylight videos.
 * Custom Info Strip: Adds "seconds" to the time of day; adds battery percent; compresses the size of the Browning logo so it doesn't extend up into the main screen space. 
 * Custom Volume/Directory/Filenames: Normally, this camera renames the SD card "volume"  to "BROWNING", in folders in DCIM called xxxBTCF, in files called IMG_xxxx.  With this modification, these labels are all taken from the camera name, as set by the user.  Note that only the first 5 and 4 characters are used for the folder and file suffix/prefix respectively.  Thus, for camera name, "MYCAMERA", the SD card will be labeled "MYCAMERA" and files can be found in DCIM/100MYCAME/MYCA0001.JPG.  Any "space" in the first 5 characters is replaced by an "underscore".
 * External Trigger: In the "DSLR" and "FLASH" settings, causes the "aim led" to turned on to trigger an external camera or external flashes.  In the "DSLR" setting, the aim test LED is set whenever a photo or video is taken.  In the "FLASH" setting the "aim led" is only turned on during low light conditions.  This can be used to trigger external flashes, which are only used at night.
 * Time and Date Format Options: Added options for time format -- 12H/24H; and date formats MM/DD/YYYY; DD/MM/YYYY; YYYY/MM/DD; and YYYYMMDD
 * IR Flash Power: Added an "Off" option to IR Flash power.  When "Off", the internal IR Flash is not used, even for night photos.  Intended for use in sets with another source of IR or White Flash illumination. 
 * Night Threshold: Lowers the amount of light required to take a color image.  Defaults to "Standard".  In the "Always Color" setting, the camera will take color photos even in darkness.  Useful with external illumination, or when converting a camera to white flash.  
 * Timelapse+ Mode Enhancements:
 
   * More Frequent Timelapse Options: I added (every) "1" and "2" second options to the Timelapse Frequency Menu.  

   * All Day/Night Timelapse Period:  The factory firmware does it's best to limit timelapse photos to daytime only.  The factory "timelapse period" menu allows you to restrict daytime photos to 1,2,3, or 4 hours after sunrise and before sunset; or to take photos "all day".  For some applications, it is desirable to take 24 hour timelapse footage.  Thus, I have added an "all day/night" menu entry.  In this mode the camera will take a photo 24/7 at the specified interval.  In the "ALL DAY/NIGHT" mode, a new .TLS file is created every at midnight, per the local clock. This creates a separate .TLS file every 24 hours.   
   * PIR Triggers always stored as JPG: In the factory firmware, PIR triggered photos are stored with the Timelpase photos in the .TLS file if they occur during the day.  If at night, they are stored as individual JPG images.  With my new firmware, all PIR triggered photos are stored as JPG images, making it easier to separate timelapse vs. PIR triggered images. 
   * Timelapse Format: A new menu selects whether to store images taken in Timelapse+ mode as .TLS files (factory default), or as a series of .JPG files (new feature).  This feature designed to support data processing of Timelapse images as single JPGs (e.g. an AI-based tool flow which starts with JPG images).  

* Fix to SD Corruption Issue: fixes a bug in factory firmware in which SD cards are sometimes corrupted.  This fix allows higher speed (and higer capacity) SD cards to work reliably in Edge, HP4, and HP5 models. 

 * Loading/Storing Custom Configuration to SD card: This feature allows users to save a custom configuration to a file on the SD card.  Selecting the "SAVE CUSTOM" option in the "DEFAULT SETTINGs" menu will save a copy of the current camera settings to a file on the SD card.  If an SD card contains a valid configuruation file, the "CUSTOM" entry will be selectable, and will load the configuration in the file into the camera.   SD cards can be used in multiple cameras to bring them all to a user-specific configuration quickly, and without errors associated with updating the configuration by hand. Note that configurations are camera model-specific, and separate configuration files are required for each different camera model.  The (load)"FACTORY" option returns the camera to the factory configuration.  
 * Native Photo Quality: I added a "Native" selection to the "Photo Quality" menu.  This will cause photos to be taken at the native resolution of the Sony sensor, which is 1920 * 1080 pixels [2 MPixels].  This is the same resolution used by the factory firmware to take timelapse photos, and to take "rapid burst" photos.  This feature may be useful when collecting photos for an AI-based backend processing pipeline.  

## Features no longer supported

 * Extended SD Power: Causes the CPU and SD card to remain powered on for 30 seconds after each photo or video.  This to allow shared SD card to be read by another device.  Note that during this time, the camera will not trigger.

## Build environment and Source Code

This repository contains tools and source code for building firmware images.  

This is the third reorganziation of this effort, and it is aimed at preserving as much commonality between camera platforms as possible.  For example, by containing a single set of tools and source code for all targeted cameras.

Start at [Google Colab worksheet](https://github.com/robertzak133/unified-btc-reverse/blob/main/tools/colab/2023-01-30-Unified-BTC-BRN-FIle-Creator.ipynb) 

More detailed documentation to come in future blog posts, which will be referenced here. 



