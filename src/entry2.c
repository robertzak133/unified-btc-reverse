//
// 
// entry.c
//    2022-01-18 -- Zak created for BTC-7a
//    2022-08-31 -- Zak -- updated for BTC-7e-HP5; which no longer has any of the 
//                  command line functions
//    2023-01-08 -- Zak BTC 7/8E still have some jumbo CLI command
//    2023-02-08 -- Zak BTC 7/8E-HP5 needs several functiosn
//                  for now, let me put them in order of address by hand
//    2023-02-16 -- Zak changed to "build panorama" (which definitely is not used)
//
// The entry point into the BTC-7/8E that we're going to replace with a stub and use the 
//     remaining space in the binary to put new functions.
//     This file needs to be first in line for Linking 

#include "BTC.h"
#include "WBWL.h"
// 

#define ERROR_PRINT

#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
//      Gives us 20K bytes to work with -- plenty
void cmdFPGA_CdspPV(int argc, char ** argv) {
#ifdef ERROR_PRINT
  set_pre_printf_state();
  tty_printf("Error::WBWL - cmdFPGA_CdspPV() not implemented in this patched firmware version");
  check_post_printf_state_set_sio_params();
#endif
}
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
void cli_test_dispatch(int argc, char ** argv, unsigned int * param3) {
#ifdef ERROR_PRINT
  set_pre_printf_state();
  tty_printf("Error::WBWL - cli_test_dispatch() not implemented in this patched firmware version");
  check_post_printf_state_set_sio_params();
#endif
}

#endif


