
#if defined(VM_OTA)

#define VM_OTA_MAX_VM 2
#define VM_OTA_MAX_BC 2
#define VM_OTA_RECORD 0
#define VM_OTA_VM_ADDR(idx) ( ((idx)%(VM_OTA_MAX_VM)) ? (0x110000):(0x10000))
#define VM_OTA_BYTECODE(idx) ( ((idx)%(VM_OTA_MAX_BC)) ? (0x290000):(0x210000))
#define VM_OTA_NEXT_BC_SLOT(curbc) (((curbc)+1)%(VM_OTA_MAX_BC))
#define VM_OTA_NEXT_VM_SLOT() (((VM_OTA_INDEX)+1)%(VM_OTA_MAX_VM))
#define VM_OTA_VMSTORE_ADDR(addr)   (((addr)<0x110000) ? (0x390000):(0x391000))


#define VM_OTA_STORE(idx) ( ((idx)%(VM_OTA_MAX_VM)) ? (0x391000):(0x390000))
#define VM_OTA_VM_ZONE_BEGIN 0x10000
#define VM_OTA_VM_ZONE_END 0x210000

#define VM_OTA_FLASH_CHUNK 4

#ifndef VM_OTA_INDEX
#define VM_OTA_INDEX 0
#endif

#define VM_OTA_MAP_ADDRESS(x) ((x))
#define VM_OTA_UNMAP_ADDRESS(x) ((x))

#define VM_OTA_PREFERRED_CHUNK 512

//#define VM_OTA_NEXT_BC_ADDRESS(addr)  (((addr)==0x210000) ? (0x290000):(0x210000))
#endif
