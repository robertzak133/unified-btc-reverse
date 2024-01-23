# unified-btc-reverse

This repository contains tools, source file, hand patches, and documentation for the (nearly) complete flow for adding new features, written in C, to Browning Trail Cameras via semi-automatically generated firmware update files.  Supported cameras are BTC{7,8}E{, HP4, HP5}.  That is, Browning Recon Force and Spec Ops line of cameras, models Edge, Elite HP4, and Elite HP5. 

## Feature Description
See also articles describing features at [New Optional Features for Browning HP5 Trail Cameras](https://winterberrywildlife.ouroneacrefarm.com/2022/12/19/new-optional-features-for-browning-hp5-trail-cameras/)
and 
[Adding Features to Browning Elite HP5 Firmware](https://winterberrywildlife.ouroneacrefarm.com/2022/11/14/adding-features-to-browning-elite-hp5-firmware/)

## Released Firmware Images
If you are here for RELEASE'd firmware images themselves, you can find them below:
| Camera Model | Factory Baseline  | Current WBWL | Version  | Build Date |
|--------------|-------------------|--------------|----------|------------|
| BTC-7E | [brnbtc70.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e/factory-firmware-images/BTC7E_2021_10_07/brnbtc70.BRN) | [brnbtc70.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e/created-burn-images/RELEASE/brnbtc70.BRN) | WWL7E_231114P | 2023-11-15 |
| BTC-8E | [brnbtc80.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e/factory-firmware-images/BTC8E_2021_10_07/brnbtc80.BRN) | [brnbtc80.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e/created-burn-images/RELEASE/brnbtc80.BRN) | WWL8E_231114P | 2023-11-15 |
| BTC-7E-HP4 | [brnbtc71.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e-hp4/factory-firmware-images/2023-02-01-ns/brnbtc71.BRN) | [brnbtc71.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e-hp4/created-burn-images/RELEASE/brnbtc71.BRN) | WWL7EH4_231114P | 2023-11-15 |
| BTC-8E-HP4 | [brnbtc81.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e-hp4/factory-firmware-images/2023-02-01-ns/brnbtc81.BRN) | [brnbtc81.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e-hp4/created-burn-images/RELEASE/brnbtc81.BRN) | WWL8EH4_231114P | 2023-11-15 |
| BTC-7E-HP5 | [brnbtc72.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e-hp5/factory-firmware-images/BTC7EH5_L10200F/brnbtc72.BRN) | [brnbtc72.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-7e-hp5/created-burn-images/RELEASE/brnbtc72.BRN) | WWL7EH5_231114P | 2023-11-15 |
| BTC-8E-HP5 | [brnbtc82.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e-hp5/factory-firmware-images/BTC8EH5_L10200F/brnbtc82.BRN) | [brnbtc82.BRN](https://github.com/robertzak133/unified-btc-reverse/blob/main/targets/btc-8e-hp5/created-burn-images/RELEASE/brnbtc82.BRN) | WWL8EH5_231114P | 2023-11-15 |

## Download Instructions
- Find the copy of brnbtc7x.BRN (Recon Force) or brnbtc8x.BRN (Spec Ops) file for your camera above
- Click "Download"
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
If, for any reason, you want to get back to the factory firmware, choose the "Factory Baseline" entry in the table above to get the baseline factory image, and install that



## Feature Summary
 * Custom Ribbon: In "Playback" menu, the date and time of the photo/video are shown is larger font at the bottom of the playback screen, making it easier to tell when the image was taken when reviewing in the field. 
 * Night Video Limit: The default manufacturer firmware limits night time (flash illuminated) videos to 20 Seconds.  This option removes that limit, allowing illuminated videos of the same duration as daylight videos.
 * Custom Info Strip: Adds "seconds" to the time of day; adds battery percent; compresses the size of the browning logo so it doesn't extend up into the main screen space.  Note there is a bug for this firmware in some Edge (BTC-8E) cameras which breaks the temperature and pressure reading including in the info strip.  
 * Custom Volume/Directory/Filenames: Normally, this camera renames the SD card "volume"  to "BROWNING", in folders in DCIM called xxxBTCF, in files called IMG_xxxx.  With this modification, these labels are all taken from the camera name, as set by the user.  Note that only the first 5 and 4 characters are used for the folder and file suffix/prefix respectively.  Thus, for camera name, "MYCAMERA", the SD card will be labeled "MYCAMERA" and files can be found in DCIM/100MYCAME/MYCA0001.JPG.  Any "space" in the first 5 characters is replaced by an "underscore".
 * DSLR Trigger: Causes the "aim led" to turn on whenever a photo or video is taken.  This LED can be used to trigger a DSLR camera, while also allowing the trail camera to take photos or video.
 * Extended SD Power: Causes the CPU and SD card to remain powered on for 30 seconds after each photo or video.  This to allow shared SD card to be read by another device.  Note that during this time, the camera will not trigger.
 * Time and Date Format Options: Added options for time format -- 12H/24H; and date formats MM/DD/YYYY; DD/MM/YYYY; YYYYMMDD
 * IR Flash Power: Added an "Off" option to IR Flash power.  When in "Off", the IR Flash is not used, even for night photos.  Intended for use in sets with another source of IR illumination. 
 * Night Threshold: Lowers the amount of light required to take a color image.  Defaults to "Standard".  In "No light" setting, the camera will take color photos even in darkness.  Useful with external illumination. 
 * Fix to SD Corruption Issue: fixes a bug in factory firmware in which SD cards are sometimes corrupted.  This fix allows higher speed (and higer capacity) SD cards to work reliably in Edge, HP4, and HP5 models. 
 
## Build environment and Source Code

This repository contains tools and source code for building firmware images.  

It is the third reorganziation of this effort, and it is aimed at preserving as much commonality between camera platforms as possible.  For example, by containing a single set of tools and source code for all targeted cameras.

Start at [Google Colab worksheet](https://github.com/robertzak133/unified-btc-reverse/blob/main/tools/colab/2023-01-30-Unified-BTC-BRN-FIle-Creator.ipynb) 

More detailed documentation to come in future blog posts, which will be referenced here. 



