// System Service prototypes
//    These are functions that user code can call to access "system
//    services

// Debug functions
extern void ctc_debug_print_string(uint level, char *format_string);

// File Services
extern uint ctc_fopen(char *filename, uint flags);
extern uint ctc_fclose(unsigned int file_ptr);



// User Code base
// By convention, this entry points marks the space reserved for user code

// Maximum size of user binary image in bytes
//     this is conservative -- for hook I've picked, we actually have ~22,000 bytes

extern const uint ctc_user_code_base[CTC_MAX_USER_SIZE_IN_UINT];

