//
// dslr.c
// 
// Activ versions of functions which would (in a DSLR trigger configuration)
//       turn the aim LED on and off
//       Link in this file if you don't want DSLR

#include "dslr.h"
#include "BTC.h"

void dslr_LEDOn() {
  Write_LEDOn();
}

void dslr_LEDOff() {
  Write_LEDOff();
}
