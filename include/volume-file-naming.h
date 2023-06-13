//
// volume-file-nameing.h
//
// Functions to replace the naming of the volume and 
//     file prefixes

#define VFN_FILE_PREFIX_CHARS 4
#define VFN_DIR_SUFFIX_CHARS 5

// This is the function that normally labels a drive after 
//      it's been formatted/erased
//      we've hijacked it, discarded *volume_name (typically "BROWNING")
//      and replaced with the camera name

bool wbwl_fatVolLabSet(char *drive_letter, char *volume_name);

void wbwl_init_directory_suffix_file_prefix();

void wbwl_temp_file_path_sprintf(char *buffer, char *format_string, int dir_index, 
				 char *dir_suffix, char* file_prefx, int file_index);


void vfn_get_dir_suffix_file_prefix_from_camera_name(char * directory_suffix, 
						     char *file_prefix, 
						     char *camera_name);
