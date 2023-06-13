// 
// WBWL.h
// Structures and Constants defined for new functions

#define WBWL_WHITE_FLASH

// Bit Hacking for Cold Management

#define WBWL_SD_MANAGEMENT_LSBIT      0
#define WBWL_SD_MANAGEMENT_N_BITS     1
#define WBWL_EXTENDED_SD_POWER_LSBIT  1
#define WBWL_EXTENDED_SD_POWER_N_BITS 1
#define WBWL_DATE_FORMAT_LSBIT        2
#define WBWL_DATE_FORMAT_N_BITS       2
#define WBWL_TIME_FORMAT_LSBIT        4
#define WBWL_TIME_FORMAT_N_BITS       1

#define WBWL_DSLR_TRIGGER_LSBIT       5
#define WBWL_DSLR_TRIGGER_N_BITS      1

#define WBWL_APERTURE_N_BITS          2
#define WBWL_APERTURE_LSBIT           0



#define GET_BYTE_N_BIT(data, n, lsbit) ((data >> lsbit) & ((1 << n)-1))
#define SET_BYTE_N_BIT(data, field, n, lsbit) ((data & (0xff ^ (((1 << n)-1) << lsbit))) | ((field & ((1 << n)-1)) << lsbit))


// Number of entries in the factory menu handling function array

#if (defined BTC_7E) || (defined BTC_8E)
#define WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS   25 
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4) 
#define WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS   25 
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5) 
#define WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS   26 
#endif 



#define WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS   5
