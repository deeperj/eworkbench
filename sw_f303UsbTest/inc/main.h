

#ifndef __MAIN_H
#define __MAIN_H
//multiplication factors for calculating the powe and signal voltages from the adc

#include "stm32f30x.h"
#include "STM32F303_HAL.h"
//#include "DataTypes.h"  //here we difined all the global data types used



//typedef struct
//{
//uint32_t MsgStart;
//uint32_t MsgEnd;
//bool BufferCycle;
//bool NewMessage;	
//}MessageRegisterType;

//typedef struct
//	{
//MessageRegisterType Message[RX_OBJ_MAX_MESSAGES]; //holds data for every message received after \r\n
//char RxBuffer[RX_OBJ_BUFF_SIZE] ;
//uint32_t ReceiveCounter ;
//uint32_t StoreMessagePointer;
//}USART_ReceiveObjectType;


#define TOTAL_WWDG_RECORD  20

	#define TOTAL_ATT_LEVELS 3
	
#define WWDG_STACK_OFFSET  10

#define MAX_PROFILE_EEP_MEMORY (eep_profile_end - eep_profile_base)   //total number of eeprom bytes that the profile memory can use


#define MAX_USB_TIMEOUT 10


#define I2Cx_FLAG_TIMEOUT             ((uint32_t)0x1000)
#define I2Cx_LONG_TIMEOUT             ((uint32_t)(10 * I2Cx_FLAG_TIMEOUT))  
/* Uncomment the following line to use the default LSM303DLHC_TIMEOUT_UserCallback() 
   function implemented in stm32f3_discovery_lgd20.c file.
   LSM303DLHC_TIMEOUT_UserCallback() function is called whenever a timeout condition 
   occure during communication (waiting transmit data register empty flag(TXE)
   or waiting receive data register is not empty flag (RXNE)). */   
/* #define USE_DEFAULT_TIMEOUT_CALLBACK */

/* Maximum Timeout values for flags waiting loops. These timeouts are not based
   on accurate values, they just guarantee that the application will not remain
   stuck if the I2C communication is corrupted.
   You may modify these timeout values depending on CPU frequency and application
   conditions (interrupts routines ...). */   



#define DUMMY_MESSAGE_ID_USE_MACRO MessageID++; MessageID-- ;

#define NUM_OVERRIDES 5

#define LIN_TABLE_FLASH_ADDRESS  0x08032000 //the sector to start LINEARization table writing from

#define TIME_PwrUpCntr 1000000 //one second for power up dalay
#define TIME_PwrDownCntr 1000000   //500 ms after power loss before we change power state
#define TIME_OSCILLATOR_FAULT_DELAY TIME_PwrDownCntr * 2 // twice the time for power down so we dont raise oscillator fault flag as a result of power faileure
//#define TIME_MUX_SWITCH_DELAY 20000 
/* Includes ------------------------------------------------------------------*/
#define NUM_SETUP_POINTS 50  //sets the number of linearization point to use on each side of each range 
//#define NUM_CORRECTION_POINTS 200  //too points per side per range hence 200 x 2 x 4 ranges 
#define SIZ_DEVICE_SERIAL 6 


#define SIZ_ROM_CODE_BYTES 8 //number of bytes contained inthe rom code array

#define DATA_STRING_BUFFER_SIZE 4000   //alter this to 12000 to test overflow routine//16000


#define TOTAL_WEATHER_SENSORS 10

//#define PROF_STRING_BASE 5   //the locationon the profile report where the description text starts


//used to detect th sero crossing moment of the output signal

/*---------------------------DEFINE GPIO PINS USED HERE--------------------------------*/
/////////////////////////////////////////////////////////////////////////////////////////////

#define RED_LED_Port 															GPIOE
#define RED_LED_Pin 																GPIO_Pin_9
#define RED_LED_RCC_AHBPeriph 											RCC_AHBPeriph_GPIOE

#define GREEN_LED_Port 															GPIOE
#define GREEN_LED_Pin 																GPIO_Pin_11
#define GREEN_LED_RCC_AHBPeriph 											RCC_AHBPeriph_GPIOE

#define BLUE_LED_Port 															GPIOE
#define BLUE_LED_Pin 																GPIO_Pin_8
#define BLUE_LED_RCC_AHBPeriph 											RCC_AHBPeriph_GPIOE

#define ORANGE_LED_Port 															GPIOE
#define ORANGE_LED_Pin 																GPIO_Pin_10
#define ORANGE_LED_RCC_AHBPeriph 											RCC_AHBPeriph_GPIOE



#define RED2_LED_Port 															GPIOE
#define RED2_LED_Pin 																GPIO_Pin_13
#define RED2_LED_RCC_AHBPeriph 											RCC_AHBPeriph_GPIOE

#define GREEN2_LED_Port 															GPIOE
#define GREEN2_LED_Pin 																GPIO_Pin_15
#define GREEN2_LED_RCC_AHBPeriph 											RCC_AHBPeriph_GPIOE

