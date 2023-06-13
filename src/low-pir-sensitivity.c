//
// low-pir-senstivity.c
// 
// 2022-11-12 Zak: Created
// code that adds a "short range" setting below "normal" and "long" range PIR sensitivyt
//      setting.
// Includes two components
//    * code for extending the menu entry
//    * code to actually change the senstivity of the PIR sensor
// 2022-11-27 Zak: Tabled for the HP5 series.  The HP5 has a discrete amplifier and 
//      single bit control line which doesn't allow an encoding of more than two
//      sensitivity setting.  Keep this code around in case future cameras 
//      contain "digi-pyro" parts
//

#include "BTC.h"
#include "utilities.h"
#include "low-pir-sensitivity.h"


struct_hp5_menu_item g_lps_pir_range_menu[4] = {
   // First
  {
    0x20, 0x31, 0x00, 0x01, 0x00, 0x1, 0x1
  },
   // Second
  {
    0x20, 0x32, 0x00, 0x01, 0x00, 0x1, 0x1
  },
   // Third
  {
    0x20, 0xb8, 0x00, 0x01, 0x00, 0x1, 0x1
  },
  // Fourth
  {
    0x20, 0x33, 0x00, 0x00, 0x01, 0x03, 0x03
  }
};

void lps_handlePIRRangeMenu(void) {


}


void lps_set_pir_sensor_range(enum_pir_range_options pir_range_option) {
  byte mcu_register_value;
  struct_mpu_spi_data mpu_spi_data;
  struct_mpu_spi_address mpu_spi_address;
  
  getMCURegisterByte(0xe,&mcu_register_value);

  mpu_spi_address.addr0 = 0xf;
  mpu_spi_address.addr1 = 0x10;
  mpu_spi_address.addr2 = 0xe;

  mcu_register_value = mcu_register_value & 0xf0;
  mpu_spi_data.data2 = mcu_register_value | 8;


  switch(pir_range_option) {
  case pir_short_range:
    mpu_spi_data.data0 = 0xff;
    mpu_spi_data.data1 = 0x00;
    break;
  case pir_normal_range:
    mpu_spi_data.data0 = 0xff;
    mpu_spi_data.data1 = 0x00;
    break;
  case pir_long_range:
    mpu_spi_data.data0 = 0x00;
    mpu_spi_data.data1 = 0xff;
    break;
  default:
    // Defaults to "normal"
    // 2022-11-14 -- note (unreachable) call to hooked function and 
    //               data value (g_pir_range_menu) so that they end up 
    //               in the symbol table
    set_pir_sensor_range(pir_range_option);
    mpu_spi_data.data0 = (byte) g_pir_range_menu[0].text_id;
    mpu_spi_data.data1 = 0;
    break;
  } 

  WrappedMPUSpi_WriteNPacketByManualPWM(&mpu_spi_address,&mpu_spi_data,3);
  return;
}

