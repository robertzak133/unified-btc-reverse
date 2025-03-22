//
// native-quality.c
//    Adds a mode to "photo quality" menu for "native" 
//    This sets the quality to be the native resolution of the sensor

#include "BTC.h"
#include "WBWL.h"
#include "menus.h"
#include "native-quality.h"

#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) 
ushort g_npr_photo_resolution_string_lookup_table[5] = {
  SST_4MP,
  SST_8MP,
  SST_12MP,
  SST_20MP,
  SST_2MP
};
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4) 
ushort g_npr_photo_resolution_string_lookup_table[5] = {
  SST_4MP,
  SST_8MP,
  SST_12MP,
  SST_22MP,
  SST_2MP
};
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5) 
ushort g_npr_photo_resolution_string_lookup_table[5] = {
  SST_4MP,
  SST_8MP,
  SST_12MP,
  SST_24MP,
  SST_2MP
};
#else
**** ERROR : Unrecognized Camera Targer ****
#endif

struct_hp5_menu_item g_ntvq_photo_quality_menu[6] = {
  {no_icon, SST_LOW_SP__LB_4MP_RB_ ,    0x0, 0x1, 0x0, 0x1, 0x1},
  {no_icon, SST_MEDIUM_SP__LB_8MP_RB_ , 0x0, 0x1, 0x0, 0x1, 0x1},
  {no_icon, SST_HIGH_SP__LB_12MP_RB_ ,  0x0, 0x1, 0x0, 0x1, 0x1},
  {no_icon, SST_ULTRA_SP__LB_20MP_RB_ , 0x0, 0x1, 0x0, 0x1, 0x1},
  {no_icon, SST_NATIVE_LB_2M_RB_ ,      0x0, 0x1, 0x0, 0x1, 0x1},
  {no_icon, SST_PHOTO_SP_QUALITY,       0x0, 0x0, 0x1, 0x3, 0x3}
};


struct_photo_dimensions_int *ntvq_get_camera_photo_resolution(struct_photo_dimensions_int *photo_dimensions, enum_photo_quality encoded_photo_quality) {

  if (encoded_photo_quality > 1000) {
    // Dummy (never taken) branch just to get the function below into the symbol table
    return get_camera_photo_resolution(photo_dimensions, encoded_photo_quality);
  }
  if (encoded_photo_quality <= ultra_20MP) {
    photo_dimensions->width = (uint) g_image_resolution_lookup_table[(uint)encoded_photo_quality].width;
    photo_dimensions->height = (uint) g_image_resolution_lookup_table[(uint)encoded_photo_quality].height;
    photo_dimensions->width_hi = 0;
    photo_dimensions->height_hi = 0;
  } else {
    get_multi_shot_photo_dimensions(photo_dimensions);
  }
  return photo_dimensions;
}



void npr_draw_sst_string_on_display (int param_1,int param_2,void *param_3,int *param_4,int param_5,char *format_string,
				     int param_7,int param_8) {
  enum_multi_shot_encoding multi_shot_encoding = get_cold_item_multi_shot_encoding();
  enum_photo_quality photo_resolution;

  if (multi_shot_encoding <= ms_single_shot) {
    // In single shot, and standard multi shot, resolution is what we set the camera for
    photo_resolution = get_cold_item_photo_resolution();
  } else {
    // In multi shot mode resolution is sensor native, 2MP.  Fixing a bug of omission in the factory code while
    //    I'm here.  I know, a complete waste of time :(
    photo_resolution = native_2MP;
  }
  int photo_resolution_string_id = g_npr_photo_resolution_string_lookup_table[photo_resolution];
  draw_sst_string_on_display (param_1,param_2,param_3,param_4,param_5,format_string, param_7, photo_resolution_string_id);
}
