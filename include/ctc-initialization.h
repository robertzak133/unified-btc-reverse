//
// Customer Trail Camera (CTC) Initialization

// A series of functions to enable a user-specified binary to run
//   in a mostly unmodified Trail Camera firmware environment

// 2021-08-31 zak: created



// Defines

#define CTC_USER_BINARY_FILENAME "A:\\CTC\\USER.BIN"

#define CTC_MAX_USER_SIZE 10000
#define CTC_MAX_USER_SIZE_IN_UINT (CTC_MAX_USER_SIZE >> 2)

// User Function Table Entry

void uctc_init();
// Public Interface Prototypes

void ctc_init();
void ctc_initCodeSentry(uint dev_type);

// System Services
void ctc_error_printf(char * format_string, ...);


// Private Interface Prootypes
uint ctc_check_for_user_binary(char * file_name, uint *file_ptr);

int ctc_load_user_binary(uint user_bin_file_ptr, uint file_size);


