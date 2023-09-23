//
// 
// entry0.c
//    2022-01-18 -- Zak created for BTC-7a
//    2022-08-31 -- Zak -- updated for BTC-7e-HP5; which no longer has any of the 
//                  command line functions
//    2023-01-08 -- Zak BTC 7/8E still have some jumbo CLI command
//    2023-02-08 -- Zak BTC 7/8E-HP5 needs several functiosn
//                  for now, let me put them in order of address by hand
//    2023-03-17 -- entry0 hijacks an unused function early in the code space
//                  to make patch space available for fucntions that need to be
//                  called early in camear boot (e.g. devInitPrimary). For all 
//                  camears
//
// The entry point into the BTC-7/8E that we're going to replace with a stub and use the 
//     remaining space in the binary to put new functions.
//     This file needs to be first in line for Linking 

#include "BTC.h"
#include "WBWL.h"
//#define ERROR_PRINT
// 

#if (defined BTC_7E) || (defined BTC_8E)
// This function is smaller, but it's earlier in the binary, necessary in the 7E/8E to avoid
//      executing out of uninitialized memory
uint MakeShortNameByLongName(char *param1, int *param2, char *dest_string, char *src_string) {
#ifdef ERROR_PRINT
  set_pre_printf_state();
  tty_printf("Error::WBWL - MakeShortNameByLongName() not implemented in this patched firmware version");
  check_post_printf_state_set_sio_params();
#endif

  btc_strcpy(dest_string, "WBWL");
  return 1; 
}    
#else

uint          get_VideoFormatStructure(int param_1, void* unknown_structure_pointer){

#ifdef ERROR_PRINT
  set_pre_printf_state();
  tty_printf("Error::WBWL - get_VideoFormatStructure() not implemented in this patched firmware version");
  check_post_printf_state_set_sio_params();
#endif
  return 0;
}

#endif