#define BLUE2_LED_Port 															GPIOE
#define BLUE2_LED_Pin 																GPIO_Pin_12
#define BLUE2_LED_RCC_AHBPeriph 											RCC_AHBPeriph_GPIOE

#define ORANGE2_LED_Port 															GPIOE
#define ORANGE2_LED_Pin 																GPIO_Pin_14
#define ORANGE2_LED_RCC_AHBPeriph 											RCC_AHBPeriph_GPIOE



#define DFU_Btn_Port 							GPIOA
#define DFU_Btn_RCC_AHBPeriph 		RCC_AHBPeriph_GPIOA
#define DFU_Btn_Pin 							GPIO_Pin_0

#define Buzzer_Port 							GPIOC
#define Buzzer_RCC_AHBPeriph 		 RCC_AHBPeriph_GPIOC
#define Buzzer_Pin 							 GPIO_Pin_6

uint32_t RTC_GetTotalDays(uint8_t year, uint8_t month,uint8_t date);
uint8_t RTC_GetWeekday(uint8_t year, uint8_t month,uint8_t day);
RTC_DateTimeTypeDef RTC_GetDateTimeFromSeconds(uint32_t DateTimeSeconds);
uint32_t RTC_GetDateTimeSeconds(RTC_DateTimeTypeDef StartDateTime);
int32_t RTC_GetDateTimePeriod(RTC_DateTimeTypeDef StartDateTime, RTC_DateTimeTypeDef EndDateTime);
char *  RTC_GetDateTimeString(RTC_DateTimeTypeDef * DateTime);
RTC_DateTimeTypeDef RTC_GetDateTimeOffset(RTC_DateTimeTypeDef CurrentTime,int32_t TimeSeconds);

uint32_t  millis(void);

void RF_SetDefaultCodes(void);
void SetHomeLocations(void);
void LedBlink(LedColour Colour , uint32_t delay);
void LedState(LedColour Colour , SwitchState State );
void ConfigDebugUsart(void);
extern  USART_ConfigType DEBUG_USART_Config ;
ErrorStatus LogWeatherDataToFile(WeatherDataStruct * WeatherData);

typedef struct{
bool	button1;
bool	button2;
bool	button3;
bool	button4;
	bool	button5;
		bool	button6;
			bool	button7;
				bool	button8;
			
}buttonstruct;

typedef union {
	buttonstruct buttons;
	uint8_t all_buttons;
}mouse_buttons;

  typedef struct  {
     mouse_buttons  buttons;
      int8_t x;
      int8_t y;
      int8_t wheel;
  }mouse_report;
	

		typedef union{
				uint8_t raw[4];
				mouse_report mouse;
				}usb_mouse_union;
		 
extern const NVRAM_Location_Type NVR_ServedIdents[];

//make this accessible to the receive usart interrupt
extern USART_ReceiveObjectType DEBUG_UsartReceiveObject;

extern  DelayStruct GlobalDelay;
extern volatile bool InitializationComplete ;//---------------------------*/
extern volatile bool USB_Packet_Recieved;

extern  ErrorStatusStruct  ErrorStatusBits1;
int32_t SearchStringForPattern(char * String , char * Pattern , uint32_t StringLength );

uint16_t ComputeMeanInt16( volatile uint16_t * Array, uint8_t Count);
//ErrorStatus SendHttpPostRequest(char * IpAddress,char * PostUrl,uint32_t UrlLen ,char * PostBody,uint32_t BodyLen );
uint32_t ComputeMeanInt32( volatile uint32_t * Array, uint8_t Count);
uint32_t  USART_DMA_MarkMessagePointer(USART_ConfigType * UsartObject);
uint32_t  USART_DMA_GetCurrentPointer(USART_ConfigType * UsartObject);
char * itoha (unsigned int num);
uint32_t GetAsciiDeviceList(char * String,uint16_t * Array);
uint32_t GetAsciiControlsList(char * String,ControlType * Array);
extern volatile uint32_t SystickCount_us ;
extern volatile  uint32_t CurrentCount;

extern volatile uint8_t EepExitCode ;
	void CRC_Config8Bits(uint8_t poly);
uint8_t CRC_Cal8Bits(uint8_t* data, uint32_t size);

float Bytes2Float(uint8_t * Bytes);
ErrorStatus Float2Bytes( float FloatVal, uint8_t * Bytes);

void SecondsCallback (void);
	void MillisecondsCallback (void);
	void RTC_Config(void);
	
uint32_t GetNumberDifference(uint32_t Value1, uint32_t Value2);
float GetNumberDifferenceFloat(float Value1, float Value2);

typedef void (*usb_mouse_report_ready_cb_f)(void);

extern   uint8_t Receive_Buffer[];



void Acc_Config(void);
void Acc_ReadData(float* pfData);

void configGPIO(void);

uint32_t GetStringLength(char * String);

void USART_sprintf(uint32_t Data);
ErrorStatus USART_Send_String(USART_ConfigType * USART_Conf,  char *s);
ErrorStatus USART_Send_Char(USART_ConfigType * USART_Conf,unsigned char Data);
	ErrorStatus USART_Send_Int(USART_ConfigType * USART_Conf,uint32_t Data);
