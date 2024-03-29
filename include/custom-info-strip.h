// custom-ribbon.h
//     Headers Routines which print the creation date and time of the current image/video
//     on the playback screen so that a person can read them without a magnifying glass


int wbwl_custom_info_strip_date_sprintf(char *buffer, char *format_string, int month, int day, int year);

int wbwl_custom_info_strip_time_sprintf(char *buffer, char * format, int hour, int minute, char* am_pm_string); 

int wbwl_custom_info_strip_strlen(char *buffer);

//int wbwl_StampLoadFont(unsigned int font_id,
//			unsigned short *large_width, unsigned short *large_height,
//			unsigned short *small_width, unsigned short *small_height,
//			unsigned int font_scale);

void wbwl_StampDrawLogo(struct_video_page_descriptor *video_page_descriptor, unsigned int font_scale);
