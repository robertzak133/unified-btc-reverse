//
// custom-settings.h
//
// Functions to allow saving and restoring custom camera settings
//     from a file on the SD card


// Name and location of file we'll be using to load and store 
//      the custom configuration

#if (defined BTC_7A)
#define CST_CUSTOM_CONFIG_FILENAME "D:\\CUSTOM78A.BIN"
#elif (defined BTC_7E) || (defined BTC_8E)
#define CST_CUSTOM_CONFIG_FILENAME "D:\\CUSTOM780.BIN"
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4) 
#define CST_CUSTOM_CONFIG_FILENAME "D:\\CUSTOM781.BIN"
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5) 
#define CST_CUSTOM_CONFIG_FILENAME "D:\\CUSTOM782.BIN"
#endif 
