//
// timelapse.h
// 
// Prototype declaration for timelapse additions

// 


// External Global Variables

// Here is a global variable we stole from the string space used in the 
//   the entry function we hijacked -- cmdFPGA_CsdspPV
extern unsigned int g_last_timelapse_time_in_ms;

extern void TaskTimeLapseFSM_task0();
extern void TaskTimeLapseFSM_task1();
extern void TaskTimeLapseFSM_task2();
extern void TaskTimeLapseFSM_task3_ae_set();
extern void TaskTimeLapseFSM_task4();
extern void TaskTimeLapseFSM_task5();
extern void TaskTimeLapseFSM_task6();
extern void TaskTimeLapseFSM_task7();
extern void TaskTimeLapseFSM_task8_CopyJPGFromRAM();
extern void TaskTimeLapseFSM_task9();
extern void TaskTimeLapseFSM_task10_WaitMountSD();
extern void TaskTimeLapseFSM_task11_openTLfile();
extern void TaskTimeLapseFSM_task12();
extern void TaskTimeLapseFSM_task13();
extern void TaskTimeLapseFSM_task14_end();



// Internal Global Variables
struct_hp5_menu_item g_wbwl_timelapse_frequency_menu[13];

#ifdef TLPS_NIGHT_DAY
struct_hp5_menu_item g_wbwl_timelapse_period_menu[7];
#endif

short g_wbwl_timelapse_frequency_lookup_table[12];

// Functions
short tlps_encoded_timelapse_frequency_to_seconds(int index);

void tlps_tty_printf(char * format_string, int mode);

#if (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
void tlps_TaskTimeLapseFSM_task4(void);
#endif

void tlps_TaskTimeLapseFSM_task12a(void);

void tlps_update_system_measurements();


int tlps_Pressure_sensor_getReading(int * pressure, int * temperature);