void USART_Newline(USART_ConfigType * USART_Conf);
ErrorStatus ESP8266_Init(void);
//ErrorStatus write(USART_ConfigType * USART_Conf,char s);
ErrorStatus println(USART_ConfigType * USART_Conf,char *s);

uint8_t  USART_ReadBuffer(USART_ConfigType * ReceiveObject);
bool  USART_BytesAvailable(USART_ConfigType * ReceiveObject);

ErrorStatus ConfigureIOPin(GPIOParamStruct * Pindata, bool ConfigInterrupt);

void USARTx_TIMEOUT_UserCallback(void);



ErrorStatus USB_QUIET_MODE(FunctionalState State);
uint32_t USART_DMA_ScanBytes(USART_ConfigType * USART_Config);
static void ADC_Config(void);
void USART_Receive_Data(USART_ConfigType * ReceiveObject);
void USB_Packet_Handler(void);

ErrorStatus USART_Configuration(USART_ConfigType * USART_Config);

ErrorStatus  CompareString( char * char1,  char * char2, unsigned int count);
ErrorStatus  CopyString( char * charfrom,  char * charto, unsigned int count);

//ErrorStatus DEBUG_MessageHandler(USART_ReceiveObjectType * ReceiveObject, uint32_t MesgIndex);
uint8_t	SPI_Send_Data(SPI_TypeDef * SPI_Base , uint8_t SPI_Data, TimeoutCallbackFunctionType TimeoutCallback);
//int32_t SearchMessageForResponse(MessageRegisterType * Message, char * Pattern );
int32_t SearchMessageForResponse(USART_ReceiveObjectType * ReceiveObject, uint32_t MesgIndex, char * Pattern );
ErrorStatus I2Cx_Write( I2C_TypeDef * I2Cx, uint8_t I2Cx_ADDRESS, uint8_t* pBuffer, uint8_t WriteAddr, uint16_t NumByteToWrite, TimeoutCallbackFunctionType TimeoutCallback);
ErrorStatus I2Cx_Read( I2C_TypeDef * I2Cx, uint8_t I2Cx_ADDRESS, uint8_t* pBuffer, uint8_t ReadAddr, uint16_t NumByteToRead ,TimeoutCallbackFunctionType TimeoutCallback);

//extern volatile uint32_t SystickCount_ms;

ErrorStatus I2C_Config(I2C_TypeDef * I2Cx);
void BootLoaderInit(void);
int32_t String_FindCharIndex(char * String, uint32_t StartIndex, uint32_t EndIndex, char FindChar);
ErrorStatus SetDateTimeFromString(char * String);
	//char * GetCurrentDateTime(void);
//void USART_Receive_Data(USART_TypeDef* USART);
//uint32_t GetSystemUptime_ms(void);

uint32_t ReadEeprom(EEP_Location_type Address, uint8_t NumBytes);
ErrorStatus  WriteEeprom(EEP_Location_type Address, uint32_t WriteData,uint8_t NumBytes);
int StringReplaceChar(char *str, char orig, char rep,uint32_t strlen) ;
void SendStatusReport(void);
void SendConfigurationReport(void);
	
void RF_OOK_Receive(void);
	
	int32_t CheckForWeatherSensorUpdate(uint16_t SensorID);
	
	ErrorStatus UpdateThingspeakTemperatureChannel(void);
		ErrorStatus UpdateThingspeakHumidityChannel(void);
		
void Delay_ms(uint32_t ms);
	void Delay_us(uint32_t ms);
	
void TimingDelay_Decrement(void);
extern char MessageReportStringBuff[];
//should this be changed to long jump
void TIMEOUT_UserCallback(void);

ErrorStatus WaitPrevXferComplete(void);

void UpdateErrorStatus(void);
ErrorStatus UpdateWeatherSensorData(uint64_t SensorCode, uint8_t TotalBits, uint32_t DataTime);

void ReadADCValues(uint8_t index);  //this read the two multiplexed adc values and store in the array

void InitializeSystemChips(void);
void ReloadWatchdogCounter(void);
void SystemReset(void);
void	DisableWatchdog(void);
void ConfigureWatchdog(void);

bool CheckDelayTimeout( DelayDataType * Delay); //check if a global delay item has timed out
ErrorStatus StartGlobalDelayTimeout(DelayDataType * Delay,uint32_t Delaytime);

void SetSystemDateTime(uint8_t * DateBuf);

ErrorStatus SendControlStatusReportIN(void);
ErrorStatus SendControllerVarsReportIN(void);

ErrorStatus SendControlMessageReportIN(uint8_t MsgID, int Param, char * MessagePtr );



uint8_t NVRAM_ReadByte(NVRAM_Location_Type location);
void NVRAM_WriteByte(NVRAM_Location_Type location, uint8_t data);


//void WriteLogFile(  char *LogString);

#endif /* __MAIN_H */  


