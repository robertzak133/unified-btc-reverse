// cutom-ribbon.h

extern void cr_expand_date_time(uint compressed_date_time, struct_DateTime *expanded_date_time);

extern void wbwl_custom_ribbon_sprintf(char *buffer, char * format, 
				       unsigned int current_media_index, 
				       unsigned int total_num_media);

extern int wbwlFileCTimeGet(char *filename, struct struct_DateTime *creation_date_time);

extern void ld_draw_video_scroll_bar(unsigned int percent_complete);

extern void ld_clear_video_scroll_bar(unsigned int right_x,
				      unsigned int bottom_y,
				      unsigned int width,
				      unsigned int height,
				      char color);

void cr_unpack_pressure_temperature_coefficients(struct_pressure_temperature_coefficients *unpacked_coefficients, 
						 struct_i2c_pressure_temperature_coefficients *packed_coefficients);

void cr_read_check_compensation_coefficients(int store_flag);
void cr_sign_extend(int *n_bit_twos_complement, int num_bits);

void cr_sign_extend_coefficients(struct_pressure_temperature_coefficients *unpacked_coefficients);
void cr_store_coefficients(struct_pressure_temperature_coefficients *unpacked_coefficients);
void cr_print_coefficients(char * title, struct_pressure_temperature_coefficients *unpacked_coefficients);
void cr_print_temperature_formula(struct_pressure_temperature_coefficients *unpacked_coefficients,  int traw, int kT);
void cr_print_pressure_formula(struct_pressure_temperature_coefficients *unpacked_coefficients, int traw, int praw, int t_kT, int p_kT);
