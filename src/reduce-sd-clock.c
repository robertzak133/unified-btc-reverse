//
// reduce-sd-clock.c
//  
// intercept the call to initialize the default SD card
//    if the speed mode is 100 MHz
//       reduce the speed to 50 MHz 
//     

//   2024-05-30 Zak: refined my approach to cover several more cases
//       relying on 4-single-value patches
//       Nulling out this file.  Leaving it here in case I need to come back
//


#include "BTC.h"


