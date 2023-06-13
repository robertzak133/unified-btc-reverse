// cold-storage.h

// Function prototypes for storing/restorign items from internal file system


typedef struct struct_cs_bundle {
  boolean extern_trigger_p;

} struct_cs_bundle;

void cs_on_power_up(void);
void cs_on_power_down(void);
