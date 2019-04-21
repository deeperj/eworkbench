#ifndef __DTYPES_H
#define __DTYPES_H
#include "stm32f30x.h"
#include "stm32f30x_rtc.h"

#include <stdbool.h>

#define RX_OBJ_BUFF_SIZE 1024 
#define RX_OBJ_MAX_MESSAGES 50
typedef enum {OUTPUT = 1 , INPUT = 2} DataDirectionType ;

typedef struct
{
	GPIO_TypeDef * IO_Port;
	uint16_t IO_Pin;
	uint32_t IO_Rcc;
	GPIOPuPd_TypeDef IO_Pull;
	DataDirectionType Mode;
	uint32_t EXTI_Line       ;
	uint8_t EXTI_PinSource    ;
	uint8_t EXTI_PortSource   ;
	uint8_t EXTI_IRQChannel    ;
	EXTITrigger_TypeDef TriggerType ;
	uint8_t EXTI_Priority    ;
	uint8_t EXTI_SubPriority    ;
	bool Initialized;
}GPIOParamStruct;



typedef struct
{
char *	Name;
uint8_t	Type;
uint16_t CodeIndex;
}ControlType;





typedef struct
{
uint32_t MsgStart;
uint32_t MsgEnd;
bool BufferCycle;
bool NewMessage;	
}MessageRegisterType;

typedef struct
	{
MessageRegisterType Message[RX_OBJ_MAX_MESSAGES]; //holds data for every message received after \r\n
char RxBuffer[RX_OBJ_BUFF_SIZE] ;
uint32_t ReceiveCounter ;
uint32_t StoreMessagePointer;
uint32_t LastReadMessagePointer;		
//uint32_t CurrentDmaCounter	;
uint32_t LastDmaCounter	;
}USART_ReceiveObjectType;

typedef struct
{
USART_ReceiveObjectType UsartReceiveObject ;
USART_TypeDef* USARTn;
uint32_t BaudRate;
	bool ConfigRX;
	bool ConfigTX;
	bool RXNE_INT_EN;
	bool TC_INT_EN ;
	bool TXE_INT_EN;
	bool USE_DMA;
	//uint32_t  DMA_BUFFER; these will be taken from the receive object
	//uint32_t DMA_BUFFER_SIZE; 
	DMA_Channel_TypeDef * DMA_Channel;
bool Configured;	
	bool Busy;
	//NOTE: //available flag hasnt been inmplemented detect when unread bytes are available
bool available;
	
}USART_ConfigType;

typedef struct
{
	bool Timeout;	
uint32_t	CurrentCount;
uint32_t LastPeriodCount;	
	
uint32_t DelayTime; //this is the default delay time to be used for example autoreloadiung	
const uint32_t DefaultDelayTime;	
}DelayDataType;

typedef struct
{
		DelayDataType SleepDelay;
	//DelayDataType TestATCommand;
	DelayDataType UpdateScreen;
		DelayDataType LastWifiReset;
	DelayDataType TestRfm;
	DelayDataType LogThingspeak;
	DelayDataType MessageWait;
	DelayDataType RF_DataTimeout;
	DelayDataType SystemCheckIn;
		DelayDataType MillisecondIncrement;
		DelayDataType SendStatusReport;
			DelayDataType TestWiFiLink;
}
DelayStruct;

typedef enum {ON = 1, OFF = 0} SwitchState;

typedef enum{
	RED = 0,
	ORANGE = 1,
	GREEN = 2,
	BLUE2 = 3,

	RED2 = 4,
	ORANGE2 = 5,
	GREEN2 = 6,
	BLUE = 7,
}LedColour;

typedef struct
{
	//RTC_TimeTypeDef LastTime;
	RTC_DateTimeTypeDef LastDateTime;
	
float	Temperature;
	bool TemperatureUpdated;	
uint8_t Humidity;
bool HumidityUpdated;	
uint8_t Channel;
uint16_t SensorID;
uint32_t HitCount	;

}WeatherDataStruct;



typedef enum { //this enum specifies the memory location on the eeprom where these values are stored
eep_CalCheck_Compression_2B = 	0x000E,
EepSDSerial_4B = 0x0010,
EepDeviceSerial_6B = 0x0014,
	
eep_WWDG_Stack_base_41B = 0x0024,  //stores the addres of the last watchdog timer reset
} EEP_Location_type;

//define the structure of the callback function for the timout
typedef void (* TimeoutCallbackFunctionType)(void) ;


