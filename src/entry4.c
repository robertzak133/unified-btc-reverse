//
// 
// entry4.c
//
// The entry point into the BTC-7/8E-HP5 that we're going to replace with a stub and use the 
//     To make room for more code

#include "BTC.h"
#include "WBWL.h"

#define ERROR_PRINT
// 

#if (defined BTC_7E_HP5) || (defined BTC_8E_HP5)

// void used_jfif_function(void) {
// void hijacked_digital_zoom_function(void) {
int snapYuv2ExifJpgWrite (void *image_descriptor,uint jpg_width,uint jpg_height,
			  char *filename,uint param_5,uint param_6) {
#ifdef ERROR_PRINT
  set_pre_printf_state();
  // tty_printf("Error::WBWL - used_jfif_function() not implemented in this patched firmware version");
  // tty_printf("Error::WBWL - hijacked_digital_zoom_function() not implemented in this patched firmware version");
  tty_printf("Error::WBWL - snapYuvExifJpgWrite() not implemented in this patched firmware version");
  check_post_printf_state_set_sio_params();
#endif
}

#endif

