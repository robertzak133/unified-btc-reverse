//
// volume-file-naming.c
//
// Functions to replace the naming of the volume and 
//     file prefixes

#include "BTC.h"
#include "volume-file-naming.h"
#include "timelapse.h"

//#define DEBUG


// Global Variables



// This is the function that normally labels a drive after 
//      it's been formatted/erased
//      we've hijacked it, discarded *volume_name (typically "BROWNING")
//      and replaced with the camera name

bool wbwl_fatVolLabSet(char *drive_letter, char *volume_name) {

  char camera_name[16];

#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("wbwl_fatVolLabSet -s \n");
  check_post_printf_state_set_sio_params();
#endif

  get_cold_item_camera_name(camera_name);
 
  // If camera_name is NULL, do the same thing as before
  if (camera_name[0] == (char) 0) {
    return fatVolLabSet(drive_letter, volume_name);
  }
  // else, substitute in camera name for volume name
  camera_name[10] = (char)0x00;

#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("wbwl_fatVolLabSet -e \n");
  check_post_printf_state_set_sio_params();
#endif


  return fatVolLabSet_wrapper(drive_letter, camera_name);
}



//
// this is the function that normally returns the "directory suffix" 
//     (usually BTCF_) and the "file prefix" (usally IMG_).
// We're going to replace these with the first characters from the 
//     cameraname
// 

void wbwl_init_directory_suffix_file_prefix() {
  char directory_suffix[16];
  char file_prefix[16];
  char camera_name[16];

  get_cold_item_camera_name(camera_name);

#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("wbwl_init_directory_suffix_file_prefix -s \n");
  check_post_printf_state_set_sio_params();
#endif

  vfn_get_dir_suffix_file_prefix_from_camera_name(directory_suffix, file_prefix, camera_name);


  // Now we do the indirection

  if (g_dcfapi_loaded_p != 1) {
    function_with_syscall_zero("dcfapi.c",173,0);
  }
  if (g_active_dcfapi_functions.set_dir_suffix_image_prefix != (void *)0x0) {
    (g_active_dcfapi_functions.set_dir_suffix_image_prefix)(directory_suffix, file_prefix, 0);
  }
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("wbwl_init_directory_suffix_file_prefix -e \n");
  check_post_printf_state_set_sio_params();
#endif

}

#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E)
void wbwl_alt_init_directory_suffix_file_prefix(char *suffix, char *prefix, uint param2) {
  char directory_suffix[16];
  char file_prefix[16];
  char camera_name[16];

  get_cold_item_camera_name(camera_name);

#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("wbwl_alt_init_directory_suffix_file_prefix -s \n");
  check_post_printf_state_set_sio_params();
#endif

  // I need a dummy call in here to get the symbol
  if (camera_name[0] == (char) 0) {
    init_directory_suffix_file_prefix(suffix, prefix, param2);
  } else {
    wbwl_init_directory_suffix_file_prefix();
  }
}
#endif


void vfn_get_dir_suffix_file_prefix_from_camera_name(char * directory_suffix, char *file_prefix, char *camera_name) {
  int i;

  // If camera_name is null, then do the regular thing
  if (camera_name[0] == (char)0) {
    btc_init_directory_suffix_file_prefix();
    btc_strcpy(directory_suffix, "_BTCF");
    btc_strcpy(file_prefix, "IMG_");
    return;
  }

  // Set directory_suffix to first 5 characters of camera name
  //     note that I believe software wants to keep total directory
  //     and filename length to 8 characters.  Substitute a "_" for
  //     any spaces (which are not accepted by downstream functions)

  for(i=0; i < VFN_DIR_SUFFIX_CHARS; i++) {
    if (camera_name[i] == ' ') {
      directory_suffix[i] = '_';
    } else {
      directory_suffix[i] = camera_name[i];
    }
    if (camera_name[i] == (char)0)
      break;
  }
  directory_suffix[i] = (char)0;

  // Set File Prefix to first 4 characters of camera name
  for(i=0; i < VFN_FILE_PREFIX_CHARS; i++) {
    if (camera_name[i] == ' ') {
      file_prefix[i] = '_';
    } else {
      file_prefix[i] = camera_name[i];
    }
    if (camera_name[i] == (char)0)
      break;
  }
  file_prefix[i] = (char)0;
}

// wbwl_temp_file_path_sprintf
// in TaskTimeLapseFSM_task8
// replaces:
//   local_sprintf(acStack52,s_H:\DCIM\%03d%s\%s%04d.jpg_8036f398,local_36,s__BTCF_8036d4c4,
//                 s_IMG__8036d4cc,local_38);
//     
// with the new directory names based on camera name

void wbwl_temp_file_path_sprintf(char *buffer, char *format_string, int dir_index, 
				 char *dir_suffix, char* file_prefx, int file_index){

  char l_directory_suffix[16];
  char l_file_prefix[16];
  char camera_name[16];

  get_cold_item_camera_name(camera_name);

  vfn_get_dir_suffix_file_prefix_from_camera_name(l_directory_suffix, l_file_prefix, camera_name);

  local_sprintf(buffer,format_string,dir_index, l_directory_suffix, 
		l_file_prefix, file_index);
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("wbwl_temp_file_path_sprintf -- output file is %s\n",
	     buffer);
  check_post_printf_state_set_sio_params();  
#endif
}
