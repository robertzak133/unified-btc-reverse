// cutom-ribbon.h

extern void wbwl_custom_ribbon_sprintf(char *buffer, char * format, 
				       unsigned int current_media_index, 
				       unsigned int total_num_media);

extern int wbwlFileCTimeGet(unsigned int file_ptr, struct struct_DateTime *creation_date_time);

extern void ld_draw_video_scroll_bar(unsigned int percent_complete);

extern void ld_clear_video_scroll_bar(unsigned int right_x,
				      unsigned int bottom_y,
				      unsigned int width,
				      unsigned int height,
				      char color);