typedef enum {
_RTC_BKP_DR0	= RTC_BKP_DR0,
NVR_ResetCounter	= RTC_BKP_DR1,
NVR_SYSTEM_UPTIME = RTC_BKP_DR2, //used to backup system uptime
NVR_SYSTEM_UPTIME_OVERCOUNT	= RTC_BKP_DR3,
NVR_AutozeroPot = RTC_BKP_DR4,
NVR_ErrorStatus	= RTC_BKP_DR5,
NVR_WWDT_ADDRESS = RTC_BKP_DR6,
	NVR_DATUM_DAC_MS = RTC_BKP_DR7,
	NVR_DATUM_DAC_LS = RTC_BKP_DR8,
	NVR_HARDFAULT_ADDRESS = RTC_BKP_DR9,
_RTC_BKP_DR10 = RTC_BKP_DR10,

	//from RTC_BKP_DR11 onward we will use for byte based storage
	//from RTC_BKP_DR11 Start ///////////////////////////////
	NVR_ABMix = 		44		,
	NVR_MySlot = 				45,
	NVR_MyAxis = 				46,
	NVR_SystemInititalized = 47,
//	RTC_BKP_DR12 Start ///////////////////////////////
	NVR_AutozeroState = 	48,
	//NVR_AutozeroLSB = 	49,
	NVR_BenchTestMode = 50,
	NVR_AutoselStatus = 51,
//	RTC_BKP_DR13 Start ///////////////////////////////
	NVR_CurrentMuxen = 52,
	_free57 = 53,
	NVR_CurrentRange = 	54,
	//NVR_AutozeroLSB = 	55,
//	RTC_BKP_DR14 Start ///////////////////////////////
	_free56 = 56,
NVR_BootloaderRequest = 57,

NVR_ServedIdent_0 = 58,
NVR_ServedIdent_1 = 59,
//	RTC_BKP_DR15 Start ///////////////////////////////
NVR_ServedIdent_2 = 60,
NVR_ServedIdent_3 = 61,
NVR_ServedIdent_4 = 62,
//	_free63 = 63,
//	RTC_BKP_DR16 Start ///////////////////////////////
//	_free64 = 64,
//	_free65 = 65,
//	_free66 = 66,
//	_free67 = 67,
} NVRAM_Location_Type;

typedef enum {
IN_ClusterPowerStatus = 2,//	
IN_OperationStatus = 3,//
OUT_SetOperationState = 4,//	
OUT_SetClusterPowerLevel = 5,//
OUT_RequestConfiguration = 6,//
IN_StatusMessage = 7 ,//
IN_HardwareConfiguration = 8, //	
	

OUT_ControlOperation = 9,//	
OUT_10 = 10,//		
OUT_11 = 11,//		
IN_12 = 12,//
OUT_13 = 13,//
OUT_14 = 14,//
IN_15 = 15,//	
IN_16 = 16,//	
IN_17 = 17,//		

} INOUT_Reportids ;



typedef struct
{
	bool InWrongSlot; //BIT0
	bool FixedSlotInvalid; //BIT1
	bool InvalidAmpTypeForFixedSlot;//BIT2
	bool IdentRequestFailed;//BIT3
	bool EepromWriteError;//BIT4
	bool ProfileMemoryFull;//BIT5
	bool WatchdogTimerOverflow;//BIT6
	bool Autozero_RequestWhile_Prezero;//BIT7
	bool Oscillator_Demod_Fault;//BIT8
	bool WatchDog_Address_List_Full;//BIT9
	bool Power_Minus15V_Error;//BIT10
	bool Power_Plus15V_Error;//BIT11
	bool Power_Minus5V_Error;//BIT12
	bool Power_Plus5V_Error;//BIT13
	bool Power_24V_Error;//BIT14
	bool Range_Output_Circuit_Error;//BIT15
	bool Input_Circuit_Test_Error;//BIT16
	bool Hard_falt_Exception;//BIT17
	bool SPARE18;//BIT18
	bool SPARE19;//BIT19
	bool SPARE20;//BIT20
	bool SPARE21;//BIT21
	bool SPARE22;//BIT22
	bool SPARE23;//BIT23
	bool SPARE24;//BIT24
	bool SPARE25;//BIT25
	bool SPARE26;//BIT26
	bool SPARE27;//BIT27
	bool SPARE28;//BIT28
	bool SPARE29;//BIT29
	bool SPARE30;//BIT30
	bool SPARE31;//BIT31
}ErrorStatusStruct;


#endif /* __MAIN_H */  


