// monitor bDeviceState
# include "main.h"

# include <stm32f30x.h>
#include <string.h>
#define FW_REVISION 1.002
#define CustomBootloaderAddress 0x08000000
#define SysMemBootloaderAddress 0x1FFFD800


	
#define MAX_PROGRAM_SIZE 0x00032000  //thi is the maximum space the program must occupy ti leave room for linearization data
//this limitation must be put in the project options options
#define SECTOR_SIZE  0x800


#define USART_TIMEOUT_FLAG ((uint32_t)0x1000)
#define USART_TIMEOUT_LONG ((uint32_t)(10 * USART_TIMEOUT_FLAG)) 
volatile uint32_t UsartTimeout =	0;
//volatile bool IN_LOG_WRITE = FALSE;
char DeviceSerial[SIZ_DEVICE_SERIAL+1]; //1 for the null terminator 

volatile uint32_t CurrentFiringTime = 0;


//volatile uint32_t UpdateCycle = 0;






volatile int32_t BtnDownCnt = 0 ;
volatile uint8_t FillValue = 0;

//RFCodeDataType TestPmd ; 
char DataString[DATA_STRING_BUFFER_SIZE];

//extern char ESP8266_USART_Config.UsartReceiveObject.RxBuffer[] ;
uint32_t DataOverflowTrack = 0 ;
uint32_t I2Cx_TIMEOUT_COUNT;
uint32_t  I2Cx_Timeout;

volatile uint32_t 	TempLogStringCnt = 0 ;

bool TEST_TRAP1 = FALSE;



uint32_t SendCntr ;

char CurrentDateTimeString[25];

#define SPI_MAX_TIMEOUT 40000
__IO uint16_t SPI_Timeout = SPI_MAX_TIMEOUT;

volatile bool USE_SYSMEM_BOOT = FALSE;

volatile bool  USB_CABLE_PLUGGED = FALSE ; //default this to true so that the 
volatile bool LAST_CABLE_STATE = FALSE ;

bool RTCWasReset = FALSE;

bool DATE_TIME_SET = FALSE;

		RTC_DateTimeTypeDef TestDateTime;
	RTC_DateTimeTypeDef SystemDateTimeStructure;
	RTC_DateTimeTypeDef TempDateTime;
	int32_t TestDateTimeOffset ; //date time offset in seconds
int32_t TestDateTimeOffsetCnt = 3739;

volatile uint32_t ToneFreq = 5000;

volatile DEVICE_STATE CurrentUsbState;

uint8_t Receive_Buffer[USB_EP1_MAX_BUFFER_SIZE];

uint8_t Transmit_Buffer[USB_EP1_MAX_BUFFER_SIZE];

 USART_ConfigType DEBUG_USART_Config ;

 
volatile bool USB_Packet_Recieved = FALSE;
//volatile uint8_t UsbComputedCRC;

uint8_t x = 0;


//#define BuildDay  BUILD_DAY ;
const char *  DatePointer __attribute__((at(0x08006400))) = __DATE__ ; 
const char * TimePointer __attribute__((at(0x08005500))) = __TIME__ ;

DelayStruct GlobalDelay ;

char MessageReportStringBuff[200]; //size limited by max buffer size for our usb

volatile uint32_t SystickCount_us = 0; //reset the counter to 0 then systick will start incrementing it.
//volatile uint32_t SystickCount_ms = 0;
volatile uint32_t SystemUptime_Ovf = 0;

volatile uint32_t LoopLatency;
//volatile uint32_t segment;
USART_TypeDef* DEBUG_USART = USART2 ;

volatile bool InitializationComplete = FALSE;

volatile uint32_t ReSetCount;

RCC_ClocksTypeDef RCC_Clocks;

volatile bool IN_USB_HANDLER = FALSE;

//volatile bool APPLY_LINEARIZATION = FALSE;
volatile uint8_t USB_Timeout_Counter = 0;
volatile uint32_t WWDG_EventAddress = 0; //temporearily holds the ddwg event address before it it properly stored on nvram and eeprom

volatile uint8_t EepExitCode = 0;

volatile uint32_t UsbInitDelay = 0;  //the delay before starting usb in the main loop
volatile bool USB_INITIALIZED = FALSE; //flag to tell when usb has been inititalized

volatile uint32_t LastLoopPeriod = 0;

ErrorStatusStruct ErrorStatusBits1;
volatile ErrorStatusStruct LastErrorStatusBits1;
volatile uint32_t CurrentErrorStatusVal = 0; //this hold the bit ordered 32 bits value of Errorstatus bits
uint32_t ErrorTempVal, errorindex, errorindex1 = 0;

volatile bool STATUS_TRANSMIT = TRUE;
volatile bool EnterBootloader = FALSE;

__IO uint8_t PrevXferComplete = 1;  //semaphore ???

__IO uint32_t TimingDelay = 0; //hide with a function??

__IO uint32_t Xfer_Decrement = 0;

bool SELF_TEST = FALSE;
uint8_t TestCount =0;
uint32_t SelfTestDelay;
uint8_t TESTDELAY2 = 1; //time in seconds for test delay loop
uint8_t TESTDELAY = 5; //time in seconds for test delay loop
uint8_t TEST_LEVEL = 60;

volatile bool COPY_EEPROM = FALSE;
volatile bool WIPE_EEPROM = FALSE;

__IO uint32_t  Test_Variable = 0 ; //this is just used to hold random data while debugging

uint32_t Test_Variable2 = 0;

uint8_t temp;
uint8_t dat;
uint16_t datskip = 0;
uint8_t seq, v;

GPIO_InitTypeDef GPIO_InitStructure; //create the structure used for inititalizing the gpio

void (* SysMemBootJump)(void);


bool SEND_SERIAL_DATA = FALSE ;

GPIOParamStruct LedsGpio[]=
{
{RED_LED_Port,RED_LED_Pin,RED_LED_RCC_AHBPeriph},
{ORANGE_LED_Port,ORANGE_LED_Pin,ORANGE_LED_RCC_AHBPeriph},
{GREEN_LED_Port,GREEN_LED_Pin,GREEN_LED_RCC_AHBPeriph},
{BLUE_LED_Port,BLUE_LED_Pin,BLUE_LED_RCC_AHBPeriph},

{RED2_LED_Port,RED2_LED_Pin,RED2_LED_RCC_AHBPeriph},
{ORANGE2_LED_Port,ORANGE2_LED_Pin,ORANGE2_LED_RCC_AHBPeriph},
{GREEN2_LED_Port,GREEN2_LED_Pin,GREEN2_LED_RCC_AHBPeriph},
{BLUE2_LED_Port,BLUE2_LED_Pin,BLUE2_LED_RCC_AHBPeriph},

		};

 bool LedInverted[]= 
{
	FALSE , //Red inverted
	FALSE, //Green inverted
	FALSE,	//Blue inverted
	FALSE,	//ORANGE inverted
	FALSE , //Red inverted
	FALSE, //Green inverted
	FALSE,	//Blue inverte
	FALSE,	//ORANGE inverted
};


int main(void)
{
	uint8_t MessageID = 8;
	
	InitializationComplete = FALSE;
		
	NVIC_SetVectorTable(NVIC_VectTab_FLASH, 0x3000);

	/* 2 bit for pre-emption priority, 2 bits for subpriority */
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);

	__disable_irq();                            // Disable all interrupts until after initialization

	////	CORRECT THE SYSTICK TIMING ////
	/* SysTick end of count event each 10ms */
	RCC_GetClocksFreq(&RCC_Clocks);  //get the clock settings as configures by systemXXX.c
	SysTick_Config(RCC_Clocks.HCLK_Frequency / 1000000); //set the systick period for 1us interval

	NVIC_SetPriority(SysTick_IRQn, 0); /* set Priority for Systick Interrupt */
									   /* stm32 uses 4 bits to store preemption and sub priorities, the high bits are for preemption and low bits are for sub priority. 
									   If the parameter for priority is 0 for the function	above(that�s also what I had in the function), 0 is 0x00 in hex and 0000 in binary,
									   since the default priority grouping for stm32 is group 2, which is 2 bits for preemption	priority and 2 bits for sub priority, 
									   we get 00 for preemption and 00 for sub. If we change the input from 0 to 7 for the function, the binary form for 7 is 0111, so higher 2 bits is
									   01 which is 1 in decimal gives you preemption priority as 1, and the lower 2 bits is 11 which is 3 gives you sub priority as 3.
									   Note!! that higher number means lower priority	*/

	DBGMCU_Config(DBGMCU_SLEEP | DBGMCU_STANDBY | DBGMCU_STOP, ENABLE);
	DBGMCU_APB1PeriphConfig(DBGMCU_WWDG_STOP, ENABLE);//stop the watchdog timer when the cpu is halted during debugging

//I2C_Eeprom_Init();

//	ADC_Config(); //this calls the private function to configure ADC

	RTC_Config(); //the nvram of the rtc is used to store state to be remembered on non-power down resets

	configGPIO();
	
	GPIO_ResetBits(USB_DISCONNECT_PORT, USB_DISCONNECT_PIN);

	 ConfigDebugUsart();

	
	USART_Send_String( &DEBUG_USART_Config ,"System Startup . . . .\r\n" );	


	
	//check if the reset was caused by bootloader request, as a way to turn off the WWDG timer
	//when a enter bootloader request is made the  

	if (NVRAM_ReadByte(NVR_BootloaderRequest) == 0xA5)
	{
		//enter custom bootloader
		USE_SYSMEM_BOOT = FALSE;
		BootLoaderInit();
	}
	if (NVRAM_ReadByte(NVR_BootloaderRequest) == 0x5A)
	{
		//enter sysmem bootloader
		USE_SYSMEM_BOOT = TRUE;
		BootLoaderInit();

	}
	//setup the window watchdog timer
	ConfigureWatchdog();

	/* Configure the CRC peripheral to use the polynomial x8 + x7 + x6 + x4 + x2 + 1 */
	CRC_Config8Bits(0xD5);

	ReSetCount = (uint8_t)RTC_ReadBackupRegister(NVR_ResetCounter);
	//update Count
	ReSetCount++;
	//save back reg
	PWR_BackupAccessCmd(ENABLE);
	RTC_WriteBackupRegister(NVR_ResetCounter, (uint32_t)ReSetCount); //
	PWR_BackupAccessCmd(DISABLE);
	

	ReloadWatchdogCounter();

	//reset the period counter for all the time taken during inititalization
	SystickCount_us = 0;

	UsbInitDelay = SystickCount_us; //inititalize the usb delay countdown


	LedBlink(RED,30);
	LedBlink(ORANGE,30);
	LedBlink(GREEN,30);
	LedBlink(BLUE2,30);
	
	
	LedBlink(RED2,30);
	LedBlink(ORANGE2,30);
	LedBlink(GREEN2,30);
	LedBlink(BLUE,30);
	
	sprintf(MessageReportStringBuff, "FW Build Date %02d-%02d-%04d,Time %02d:%02d:%02d\n", BUILD_DAY ,BUILD_MONTH, BUILD_YEAR, BUILD_HOUR, BUILD_MIN, BUILD_SEC);
	SendControlMessageReportIN(MessageID, 0 ,MessageReportStringBuff);
	
	//clear this as the system has finined initita;lizing so all timed calles started properly
	SystickCount_us = 0;
	//SystickCount_ms = 0 ;
	
	//IRArray_Config();
	
	//InitTestCluster();
	

		__enable_irq();                             // Enable all interrupts 
	InitializationComplete = TRUE;
	//#################################################################################################################################################################################################
	//#################################################################################################################################################################################################
	//#################################################################################################################################################################################################
	//#################################################################################################################################################################################################
	//#################################################################################################################################################################################################
	//#################################################################################################################################################################################################
	//#################################################################################################################################################################################################
	//#################################################################################################################################################################################################

while (1)
{
	ReloadWatchdogCounter();	
	
	
		
	
if ((USB_INITIALIZED == FALSE) && ((SystickCount_us - UsbInitDelay) >= 1000000))//do this only after abotu 2 seconds of main loop iteration
		{
			USB_Config(); //configure the usb peripheral
			USB_INITIALIZED = TRUE;
		}

		if (USB_Packet_Recieved == TRUE)
		{
			USB_Packet_Handler();
			USB_Packet_Recieved = FALSE;
		}	
		
if (EnterBootloader)
		{
			//do any house keeping before bootloader
			EnterBootloader = FALSE;

			BootLoaderInit();   //enter the boot loader mode
		}	




			if (SystickCount_us >= LastLoopPeriod) //check for overflow of loop counter enter only when
			{
				LoopLatency = SystickCount_us - LastLoopPeriod; //get the loop latency in uSeconds
			}
			LastLoopPeriod = SystickCount_us; //save the current counter

			
	if(bDeviceState == CONFIGURED) 
	{
		if ((STATUS_TRANSMIT == TRUE )&& ((GlobalDelay.SendStatusReport.CurrentCount = (SystickCount_us - GlobalDelay.SendStatusReport.LastPeriodCount)) >= 500000))
		{
		SendStatusReport();
			
		GlobalDelay.SendStatusReport .LastPeriodCount = SystickCount_us ;
		}
		
		
	}	
	//detect USB state change
		if (bDeviceState != CurrentUsbState)
		{
			//set led to indicate status	
			if (bDeviceState == CONFIGURED)
			{
				LedState(GREEN, ON );
			}
			else
			{
				LedState(GREEN, OFF );
			}
			CurrentUsbState = bDeviceState;
		}
//#################################################################################################################################################################################################
//#################################################################################################################################################################################################
//#################################################################################################################################################################################################
//#################################################################################################################################################################################################

	}   ////END OF MAIN PROGRAM LOOP////////////////////////////////////////////////////////////////////////////
}  ///END OF MAIN PROGRAM BLOCK//////////////////////////////////////////////////////////////////////



uint32_t GetAsciiControlsList(char * String,ControlType * Array)
{
	
return 0;	
}

uint32_t GetAsciiDeviceList(char * String,uint16_t * Array)
{
	
return 0;	
}

void USB_Config(void)
{
	uint8_t MessageID = 98;
	
//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
		
	Set_System();
	Set_USBClock();
	USB_Interrupts_Config();

	USB_Init();

	//while (bDeviceState != CONFIGURED) // wait for device to be plugged into host
	//{}
	//no dont wait for this implementation
}

//this marks the current dma point se we can detect if ned datra is received by dma
uint32_t  USART_DMA_MarkMessagePointer(USART_ConfigType * UsartObject)
{
UsartObject->UsartReceiveObject.LastDmaCounter = RX_OBJ_BUFF_SIZE - DMA_GetCurrDataCounter(UsartObject->DMA_Channel) ;
return UsartObject->UsartReceiveObject.LastDmaCounter;
}

uint32_t  USART_DMA_GetCurrentPointer(USART_ConfigType * UsartObject)
{
return RX_OBJ_BUFF_SIZE - DMA_GetCurrDataCounter(UsartObject->DMA_Channel) ;
}




void SendStatusReport(void)
{
uint8_t UsbCRC;
if(bDeviceState == CONFIGURED) //transmit via usb if cable is plugged in
	{
	Transmit_Buffer[0] = IN_OperationStatus ;   //add the USB report ID
		
	if(	WaitPrevXferComplete() == ERROR)//wait for previous transfer to be complete
	{
		return;
	}
	/* Reset the control token to inform upper layer that a transfer is ongoing */
	PrevXferComplete = 0;
	//fill in the data here#######################################################
	
	
	
	
	//compute the crc of the transmit buffer
	 UsbCRC = CRC_Cal8Bits(Transmit_Buffer,PROFILE_REPORT_SIZE );//	PROFILE_REPORT_SIZE
	//append the crc to the last byte [63]	
Transmit_Buffer[PROFILE_REPORT_SIZE] = UsbCRC ;
		USB_SIL_Write(EP1_IN, Transmit_Buffer , 64); //the buffer count variable must be exactly equal to the report count +1(one extra byte for the report ID) on the report descriptor for this report
				
	//		/* Enable endpoint for transmission */
	SetEPTxValid(ENDP1);

	}
	
}

void SendConfigurationReport(void)
{
uint8_t UsbCRC;
if(bDeviceState == CONFIGURED) //transmit via usb if cable is plugged in
	{
	Transmit_Buffer[0] = IN_HardwareConfiguration ;   //add the USB report ID
		
	if(	WaitPrevXferComplete() == ERROR)//wait for previous transfer to be complete
	{
		return;
	}
	/* Reset the control token to inform upper layer that a transfer is ongoing */
	PrevXferComplete = 0;
	//fill in the data here#######################################################
	
	
	
	//compute the crc of the transmit buffer
	 UsbCRC = CRC_Cal8Bits(Transmit_Buffer,PROFILE_REPORT_SIZE );//	PROFILE_REPORT_SIZE
	//append the crc to the last byte [63]	
Transmit_Buffer[PROFILE_REPORT_SIZE] = UsbCRC ;
		USB_SIL_Write(EP1_IN, Transmit_Buffer , 64); //the buffer count variable must be exactly equal to the report count +1(one extra byte for the report ID) on the report descriptor for this report
				
	//		/* Enable endpoint for transmission */
	SetEPTxValid(ENDP1);

	}
	
}
int StringReplaceChar(char *str, char orig, char rep,uint32_t strlen) 
{
	int cnt = 0;
	int n =0;
	for(n=0;(n < strlen) && (str[n]!= 0);n++)
	{
		if(str[n] == orig)
		{
			str[n] = rep;
			cnt++;
		}
	}
    return cnt; //return the number of occurences replaced
}

int32_t String_FindCharIndex(char * String, uint32_t StartIndex, uint32_t EndIndex, char FindChar)
{
uint32_t k = 0;
	if(StartIndex > EndIndex )
	{
		return -1;
	}
	
	for(k =0 ;k < EndIndex - StartIndex ;k++)
	{
		if (String[StartIndex + k] 	== FindChar)
		{
			return k;
		}
		else if(String[StartIndex + k] == 0)
		{
			return -1;	
		}
	}
	return -1;
}






uint32_t USART_DMA_ScanBytes(USART_ConfigType * USART_Config  )
{
	uint32_t MessageCount =  0;
	uint32_t FromDmaCounter = USART_Config->UsartReceiveObject.LastDmaCounter;
	uint32_t CurrentDmaCounter = RX_OBJ_BUFF_SIZE - DMA_GetCurrDataCounter(USART_Config->DMA_Channel) ;
	
	USART_Config->UsartReceiveObject.Message[USART_Config->UsartReceiveObject.StoreMessagePointer].MsgStart  = FromDmaCounter;
	//loop through the bytes saved by dma
	while(FromDmaCounter != CurrentDmaCounter)
	{	
			if(++FromDmaCounter >= RX_OBJ_BUFF_SIZE)
			{
				FromDmaCounter = 0;
			}
			//look for terminating 0x0D and 0x0A giving consideration to the bufer cycling
		if(( (FromDmaCounter != 0)	&& (USART_Config->UsartReceiveObject.RxBuffer[FromDmaCounter] == 0x0A) && (USART_Config->UsartReceiveObject.RxBuffer[FromDmaCounter - 1] == 0x0D) ) ||
			((FromDmaCounter == 0)	&& (USART_Config->UsartReceiveObject.RxBuffer[FromDmaCounter] == 0x0A) && (USART_Config->UsartReceiveObject.RxBuffer[RX_OBJ_BUFF_SIZE - 1] == 0x0D) ))
		{
			if((FromDmaCounter - USART_Config->UsartReceiveObject.LastDmaCounter) > 2 ) //check this make sure there is something between the \r\n and \r\n
			{
				USART_Config->UsartReceiveObject.Message[USART_Config->UsartReceiveObject.StoreMessagePointer].MsgEnd = FromDmaCounter;
				USART_Config->UsartReceiveObject.Message[USART_Config->UsartReceiveObject.StoreMessagePointer].NewMessage = TRUE;
				//determine message cycling
				if(USART_Config->UsartReceiveObject.Message[USART_Config->UsartReceiveObject.StoreMessagePointer].MsgEnd < 
					USART_Config->UsartReceiveObject.Message[USART_Config->UsartReceiveObject.StoreMessagePointer].MsgStart)
				{
					USART_Config->UsartReceiveObject.Message[USART_Config->UsartReceiveObject.StoreMessagePointer].BufferCycle = TRUE;
				}
				else
				{
					USART_Config->UsartReceiveObject.Message[USART_Config->UsartReceiveObject.StoreMessagePointer].BufferCycle = FALSE;
				}
				
				//increment the stored message pointer
				if(++USART_Config->UsartReceiveObject.StoreMessagePointer >= RX_OBJ_MAX_MESSAGES)
				{
				USART_Config->UsartReceiveObject.StoreMessagePointer = 0;
				}
				MessageCount++;
				
				//mark the start of the next message
				USART_Config->UsartReceiveObject.Message[USART_Config->UsartReceiveObject.StoreMessagePointer].MsgStart  = FromDmaCounter +1;
			}
		}
		//update the current dma pointer in case more have been added whilst on here
		CurrentDmaCounter = RX_OBJ_BUFF_SIZE - DMA_GetCurrDataCounter(USART_Config->DMA_Channel);
	}
	//save the pointer to pick off next time
	USART_Config->UsartReceiveObject.LastDmaCounter = CurrentDmaCounter;

	return MessageCount;
}

uint8_t  USART_ReadBuffer(USART_ConfigType * USARTObject)
{
	uint8_t data = 0;
	uint32_t CurrentDmaCounter = RX_OBJ_BUFF_SIZE - DMA_GetCurrDataCounter(USARTObject->DMA_Channel) ;

	UNIMPLEMENTED: //USART_ReadBuffer
	
	
	//if the dma is used then lets read the next available byte and incrememnt the dma bytes tracker
	if(USARTObject->USE_DMA == TRUE)
	{
	if(USARTObject->UsartReceiveObject.LastDmaCounter != USART_DMA_GetCurrentPointer(USARTObject))
		{
		//read the dma buffer and return then increment the last dma counter
		data =	USARTObject->UsartReceiveObject.RxBuffer[USARTObject->UsartReceiveObject.LastDmaCounter];
		//increment the last dma counter
			//save the pointer to pick off next time
		USARTObject->UsartReceiveObject.LastDmaCounter++;
			//check if we are at the end of the buffer
			if (USARTObject->UsartReceiveObject.LastDmaCounter >= RX_OBJ_BUFF_SIZE )
			{
				//reset the last dma counter 
				USARTObject->UsartReceiveObject.LastDmaCounter = 0;
			}
		}
	}
	else
	{
	//read serial buffer
	 data = USART_ReceiveData(USARTObject->USARTn);	
	}	
//if the dms isnt used then lets just read one byte from the usart hardware receive buffer 
return data;
}

//check for any received usart bytes
bool  USART_BytesAvailable(USART_ConfigType * USARTObject)
{
//	uint8_t data;
	UNIMPLEMENTED1: //USART_ReadBuffer
	//if the usart is configured to use DMA then compare the dma conters with the last time to know if any new byte is available
	if(USARTObject->USE_DMA == TRUE)
	{
	if(USARTObject->UsartReceiveObject.LastDmaCounter != USART_DMA_GetCurrentPointer(USARTObject))
		{
		return TRUE;
		}
	}
	else
	{


	}	
	//if dma is not used then lets read the appropriate usart flags to see if bytes are available on the fifo
	return FALSE;
}

ErrorStatus ConfigureIOPin(GPIOParamStruct * Pindata, bool ConfigInterrupt)
{
		GPIO_InitTypeDef GPIO_InitStructure; //create the structure used for inititalizing the gpio
	EXTI_InitTypeDef EXTI_InitStructure;
	NVIC_InitTypeDef NVIC_InitStructure;
	
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	
	if (Pindata->Mode  == OUTPUT )
	{
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT; //set the pin function to output for the following pins
	GPIO_InitStructure.GPIO_OType = GPIO_OType_OD;//changed this to open drain as puch pull killed txselect board when processor froze. than made it pull up
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;	
	}
	else if(Pindata->Mode == INPUT )
	{
		GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN;
		
	}
 
  GPIO_InitStructure.GPIO_PuPd  = Pindata->IO_Pull;//GPIO_PuPd_DOWN;
	GPIO_InitStructure.GPIO_Pin =  Pindata->IO_Pin   ;	// Setup vdd2 enable pin
	
	RCC_AHBPeriphClockCmd(Pindata->IO_Rcc,ENABLE); //enable the ahb peripheral clock for this pin
 	GPIO_Init( Pindata->IO_Port, &GPIO_InitStructure );    //ini
	
	//configure interrupts
	if(Pindata->Mode == INPUT && ConfigInterrupt == TRUE)
	{
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_SYSCFG, ENABLE); //enable sysconfig before using the interrupt as we have to enable the source via sysconfig registers

	SYSCFG_EXTILineConfig(Pindata->EXTI_PortSource ,Pindata->EXTI_PinSource );
	EXTI_InitStructure.EXTI_Mode = EXTI_Mode_Interrupt;
	EXTI_InitStructure.EXTI_Line = Pindata->EXTI_Line ; // Bus_IdentEn_EXTI_LINE;
		if(Pindata->TriggerType == 0) //if this was not specified
		{
			Pindata->TriggerType =EXTI_Trigger_Rising_Falling ; //default to risingfalling
		}
	EXTI_InitStructure.EXTI_Trigger = Pindata->TriggerType; //detect both state change, so we can set and clear the ident code
	EXTI_InitStructure.EXTI_LineCmd = ENABLE;
	EXTI_Init(&EXTI_InitStructure);
		
	/* Enable the EXTI3 Interrupt */
	NVIC_InitStructure.NVIC_IRQChannel = Pindata->EXTI_IRQChannel  ;//
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = (Pindata->EXTI_Priority & 0xFC) ; //higher 2 bits of the lower nibble of the byte gives premption priority
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = (Pindata->EXTI_SubPriority & 0xFC); //lower 2 bits of the lower nibble of the byte gives the sub priority
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
	NVIC_Init(&NVIC_InitStructure);

	}
	
	Pindata->Initialized = TRUE;
	return SUCCESS;
}


void USART_Receive_Data(USART_ConfigType * ReceiveObject)
{
	uint32_t LastMessage;
//check if the buffer ind3xer is at the top
			if( ++ReceiveObject->UsartReceiveObject.ReceiveCounter >= RX_OBJ_BUFF_SIZE)
			{
				ReceiveObject->UsartReceiveObject.ReceiveCounter = 0 ;
			}
			
			ReceiveObject->UsartReceiveObject.RxBuffer[ReceiveObject->UsartReceiveObject.ReceiveCounter] = USART_ReceiveData(ReceiveObject->USARTn) ;
			
			if(( ReceiveObject->UsartReceiveObject.RxBuffer[ReceiveObject->UsartReceiveObject.ReceiveCounter -1] == 0x0D) && ( ReceiveObject->UsartReceiveObject.RxBuffer[ReceiveObject->UsartReceiveObject.ReceiveCounter] == 0x0A))
			{
				//new line lreceilved
				if (ReceiveObject->UsartReceiveObject.StoreMessagePointer == 0 )
				{
					LastMessage = RX_OBJ_MAX_MESSAGES - 1 ;
				}
				else
				{
					LastMessage = ReceiveObject->UsartReceiveObject.StoreMessagePointer - 1 ;
				}
				
				if(( ReceiveObject->UsartReceiveObject.ReceiveCounter - ReceiveObject->UsartReceiveObject.Message[LastMessage].MsgEnd  ) > 2) //make sure somethig is in between
				{
					ReceiveObject->UsartReceiveObject.Message[ReceiveObject->UsartReceiveObject.StoreMessagePointer].MsgEnd = ReceiveObject->UsartReceiveObject.ReceiveCounter ;
					ReceiveObject->UsartReceiveObject.Message[ReceiveObject->UsartReceiveObject.StoreMessagePointer].NewMessage = TRUE ;
					if(++ReceiveObject->UsartReceiveObject.StoreMessagePointer >= RX_OBJ_MAX_MESSAGES )
					{
						ReceiveObject->UsartReceiveObject.StoreMessagePointer = 0 ;
					}
					ReceiveObject->UsartReceiveObject.Message[ReceiveObject->UsartReceiveObject.StoreMessagePointer].MsgStart = ReceiveObject->UsartReceiveObject.ReceiveCounter + 1  ;
				}
			}				
			//	ESP8266_RxMesssageTimeout = SystickCount_us ;
	return;
}


/*******************************************************************************
* Function Name  : USART_Configuration
* Description    : Configures the USART peripheral
* Input          : None
* Output         : None
* Return         : None
*******************************************************************************/
ErrorStatus USART_Configuration(USART_ConfigType * USART_Config)
{
  //uint32_t PeriphClock;

  GPIO_InitTypeDef  GPIO_InitStructure;
	USART_InitTypeDef 	USART_InitStructure;
   NVIC_InitTypeDef  NVIC_InitStructure;
	DMA_InitTypeDef   DMA_InitStructure;
	DMA_Channel_TypeDef * DMA_Channel;
	uint32_t DMA_IRQn;
	
uint32_t  Usart_Port_Peripheral_RCC;
uint32_t Usart_Peripheral_RCC ;
GPIO_TypeDef * Usart_Port;
uint16_t Usart_txPin;
uint8_t Usart_txPinSource;
uint16_t Usart_rxPin;
uint8_t Usart_rxPinSource;
uint8_t Usart_PinAF	;   
uint8_t USARTn_IRQ_LINE ;
	
	
	if((USART_Config->ConfigRX == FALSE) && (USART_Config->ConfigTX == FALSE))
	{
		//at least one must be true
		return ERROR;
	}
 /* --------------------------- System Clocks Configuration -----------------*/
  
	/* USARTx clock enable */
	if (USART_Config->USARTn == USART1)
	{
  Usart_Port_Peripheral_RCC = 	RCC_AHBPeriph_GPIOC;
	Usart_Peripheral_RCC =				RCC_APB2Periph_USART1;
	Usart_Port =									GPIOC;
	Usart_txPin	=									GPIO_Pin_4;
	Usart_txPinSource	=						GPIO_PinSource4;
	Usart_rxPin	=									GPIO_Pin_5;
	Usart_rxPinSource	=						GPIO_PinSource5;
	Usart_PinAF	 =								GPIO_AF_7   ; 
	USARTn_IRQ_LINE  = 						USART1_IRQn;

	RCC_APB2PeriphClockCmd(Usart_Peripheral_RCC , ENABLE); 
		
	}
	else if (USART_Config->USARTn == USART2)
	{
	Usart_Port_Peripheral_RCC = 	RCC_AHBPeriph_GPIOA;
	Usart_Peripheral_RCC =				RCC_APB1Periph_USART2;
	Usart_Port =									GPIOA;
	Usart_txPin	=									GPIO_Pin_2;
	Usart_txPinSource	=						GPIO_PinSource2;
	Usart_rxPin	=									GPIO_Pin_3;
	Usart_rxPinSource	=						GPIO_PinSource3;
	Usart_PinAF	 =								GPIO_AF_7   ; 
	USARTn_IRQ_LINE  = 						USART2_IRQn;
		
	RCC_APB1PeriphClockCmd(Usart_Peripheral_RCC , ENABLE); 
	}
	else if (USART_Config->USARTn == USART3)
	{
	Usart_Port_Peripheral_RCC = 	RCC_AHBPeriph_GPIOB;
	Usart_Peripheral_RCC =				RCC_APB1Periph_USART3;
	Usart_Port =									GPIOB;
	Usart_txPin	=									GPIO_Pin_10;
	Usart_txPinSource	=						GPIO_PinSource10;
	Usart_rxPin	=									GPIO_Pin_11;
	Usart_rxPinSource	=						GPIO_PinSource11;
	Usart_PinAF	 =								GPIO_AF_7   ; 
	USARTn_IRQ_LINE  = 						USART3_IRQn;
		
		RCC_APB1PeriphClockCmd(Usart_Peripheral_RCC , ENABLE); 
	}
	else
	{
		//#error "Wrong uart specified" 
		return ERROR ;
	}

  /* GPIOx clock enable */
  RCC_AHBPeriphClockCmd(Usart_Port_Peripheral_RCC, ENABLE);  //specify the gpio that the serial port selected is located

  /*-------------------------- GPIO Configuration ----------------------------*/

  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_OD; //GPIO_PuPd_NOPULL  //configure tx pin as open drain instead of push-pull
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP; //see ref. manual section 26.5.12
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  
if (USART_Config->ConfigTX == TRUE)
{
	//configure the TX pin
	  GPIO_InitStructure.GPIO_Pin = Usart_txPin;  //| GPIO_Pin_3; //pin A9 is for uart1 tx
	GPIO_Init(Usart_Port, &GPIO_InitStructure);
	  /* Connect USART pins to AF */
  GPIO_PinAFConfig(Usart_Port, Usart_txPinSource , Usart_PinAF); // configure alternate function for PA9//AF7 is for the uart, see ref. manual
}
else
{ //clear these as they wont be needed
USART_Config->TC_INT_EN = FALSE ;
USART_Config->TXE_INT_EN = FALSE;
}
	

if(USART_Config->ConfigRX == TRUE)
{
	//configure the RX pin
	GPIO_InitStructure.GPIO_Pin = Usart_rxPin;  //| GPIO_Pin_3; //pin A9 is for uart1 tx
	GPIO_Init(Usart_Port, &GPIO_InitStructure);
	 /* Connect USART pins to AF */	
  GPIO_PinAFConfig(Usart_Port, Usart_rxPinSource , Usart_PinAF); // no need for RX
}
else
{
USART_Config->RXNE_INT_EN = FALSE;
}

//if the dma is enabled and the reecive interupti is enebled then dma will take priority and we have to diable the receive interrup
//to avoid overflow whilst dma is receiveing the data
if((USART_Config->USE_DMA == TRUE) &&  (USART_Config->RXNE_INT_EN == TRUE))
{
	USART_Config->RXNE_INT_EN = FALSE ;
}

	
	USART_InitStructure.USART_BaudRate = USART_Config->BaudRate;
	 
  USART_InitStructure.USART_WordLength = USART_WordLength_8b;
  USART_InitStructure.USART_StopBits = USART_StopBits_1;
  USART_InitStructure.USART_Parity = USART_Parity_No;
  USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;

  USART_InitStructure.USART_Mode = (USART_Config->ConfigRX ? USART_Mode_Rx : 0 ) | (USART_Config->ConfigTX ? USART_Mode_Tx : 0 ); //  
 
  USART_Init(USART_Config->USARTn, &USART_InitStructure);
 
USART_OverrunDetectionConfig(USART_Config->USARTn,USART_OVRDetection_Disable);

  USART_Cmd(USART_Config->USARTn, ENABLE);


	if(USART_Config->TC_INT_EN == TRUE)
	{
		//enable transmit complete interrupt
	USART_ITConfig(USART_Config->USARTn, USART_IT_TC, ENABLE) ;
	}

	if(USART_Config->TXE_INT_EN == TRUE) 
	{
	//enable transmit register empty interrupt
	 USART_ITConfig(USART_Config->USARTn, USART_IT_TXE, ENABLE) ;
	}

	if(USART_Config->RXNE_INT_EN == TRUE)
	{
		 //enable receive data registert not empty interrupt
	 USART_ITConfig(USART_Config->USARTn, USART_IT_RXNE, ENABLE) ;
	}

if( USART_Config->TXE_INT_EN == TRUE || USART_Config->TC_INT_EN == TRUE || USART_Config->RXNE_INT_EN == TRUE)
{
	NVIC_InitStructure.NVIC_IRQChannel = USARTn_IRQ_LINE;
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 1;
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 2;
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
	NVIC_Init(&NVIC_InitStructure);
}

if(USART_Config->USE_DMA == TRUE)
{
	
	if(USART_Config->USARTn == USART1 )
	{	
		DMA_Channel = DMA1_Channel5; //use channel 5 for usart1 rx
		DMA_IRQn =  DMA1_Channel5_IRQn ;
	}
	else if (USART_Config->USARTn == USART2 )
	{
	 DMA_Channel = DMA1_Channel6 ;
		DMA_IRQn =  DMA1_Channel6_IRQn ;
	}
	else if (USART_Config->USARTn == USART3 ) 
	{
		DMA_Channel = DMA1_Channel3; 
		DMA_IRQn =  DMA1_Channel3_IRQn ;
	}
	//sore the dma channel assigne d to the usart being configured
	USART_Config->DMA_Channel = DMA_Channel ;
	
	//if(USART_Config->USARTn == USART1 ) //use channel
	  
	// Enable DMA2 clock -------------------------------------------------------
    RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1, ENABLE);
	
		DMA_DeInit(DMA_Channel);
    DMA_InitStructure.DMA_PeripheralBaseAddr = (uint32_t)&(USART_Config->USARTn->RDR);
    DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t )USART_Config->UsartReceiveObject.RxBuffer;
    DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralSRC ; //DMA_DIR_PeripheralDST;
    DMA_InitStructure.DMA_BufferSize = sizeof(USART_Config->UsartReceiveObject.RxBuffer); //    DMA_BUFFER_SIZE;
    DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;
    DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable ;//DMA_MemoryInc_Enable;
    DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte;
    DMA_InitStructure.DMA_MemoryDataSize = DMA_MemoryDataSize_Byte;
    DMA_InitStructure.DMA_Mode = DMA_Mode_Circular;
    DMA_InitStructure.DMA_Priority = DMA_Priority_High;
    DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;
		
	 DMA_Init(DMA_Channel, &DMA_InitStructure); 
	
		//setup dma interrupt
		NVIC_InitStructure.NVIC_IRQChannel = DMA_IRQn; // This could be different in your implementation
		NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 1;
		NVIC_InitStructure.NVIC_IRQChannelSubPriority = 1;
		NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
//		NVIC_Init(&NVIC_InitStructure);

	 // Enable DMA1 Channel Transfer Complete interrupt
//	 DMA_ITConfig(DMA_Channel, DMA_IT_TC, ENABLE);
	 
	 //finally enable the DMA for the usart
	  USART_DMACmd(USART_Config->USARTn, USART_DMAReq_Rx, ENABLE);
		DMA_Cmd(DMA_Channel, ENABLE);
 
	 
}

	
	
USART_Config->Configured  = TRUE;

return SUCCESS;
/////////////////////////////////////////////////////////////////////////////////////////
}


int32_t SearchStringForPattern(char * String , char * Pattern , uint32_t StringLength ) //return index of word in the csv string found or -1 if not found
{
	char	TempString[100] ;
	uint8_t MessageID = 00;
	int i,j,k,WordCount;
	//uint32_t Ind =0;
	#define MaxWords 13
	//check how manny words in here and starore there index points 
	uint8_t WordsIndex[MaxWords];
	WordCount= 0; //used for indexing the workds index
	//assuming the first one will be at index 0
	WordsIndex[WordCount++] = 0;
	for(k=0;Pattern[k] != 0 && WordCount < MaxWords ;k++) //thi assumes the pattern is null terminated
	{
		//serch for the separator
		if(Pattern[k] == ',')
		{
			WordsIndex[WordCount++] = k+1 ;
		}
	}
	
	
	for(i =0 ; i < StringLength ; i++)
	{	
		for(j = 0;j<WordCount;j++) //loop through al the words in the pattern array separated by comms
		{	
			//if we find the first character
			if(String[i] == Pattern[WordsIndex[j]])
			{
				//match the remaining characters to the pattern
				for (k=0; (Pattern[WordsIndex[j]+k] != 0) && (i+k < StringLength)  ; k++) //do loop while i is not zero and is less than count
				{
					if (*(&String[i]+k) == *(&Pattern[WordsIndex[j]] + k)) 
					{
					continue; //continue loop if the same
					}
					else
					{
						//break out if the pattern match and look for the next first character match
						break;
					//return FALSE ; //return false if not the same
					}
				}
				//lets see the reason why we did break out of the loop
				if ((Pattern[WordsIndex[j]+k] == 0) || (Pattern[WordsIndex[j] + k] == ',') || (i+k >= StringLength))
				{
					//there must have been a match found terminated by the bnull chracter
				sprintf(MessageReportStringBuff, "Pattern match-\"%s\" Found\r\n", &Pattern[WordsIndex[j]] );
				SendControlMessageReportIN(MessageID, 0 ,MessageReportStringBuff);
				return j; //it must have been found return the index if the word found
				}
			}
		}
	}
//	

	//null terminate the source string
//lets not use more than we have in the vbuffer
	if(StringLength > sizeof(TempString))
	{
		StringLength = sizeof(TempString) ; 
	}
	CopyString( String,  TempString, StringLength);
	//null terminate it
	TempString[StringLength] = 0 ;

	
sprintf((char *)&MessageReportStringBuff,"Specified word Patterns NOT found ! ! ! in %s \r\n",TempString);
//sprintf((char *)&MessageReportStringBuff,"Specified String Pattern NOT found ! ! ! \r\n");
			
USART_Send_String ( &DEBUG_USART_Config ,(char *)MessageReportStringBuff );		

	
	return -1; //not found so rreturn 0
}



void ConfigDebugUsart(void)
{
	DEBUG_USART_Config.BaudRate= 115200; 
	DEBUG_USART_Config.ConfigRX= TRUE;
	DEBUG_USART_Config.ConfigTX = TRUE;
	DEBUG_USART_Config.Configured = FALSE;
	DEBUG_USART_Config.USARTn = DEBUG_USART ;
	//	DEBUG_USART_Config.RXNE_INT_EN = TRUE; //no need for recieve interrupt as we will be using DMA to retreive the bytes
	DEBUG_USART_Config.USE_DMA = TRUE; //with dma enabled receive interrupt is disabled
//	DEBUG_USART_Config.DMA_BUFFER = (uint32_t )&DEBUG_UsartReceiveObject.RxBuffer;
//	DEBUG_USART_Config.DMA_BUFFER_SIZE = sizeof(DEBUG_UsartReceiveObject.RxBuffer);

	//specifuy the usart type on the buffer object
	//DEBUG_UsartReceiveObject.USARTx = DEBUG_USART;
	
USART_Configuration(&DEBUG_USART_Config);
//USART_Configuration(DEBUG_USART,115200,FALSE,TRUE,FALSE,FALSE,FALSE);	
}



ErrorStatus SoundTone(uint32_t DurationMs, uint32_t  FreqHz)
{
	//calculate the period
	float PeriodUs =  (( 1 / (float)FreqHz) * 1000000);
	float HalfPeriodUs = PeriodUs/2;
	
	float Time =  (DurationMs * 1000) / (PeriodUs) ;
	uint32_t i ;
	
	for(i=0;i < Time;i++)
	{
//		for (k=0;k < PeriodsPerMs; k++)
//		{
			//set high
			GPIO_SetBits(Buzzer_Port,Buzzer_Pin);
			//delay period
				 ReloadWatchdogCounter();
			Delay_us(HalfPeriodUs);
			//set low
			GPIO_ResetBits(Buzzer_Port,Buzzer_Pin);
			//delay period
				 ReloadWatchdogCounter();
			Delay_us(HalfPeriodUs);
//		}
	}
	return SUCCESS;
}

//get the current millissecond count
uint32_t millis(void)
{
return SystickCount_us/1000; //return the current milliseconds count
}

int32_t SearchMessageForResponse(USART_ReceiveObjectType * ReceiveObject, uint32_t MesgIndex, char * Pattern ) //return the index location of the pattern found from the csv of patterns return -1 if not found
{
	uint32_t k,count,retval;
	uint32_t msgsize = 0;
	char  TempMessagBuff[RX_OBJ_BUFF_SIZE/2];
	//first check if the message overflows the array
	if((ReceiveObject->Message[MesgIndex].MsgEnd <  ReceiveObject->Message[MesgIndex].MsgStart ) && (ReceiveObject->Message[MesgIndex].BufferCycle == TRUE))
	{	
	//first know the message length
		msgsize = (RX_OBJ_BUFF_SIZE - ReceiveObject->Message[MesgIndex].MsgStart) + ReceiveObject->Message[MesgIndex].MsgEnd ;
		
		//if the message is too long lets sinmply discard it
		if(msgsize > sizeof(TempMessagBuff))
		{
			ReceiveObject->Message[MesgIndex].NewMessage = FALSE;
			return -1; //return less than 0 if nothing found
			
		}

	
		//allocate buffer using mallock
		//TempMessagBuff = malloc(msgsize + 1);		//TempMessagBuff = calloc(msgsize + 1, )
		//copy the first part to buffer
		for(k=0;k < ( RX_OBJ_BUFF_SIZE -  ReceiveObject->Message[MesgIndex].MsgStart ) &&(k < msgsize) ; k++)
		{
			TempMessagBuff[k] = ReceiveObject->RxBuffer[ReceiveObject->Message[MesgIndex].MsgStart + k];
		}
		//get the current pointer from k
		count = k ;
		//copy the remainder from the buffer start
		for(k=0;k <=ReceiveObject->Message[MesgIndex].MsgEnd;k++)
		{
			TempMessagBuff[count++] = ReceiveObject->RxBuffer[k];
		}
		//move the message and position it from start so that any calling function will have a properlly aligned message
		//we will move the message backwards i the buffer as we dont want to mess with subsequent messages in the buffer
		CopyString(TempMessagBuff,&ReceiveObject->RxBuffer[RX_OBJ_BUFF_SIZE - msgsize-1],msgsize);
		//update the mesage stat and end pointers
		ReceiveObject->Message[MesgIndex].MsgStart = (RX_OBJ_BUFF_SIZE - msgsize-1);
		ReceiveObject->Message[MesgIndex].MsgEnd = RX_OBJ_BUFF_SIZE - 1 ;
		
	//retval = SearchStringForPattern(TempMessagBuff,Pattern,count-1) ;	
		//free the malloc buffer
	//free(TempMessagBuff);
	//return retval	;
		
	}

	retval = 	SearchStringForPattern(&ReceiveObject->RxBuffer[ReceiveObject->Message[MesgIndex].MsgStart] ,Pattern ,ReceiveObject->Message[MesgIndex].MsgEnd - ReceiveObject->Message[MesgIndex].MsgStart) ;	
	ReceiveObject->Message[MesgIndex].NewMessage = FALSE;
	return retval;

}




ErrorStatus Send_TCP_Request(char * IpAddress,char * GetUrl, uint32_t UrlCount)
{
	#ifdef _ESP8266_H
//	uint32_t StringCount;
//char GetRequestBuff[200];
//open the tcp connection	
	if (AT_CIPSTART("TCP",IpAddress,80) == ESP_OK ) //make sure ip address is checked for null termination
	{
		//lets clear the wifi no link count if we connect successful
		NO_WIFI_CNT = 0;
		NO_INTERNET_CNT = 0;
		//load message into urt buffer
		//	StringCount = sprintf((char *)GetRequestBuff,"%s\r\n\r\n",);
		//	StringCount +=	sprintf((char *)&GetRequestBuff[StringCount],"%s\r\n\r\n",GetUrl);  //first address on stack
		//delay after cipstart
		//check if this is neccessary
		//not needed as we may have waited for response   Delay_ms(500);
		if (AT_CIPSEND(GetUrl,UrlCount) == SUCCESS ) // total of GetUrlCount + 5 bytes for "GET /"
		{
		//close the connection
			//if date is not set then leave the connection so we can get the server response data whcih contains the date information
			if(DATE_TIME_SET == TRUE)
			{
			ESP8266_Send("AT+CIPCLOSE\r\n") ;
			}
		return SUCCESS;
		}
	}
//	else
//	{
//		return ERROR;
//	}
	#endif  //_ESP8266_H
return ERROR;

}

ErrorStatus Send_SSL_Request(char * IpAddress,char * GetUrl, uint32_t UrlCount)
{
	#ifdef _ESP8266_H

	if (AT_CIPSSLSIZE(4096) != ESP_OK ) //it was tested and found that pushover needed 4096 to work
	{
		return ERROR;
	}
	if (AT_CIPSTART("SSL",IpAddress,443) == ESP_OK ) //make sure ip address is checked for null termination
	{
		//lets clear the wifi no link count if we connect successful
		NO_WIFI_CNT = 0;
		NO_INTERNET_CNT = 0;
	
		//check if this is neccessary
		//not needed as we may have waited for response   Delay_ms(500);
		if (AT_CIPSEND(GetUrl,UrlCount) == SUCCESS ) // total of GetUrlCount + 5 bytes for "GET /"
		{
		//close the connection
			//if date is not set then leave the connection so we can get the server response data whcih contains the date information
			if(DATE_TIME_SET == TRUE)
			{
			ESP8266_Send("AT+CIPCLOSE\r\n") ;
			}
		return SUCCESS;
		}
	}
//	else
//	{
//		return ERROR;
//	}
	#endif  //_ESP8266_H
return ERROR;

}


ErrorStatus SendPushingBoxMessage(char * ApiKey, char * Message)
{
	#ifdef _ESP8266_H
	char PushingBoxUrl[200];
	uint32_t UrlCnt;
	
				//send this to the cloud using the api key available
				if(ApiKey[0] != 0)
				{
						// prepare GET string
					
						UrlCnt =	sprintf(PushingBoxUrl,"GET /pushingbox?devid=%s",ApiKey); 
						if(Message[0] != 0)
						{
							UrlCnt +=	sprintf(&PushingBoxUrl[UrlCnt],"%s",Message);
						}	
						UrlCnt +=	sprintf(&PushingBoxUrl[UrlCnt], " HTTP/1.1\r\n");  //construct http GET request
						UrlCnt +=  sprintf(&PushingBoxUrl[UrlCnt],"Host: api.pushingbox.com"); 
						
						UrlCnt +=  sprintf(&PushingBoxUrl[UrlCnt],"\r\n\r\n");  
						
						if (Send_TCP_Request("213.186.33.19",PushingBoxUrl, UrlCnt) == SUCCESS)
						{
							
							return SUCCESS;
						}
						else
						{
							return ERROR;
						}
				}
				else
				{
					// //no api key provided
				}	
				
				#endif
				
return ERROR;
}



ErrorStatus LogSensorCode(uint32_t SensorCode, uint32_t TimeOccurred)
{

return ERROR;		
}
		




void CRC_Config8Bits(uint8_t poly)
{

	/* Enable CRC AHB clock interface */
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_CRC, ENABLE);

	/* DeInit CRC peripheral */
	CRC_DeInit();
	/* Init the INIT register */
	CRC_SetInitRegister(0xFF);
	/* Select 8-bit polynomial size */
	CRC_PolynomialSizeSelect(CRC_PolSize_8);
	/* Set the polynomial coefficients */
	CRC_SetPolynomial(poly);
}



uint8_t CRC_Cal8Bits(uint8_t* data, uint32_t size)
{
	uint8_t MessageID = 8;
	uint8_t* dataEnd = data + size;
//remove this when message id is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	/* Reset CRC data register to avoid overlap when computing new data stream */
	CRC_ResetDR();

	//CRC_CalcCRC8bits(0xFF); //do initial start data

	while (data < dataEnd)
	{
		/* Write the input data in the CRC data register */
		CRC_CalcCRC8bits(*data++);

	}
	/* Return the CRC value */
	return (uint8_t)CRC_GetCRC();
}





void ReadADCValues(uint8_t index)  //this read the two multiplexed adc values and store in the array
{
	#define ADC_FLAG_WAIT_MAX 10000
	uint8_t MessageID = 11;
//	static uint16_t TempMean = 0;
	uint32_t ADC_FLAG_WAIT;
	
	//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	


	ADC_ClearFlag(ADC4, ADC_FLAG_EOC);

	/* Start ADC1 Conversion using Software trigger */
	ADC_StartConversion(ADC4);

	/* Wait until ADC Channel end of conversion */

	ADC_FLAG_WAIT = 0;
	while (ADC_GetFlagStatus(ADC4, ADC_FLAG_EOC) == RESET)
	{
		if (ADC_FLAG_WAIT++ >= ADC_FLAG_WAIT_MAX)
		{
			break;
		}
	}

	/* Read First ADC conversion result */ //this clears the EOC flag as well

	//AdcLastRead[0] = ADC_GetConversionValue(ADC4);
	
	ADC_FLAG_WAIT = 0;
	while (ADC_GetFlagStatus(ADC4, ADC_FLAG_EOC) == RESET)  //&& ((ADC_GetFlagStatus(ADC4,ADC_FLAG_EOS) == RESET)))
	{
		//wait for endo of conversion or if we werere to lat then end of sequence should get us out of here
		if (ADC_FLAG_WAIT++ >= ADC_FLAG_WAIT_MAX)
		{
			break;
		}
	}

	/* Read second ADC conversion result */ //this clears the EOC flag as well
//	AdcLastRead[1] = ADC_GetConversionValue(ADC4);

	
	ADC_StopConversion(ADC4);   //stop ADC conversion
								//if the power arrray has been filled then lets commpute th e mean

//	AdcReadLatency = SystickCount_us - LastAdcReadCount;
}


void UpdateErrorStatus(void)
{
	uint8_t MessageID = 10;
	//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	
	//compute the errorstatus struct into a 32 bit int
	ErrorTempVal = 0;   //clear this valu before start using	
	for (errorindex1 = 0; errorindex1 <= 31; errorindex1++)
	{//convert errpstatus struct address into 8 bit address, get the index location for that converted 8 bit array which equivalent to the struct member index, then convert the contents to 32 bit
		ErrorTempVal |= (uint32_t)(((uint8_t*)&ErrorStatusBits1)[errorindex1]) << errorindex1;
		//	ErrorTempVal <<= 1 ; //chift the bit status
	}


	if (ErrorTempVal != CurrentErrorStatusVal)
	{
		CurrentErrorStatusVal = ErrorTempVal;
		//update the NVRAM for error storage
		if (RTC_ReadBackupRegister(NVR_ErrorStatus) != CurrentErrorStatusVal)
		{
			//save back reg if not previously saved
			PWR_BackupAccessCmd(ENABLE);
			RTC_WriteBackupRegister(NVR_ErrorStatus, CurrentErrorStatusVal); //
			PWR_BackupAccessCmd(DISABLE);

		}
	}

}

ErrorStatus WaitPrevXferComplete(void)
{
	uint8_t MessageID = 15;
	//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	
	if (bDeviceState != CONFIGURED)  //if usb not connected then return error
	{
		return ERROR;
	}       //uint32_t decsave = Xfer_Decrement;
	if (USB_Timeout_Counter <= MAX_USB_TIMEOUT) //if the timeout is enoug then lets diconnect the usb cable
	{
		Xfer_Decrement = 1000; //load new us decrement
		while ((PrevXferComplete == 0) && (Xfer_Decrement))
		{
			Xfer_Decrement--;
			Delay_us(100);
			ReloadWatchdogCounter();
			//wait for either us decrement timout or previous transfer flag to be set
		}

		if (!Xfer_Decrement)
		{
			__asm{ nop}; //just a debugging trap for when we time out

			//usb transfer timeout
			USB_Timeout_Counter++;

			//we have to set this anyway so code that called this scan still go ahead and transmit anyway
			//this may not be soo good
			PrevXferComplete = 1;
		}
		else
		{
			USB_Timeout_Counter = 0;
		}
		return SUCCESS;
	}
	else
	{  //we have had enough failed transferes so lets stop successding it 
		return ERROR;
	}

}


void RTC_Config(void)
{
	
	uint8_t MessageID = 18;

	//###############################################################################
RTC_DateTypeDef RTC_DateStructure;
RTC_TimeTypeDef RTC_TimeStructure;
RTC_InitTypeDef RTC_InitStructure;
uint32_t 	LSE_WAIT_CNT  = 0;
//RTC_AlarmTypeDef RTC_AlarmStructure;
//NVIC_InitTypeDef NVIC_InitStructure;
//EXTI_InitTypeDef EXTI_InitStructure;
//__IO uint32_t AsynchPrediv = 0, SynchPrediv = 0;
//__IO uint8_t showtime[50] = {0};
//__IO uint8_t showdate[50] = {0};
	
	//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO	
	
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_PWR, ENABLE);

 

  
  if (RTC_ReadBackupRegister(RTC_BKP_DR0) != 0x5AA5)
  {
     /* Allow access to RTC */
  PWR_BackupAccessCmd(ENABLE);
		
  /* Reset Backup Domain */
  PWR_BackupAccessCmd(ENABLE);
 // RCC_RTCResetCmd(DISABLE);
		
		/*!< LSE Enable */
    RCC_LSEConfig(RCC_LSE_ON);

    /*!< Wait till LSE is ready */
		LSE_WAIT_CNT = 0 ;
    while (RCC_GetFlagStatus(RCC_FLAG_LSERDY) == RESET)
    {
		LSE_WAIT_CNT++;
			Delay_ms(1);
		if(LSE_WAIT_CNT > 100)
		{
			
			USART_Send_String ( &DEBUG_USART_Config , "Error Waiting for LSE  ready . . . .\r\n" );
			break ;
		}
		}

    /*!< LCD Clock Source Selection */
    RCC_RTCCLKConfig(RCC_RTCCLKSource_LSE);

    /* Enable the RTC Clock */
    RCC_RTCCLKCmd(ENABLE);

    /* Wait for RTC APB registers synchronisation */
    RTC_WaitForSynchro();

    /* RTC Wakeup Interrupt Generation: Clock Source: RTCDiv_16, Wakeup Time Base: 4s */
    //RTC_WakeUpClockConfig(RTC_WakeUpClock_RTCCLK_Div16);
   //RTC_SetWakeUpCounter(0x7FF);
    /* Enable the Wakeup Interrupt */
    //RTC_ITConfig(RTC_IT_WUT, ENABLE);
    /* Enable Wakeup Counter */
   // RTC_WakeUpCmd(ENABLE);

    /*Calender Configuartion*/
    RTC_InitStructure.RTC_AsynchPrediv = 0x7F;
    RTC_InitStructure.RTC_SynchPrediv =  0xFF;
    RTC_InitStructure.RTC_HourFormat = RTC_HourFormat_24;
    RTC_Init(&RTC_InitStructure);
		
	
		/* Set the date: Wednesday August 15th 2012 */
  RTC_DateStructure.RTC_Year = 14;
  RTC_DateStructure.RTC_Month = RTC_Month_May;
  RTC_DateStructure.RTC_Date = 11;
  RTC_DateStructure.RTC_WeekDay = RTC_Weekday_Tuesday;
  RTC_SetDate(RTC_Format_BCD, &RTC_DateStructure);
  
  /* Set the time to 00h 00mn 00s AM */
  RTC_TimeStructure.RTC_H12     = RTC_H12_AM;
  RTC_TimeStructure.RTC_Hours   = 0x00;
  RTC_TimeStructure.RTC_Minutes = 0x00;
  RTC_TimeStructure.RTC_Seconds = 0x00; 
  RTC_SetTime(RTC_Format_BCD, &RTC_TimeStructure);    
  

    RTC_WriteBackupRegister(RTC_BKP_DR0, 0x5AA5);

		RTC_WriteBackupRegister(RTC_BKP_DR8, 0x5AA5); //indicate that the time is not set but defaults have been loaded
		RTCWasReset = TRUE;
		  /* disable access to RTC */
  PWR_BackupAccessCmd(DISABLE);
  }
  else
  {
    /* Wait for RTC APB registers synchronisation */
    RTC_WaitForSynchro();
  }
	
  
  
  RTC_ClearFlag(RTC_FLAG_ALRAF);
 
	
	//##############################################################################
//	//	RTC_InitTypeDef RTC_InitStructure;
//	/* Enable PWR APB1 Clock */
//	RCC_APB1PeriphClockCmd(RCC_APB1Periph_PWR, ENABLE);

//	//  /* Block access to RTC */
//	PWR_BackupAccessCmd(DISABLE);
}

void NVRAM_WriteByte(NVRAM_Location_Type location, uint8_t data)
{
	uint8_t MessageID = 19;
	uint32_t temp = 0;
	uint8_t bank = 0;
	uint8_t bytepos = 0;
	//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	
	//first decode the backup location for this write
	bank = location / 4;
	bytepos = (location - (bank * 4));
	//read the current bank state
	temp = RTC_ReadBackupRegister(bank);
	//clear the interested byte location
	temp &= ~(0x000000FF << ((3 - bytepos) * 8));

	//write the bute to the position
	temp |= (((uint32_t)data) << ((3 - bytepos) * 8));

	PWR_BackupAccessCmd(ENABLE);
	RTC_WriteBackupRegister(bank, temp); //
	PWR_BackupAccessCmd(DISABLE);

}
uint8_t NVRAM_ReadByte(NVRAM_Location_Type location)
{
	uint8_t MessageID = 20;
	uint32_t temp = 0;
	uint8_t bank = 0;
	uint8_t bytepos = 0;
	//uint8_t retbyte = 0;	
	//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	
	//first decode the backup location for this write
	bank = location / 4;
	bytepos = location - (bank * 4);
	//read the current bank state
	temp = RTC_ReadBackupRegister(bank);

	//preserve only the byte needed	

	temp >>= ((3 - bytepos) * 8);
	//(0x000000FF << 	(bytepos *8));
	return (uint8_t)temp;
}

void ConfigureWatchdog(void)
{
	uint8_t MessageID = 21;
	NVIC_InitTypeDef NVIC_InitStructure;
	//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_WWDG, ENABLE);

	//IWDG_WriteAccessCmd(IWDG_WriteAccess_Enable);	
	//WWDG_DeInit();


	WWDG_SetPrescaler(WWDG_Prescaler_8);

	/* Set Window value to 80; WWDG counter should be refreshed only when the counter
	is below 80 (and greater than 64) otherwise a reset will be generated */

	/* Enable WWDG and set counter value to 127, WWDG timeout = ~910 us * 64 = 58.24 ms 
	  In this case the refresh window is: ~910 * (127-80) = 42.7ms < refresh window < ~910 * 64 = 58.2ms
	*/

	WWDG_SetWindowValue(0x7F); //(0x7F);	



	WWDG_EnableIT();//enable the early wake up interrupt



	/* Set WWDG interrupt vector Preemption Priority to 1 */
	NVIC_InitStructure.NVIC_IRQChannel = WWDG_IRQn;
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;

	NVIC_Init(&NVIC_InitStructure);


	WWDG_Enable(0x7F);    //enable the window watchdog timer
}


void DisableWatchdog(void)
{
	uint8_t MessageID = 22;
//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	
	ReloadWatchdogCounter();
	WWDG_DeInit();

}



ErrorStatus StartGlobalDelayTimeout(DelayDataType * Delay,uint32_t Delaytime)
{
	if(Delaytime == 0) //use the default if zero is sent
	{
		//make sure the defaulet has been set
		if(Delay->DefaultDelayTime != 0)
		{
		Delay->DelayTime = Delay->DefaultDelayTime;
		}
		else
		{
			//default time not set
			return ERROR;
		}
			
	}
	else
	{
		Delay->DelayTime = Delaytime;
	}
	
	//load the current period counter
Delay->LastPeriodCount = SystickCount_us ;
	
return SUCCESS;	
}

bool CheckDelayTimeout( DelayDataType * Delay) //check if a global delay item has timed out
{
	if (SystickCount_us - Delay->LastPeriodCount > Delay->DelayTime )
	{
		return TRUE ;
	}
	else
	{
		return FALSE ;
	}
}




void LedState(LedColour Colour , SwitchState State )
{
	SwitchState RealState = State ;
	if(LedInverted[Colour] == TRUE) 
	{
	RealState = (SwitchState)(State ^ 1) ;
	}
	
	if(RealState == ON)
	{
		GPIO_SetBits(LedsGpio[Colour].IO_Port ,LedsGpio[Colour].IO_Pin);
	}
	else if (RealState == OFF)
	{
		GPIO_ResetBits( LedsGpio[Colour].IO_Port ,LedsGpio[Colour].IO_Pin);
	}
	
}

void LedBlink(LedColour Colour , uint32_t delay)
{

				LedState(Colour,ON);
					Delay_ms(delay);
				LedState(Colour,OFF);


}


void ReloadWatchdogCounter(void)
{
	WWDG_SetCounter(0x7F);
}

void SystemReset(void)
{
	uint8_t MessageID = 24;
//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	
	//execute the system reset
	NVIC_SystemReset();
}



ErrorStatus SendControlMessageReportIN(uint8_t MsgID,int Param ,char* MessagePtr)
{
	static uint8_t k ;
	uint8_t UsbCRC;
	uint32_t MoreMessage ,MessCnt;
	uint8_t MaxMesgSize = (sizeof(Transmit_Buffer) - 9) ;

	
		
			//lets determine the size of the string
		for (k = 0; MessagePtr[k] != 0; k++) ; //just loop here till null terminator

		
		MessCnt = 0		;
		MoreMessage = 0;
//check if multimessage is required
		do 
		{
	ReloadWatchdogCounter();
			if (WaitPrevXferComplete() == SUCCESS)    //wait for previous transfer to be complete before messing with the transmit buffer
			{
				PrevXferComplete = 0;

	

		Transmit_Buffer[0] = 4 ;//IN_ControlStatus;

		Transmit_Buffer[1] = 3; //set to 3 to indicate a control message report as this same report id is used for controller vars amd status etc etc  reportin
								//message id can be used to classify the type of message being sent 
		Transmit_Buffer[2] = MsgID;          //set the message id so thecomputer can identify the message coming through

		//append message parameter
		Transmit_Buffer[3] = 0xff & Param ; //o  
		Transmit_Buffer[4] = 0xff &(Param >> 8); 
		Transmit_Buffer[5] = 0xff &(Param >> 16);
				
//				FIX_VB_APP_FORTHIS:

		if(k > MaxMesgSize)
		{
			MoreMessage = k - MaxMesgSize ;
			//sset new value of k
			k = MaxMesgSize;
			
			//use to indicate multiple concatenated message				
			Transmit_Buffer[6] = (uint8_t) (MoreMessage / MaxMesgSize) ; //show messages remaoning
				
			if ((Transmit_Buffer[6] * MaxMesgSize) < MoreMessage) //if there were remainders
			{
				Transmit_Buffer[6]++; //add one more fr the remaining data
			}
			
		}
		else
		{
			MoreMessage = 0 ;
			//use to indicate multiple concatenated message				
		Transmit_Buffer[6] = 0 ;
		}

		Transmit_Buffer[7] = k;    //append the message size
		
		CopyString(&MessagePtr[MessCnt* MaxMesgSize], (char*) &Transmit_Buffer[8], k);


		//compute the crc of the transmit buffer
		UsbCRC = CRC_Cal8Bits(Transmit_Buffer, 63);//	PROFILE_REPORT_SIZE

		//append the crc to the last byte [63]	
		Transmit_Buffer[63] = UsbCRC;



		/* Copy mouse position info in ENDP1 Tx Packet Memory Area*/
		USB_SIL_Write(EP1_IN, Transmit_Buffer, PROFILE_REPORT_SIZE + 1); //the buffer count variable must be exactly equal to the report count +1(one extra byte for the report ID) on the report descriptor for this report

		/* Enable endpoint for transmission */
		SetEPTxValid(ENDP1);
		}
		else
		{
			//usb wait to send timeout
			return ERROR;
		}	
			MessCnt++;
			k = MoreMessage; //load any remaining message count into k for next iteration
		}while(MoreMessage > 0) ;//multiple message loop
		
		return SUCCESS;
	

}


//Given a command, reads a given 2-byte value with CRC from the HTU21D
ErrorStatus I2Cx_Read( I2C_TypeDef * I2Cx, uint8_t I2Cx_ADDRESS, uint8_t* pBuffer, uint8_t ReadAddr, uint16_t NumByteToRead ,TimeoutCallbackFunctionType TimeoutCallback) 
{
	uint8_t count;

	I2Cx_Timeout = I2Cx_LONG_TIMEOUT;
	while(I2C_GetFlagStatus(I2Cx, I2C_FLAG_BUSY) != RESET)
  {
    if((I2Cx_Timeout--) == 0) 
		{
	TimeoutCallback();
				return ERROR ;
		}
	ReloadWatchdogCounter();
	}

	
/* Test on BUSY Flag */
  I2Cx_Timeout = I2Cx_LONG_TIMEOUT;
  while(I2C_GetFlagStatus(I2Cx, I2C_ISR_BUSY) != RESET)
  {
		ReloadWatchdogCounter();
    if((I2Cx_Timeout--) == 0) 
			{
			TimeoutCallback();
			return ERROR ;
		  }
  }

/* Configure slave address, nbytes, reload, end mode and start or stop generation */
  I2C_TransferHandling(I2Cx, I2Cx_ADDRESS , 1, I2C_SoftEnd_Mode, I2C_Generate_Start_Write);
  
  /* Wait until TXIS flag is set */
  I2Cx_Timeout = I2Cx_LONG_TIMEOUT;
  while(I2C_GetFlagStatus(I2Cx, I2C_ISR_TXIS) == RESET)
  {
		ReloadWatchdogCounter();
    if((I2Cx_Timeout--) == 0) 
			{
			TimeoutCallback();
			return ERROR ;
		  }
  }


/* Send I2Cx Insruction Byte */

	I2C_SendData(I2Cx, ReadAddr);
  
  /* Wait until TC flag is set */
  I2Cx_Timeout = I2Cx_LONG_TIMEOUT;
  while(I2C_GetFlagStatus(I2Cx, I2C_ISR_TC) == RESET)
  {
		ReloadWatchdogCounter();
    if((I2Cx_Timeout--) == 0) 
		{
			TimeoutCallback();
			return ERROR ;
		}
	}


  /* Configure slave address, nbytes, reload, end mode and start or stop generation */
  I2C_TransferHandling(I2Cx,I2Cx_ADDRESS  , NumByteToRead, I2C_AutoEnd_Mode, I2C_Generate_Start_Read); 
  
    
	
	for (count = 0; count <= NumByteToRead -1 ; )
	{
		
    /* Wait until RXNE flag is set */
    I2Cx_Timeout = I2Cx_LONG_TIMEOUT;
    while(I2C_GetFlagStatus(I2Cx, I2C_ISR_RXNE) == RESET)    
    {
			ReloadWatchdogCounter();
      if((I2Cx_Timeout--) == 0) 
			{
			TimeoutCallback();
			return ERROR ;
		  }
    }

			
	   /* Read data from RXDR */
pBuffer[count] = I2C_ReceiveData(I2Cx); //remove this -1 later if the above nack check isnt used and count is incremented by the for construct
	

count++ ;
  
	}
  /* Wait until STOPF flag is set */
  I2Cx_Timeout = I2Cx_LONG_TIMEOUT;
  while(I2C_GetFlagStatus(I2Cx, I2C_ISR_STOPF) == RESET)   
  {
		ReloadWatchdogCounter();
    if((I2Cx_Timeout--) == 0)
			{
			TimeoutCallback();
			return ERROR ;
		  }
  }
  
  /* Clear STOPF flag */
  I2C_ClearFlag(I2Cx, I2C_ICR_STOPCF);
  

return SUCCESS;	
}	



ErrorStatus I2Cx_Write( I2C_TypeDef * I2Cx, uint8_t I2Cx_ADDRESS, uint8_t* pBuffer, uint8_t WriteAddr, uint16_t NumByteToWrite, TimeoutCallbackFunctionType TimeoutCallback) 
{
	//ErrorStatus  DispSend( uint8_t mode, uint8_t * data , uint32_t count )

		uint32_t i;

		
		/* Test on BUSY Flag */
 I2Cx_Timeout = I2Cx_LONG_TIMEOUT;
  while(I2C_GetFlagStatus(I2Cx, I2C_ISR_BUSY) != RESET)
  {
	ReloadWatchdogCounter();
    if((I2Cx_Timeout--) == 0) 
			{
			TimeoutCallback();
			return ERROR ;
		  }
  }
  
  /* Configure slave address, nbytes, reload, end mode and start or stop generation */
  I2C_TransferHandling(I2Cx, I2Cx_ADDRESS, 1, I2C_Reload_Mode, I2C_Generate_Start_Write);
  
  /* Wait until TXIS flag is set */
 I2Cx_Timeout = I2Cx_LONG_TIMEOUT; 
  while(I2C_GetFlagStatus(I2Cx, I2C_ISR_TXIS) == RESET)   
  {
		ReloadWatchdogCounter();
    if((I2Cx_Timeout--) == 0)
			{
			TimeoutCallback();
			return ERROR ;
		  }
  }
  

	
	I2C_SendData(I2Cx, WriteAddr);
  
  /* Wait until TCR flag is set */
  I2Cx_Timeout = I2Cx_LONG_TIMEOUT;
  while(I2C_GetFlagStatus(I2Cx, I2C_ISR_TCR) == RESET)
  {
		ReloadWatchdogCounter();
    if((I2Cx_Timeout--) == 0) 
		{
			TimeoutCallback();
			return ERROR ;
		}
	}
		
//  
//	/* Configure slave address, nbytes, reload, end mode and start or stop generation */
//  I2C_TransferHandling(I2Cx, I2Cx_ADDRESS, NumByteToWrite, I2C_AutoEnd_Mode, I2C_No_StartStop);
//       
//  /* Wait until TXIS flag is set */
//  I2Cx_Timeout = I2Cx_LONG_TIMEOUT;
//  while(I2C_GetFlagStatus(I2Cx, I2C_ISR_TXIS) == RESET) //wait for transmit interrupt status
//  {
//		ReloadWatchdogCounter();
//    if((I2Cx_Timeout--) == 0) 
//		{
//			TimeoutCallback();
//			return ERROR ;
//		}
//	} 
	
		/* Configure slave address, nbytes, reload, end mode and start or stop generation */
  I2C_TransferHandling(I2Cx, I2Cx_ADDRESS, NumByteToWrite, I2C_AutoEnd_Mode, I2C_No_StartStop);
    
//now we can send the data to the specified memory address

for (i=0;i < NumByteToWrite;i++)
{
   
  /* Wait until TXIS flag is set */
 I2Cx_Timeout = I2Cx_LONG_TIMEOUT;
  while(I2C_GetFlagStatus(I2Cx, I2C_ISR_TXIS) == RESET) //wait for transmit interrupt status
  {
		ReloadWatchdogCounter();
    if((I2Cx_Timeout--) == 0) 
		{
			TimeoutCallback();
			return ERROR ;
		}
	} 
	
	/* Write data to for the specified RDAC */
  I2C_SendData(I2Cx, pBuffer[i]);
	
//	if (count == 1)
//	{
//		break;
//	}
}
     
  /* Wait until STOPF flag is set */
 I2Cx_Timeout = I2Cx_LONG_TIMEOUT;
  while(I2C_GetFlagStatus(I2Cx, I2C_ISR_STOPF) == RESET)
  {
		ReloadWatchdogCounter();
    if((I2Cx_Timeout--) == 0) 
			{
			TimeoutCallback();
			return ERROR ;
		  }
  }   
  
  /* Clear STOPF flag */
  I2C_ClearFlag(I2Cx, I2C_ICR_STOPCF);
	

	return SUCCESS;
	
}



ErrorStatus I2C_Config(I2C_TypeDef * I2Cx)
{
	GPIO_InitTypeDef GPIO_InitStructure;
//	I2C_TypeDef * 
  I2C_InitTypeDef  I2C_InitStruct;
	
uint32_t	I2Cx_CLK ;
uint16_t	I2Cx_SCK_PIN  ;
GPIO_TypeDef * I2Cx_SCK_GPIO_PORT  ;
uint32_t I2Cx_SCK_GPIO_CLK  ;
uint8_t I2Cx_SCK_SOURCE   ;
uint8_t I2Cx_SCK_AF  ;

uint16_t I2Cx_SDA_PIN               ;
GPIO_TypeDef * I2Cx_SDA_GPIO_PORT  ;
uint32_t I2Cx_SDA_GPIO_CLK  ;
uint8_t I2Cx_SDA_SOURCE  ;
uint8_t I2Cx_SDA_AF ; 
	
	I2C_DeInit(I2Cx);

	if(I2Cx == I2C1)
	{
//I2Cx            =           I2C1 ;
I2Cx_CLK        =           RCC_APB1Periph_I2C1;

I2Cx_SCK_PIN     =          GPIO_Pin_6    ;              /* PB.06 */
I2Cx_SCK_GPIO_PORT =        GPIOB   ;                    /* GPIOB */
I2Cx_SCK_GPIO_CLK  =        RCC_AHBPeriph_GPIOB;
I2Cx_SCK_SOURCE    =        GPIO_PinSource6;
I2Cx_SCK_AF         =       GPIO_AF_4;

I2Cx_SDA_PIN      =         GPIO_Pin_7   ;               /* PB.7 */
I2Cx_SDA_GPIO_PORT    =     GPIOB      ;                 /* GPIOB */
I2Cx_SDA_GPIO_CLK   =       RCC_AHBPeriph_GPIOB;
I2Cx_SDA_SOURCE     =       GPIO_PinSource7;
I2Cx_SDA_AF         =       GPIO_AF_4;

	}
	else if(I2Cx == I2C2)
	{
		
//I2Cx                       I2C2
I2Cx_CLK         =          RCC_APB1Periph_I2C2;

I2Cx_SCK_PIN        =       GPIO_Pin_9     ;             /* PB.06 */
I2Cx_SCK_GPIO_PORT   =      GPIOA     ;                  /* GPIOB */
I2Cx_SCK_GPIO_CLK    =      RCC_AHBPeriph_GPIOA;
I2Cx_SCK_SOURCE      =      GPIO_PinSource9;
I2Cx_SCK_AF          =      GPIO_AF_4;

I2Cx_SDA_PIN        =       GPIO_Pin_10   ;               /* PB.7 */
I2Cx_SDA_GPIO_PORT  =       GPIOA       ;                /* GPIOB */
I2Cx_SDA_GPIO_CLK     =     RCC_AHBPeriph_GPIOA;
I2Cx_SDA_SOURCE     =       GPIO_PinSource10;
I2Cx_SDA_AF         =       GPIO_AF_4;
		
	}
	else
	{
		return ERROR;
	}
	
	
	
  /* Enable the I2C periph */
  RCC_APB1PeriphClockCmd(I2Cx_CLK, ENABLE);
  
  /* Enable SCK and SDA GPIO clocks */
  RCC_AHBPeriphClockCmd(I2Cx_SCK_GPIO_CLK | I2Cx_SDA_GPIO_CLK , ENABLE);
  

  GPIO_PinAFConfig(I2Cx_SCK_GPIO_PORT, I2Cx_SCK_SOURCE, I2Cx_SCK_AF);
  GPIO_PinAFConfig(I2Cx_SDA_GPIO_PORT, I2Cx_SDA_SOURCE, I2Cx_SDA_AF);
  
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_OD;
  GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_UP;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  
  /* I2C SCK pin configuration */
  GPIO_InitStructure.GPIO_Pin = I2Cx_SCK_PIN;
  GPIO_Init(I2Cx_SCK_GPIO_PORT, &GPIO_InitStructure);
  
  /* I2C SDA pin configuration */
  GPIO_InitStructure.GPIO_Pin =  I2Cx_SDA_PIN;
  GPIO_Init(I2Cx_SDA_GPIO_PORT, &GPIO_InitStructure);

  
  /* I2C configuration -------------------------------------------------------*/
 I2C_DeInit(I2Cx);
 

 
        /* Set the I2C structure parameters */
				I2C_InitStruct.I2C_AnalogFilter = I2C_AnalogFilter_Enable;
				I2C_InitStruct.I2C_DigitalFilter = 0x03; /*!< Configures the digital noise filter. This parameter can be a number between 0x00 and 0x0F */  
        I2C_InitStruct.I2C_Mode = I2C_Mode_I2C;
        //I2C_InitStruct.I2C_DutyCycle = I2C_DutyCycle_2;
//        I2C_InitStruct.I2C_OwnAddress1 = Own_I2C_Address;
        I2C_InitStruct.I2C_Ack = I2C_Ack_Enable;
        I2C_InitStruct.I2C_AcknowledgedAddress = I2C_AcknowledgedAddress_7bit;
        //I2C_InitStruct.I2C_ClockSpeed = 30000;
				I2C_InitStruct.I2C_Timing =  0x00902025; //This parameter calculated by referring to I2C initialization section in Reference manual

        /* Initialize the I2C peripheral w/ selected parameters */
        I2C_Init(I2Cx,&I2C_InitStruct);

        /* Enable the I2C peripheral */
        I2C_Cmd(I2Cx, ENABLE);

	return SUCCESS;
}



uint8_t	SPI_Send_Data(SPI_TypeDef * SPI_Base , uint8_t SPI_Data, TimeoutCallbackFunctionType TimeoutCallback)
{
	  /*!< Wait until the transmit buffer is empty */
			 SPI_Timeout = SPI_MAX_TIMEOUT;
  while(SPI_I2S_GetFlagStatus(SPI_Base, SPI_I2S_FLAG_TXE) == RESET)
  {
ReloadWatchdogCounter();
		if((SPI_Timeout--) == 0) 
		{
					
			USART_Send_String(&DEBUG_USART_Config," SPI TIMEOUT SPI_I2S_FLAG_TXE writebyte \r\n");	
			TimeoutCallback();
			return 0;
		}
  }
  
  /*!< Send the byte */
  SPI_SendData8(SPI_Base, SPI_Data);
  
	
	
	
  /*!< Wait to receive a byte*/
		 SPI_Timeout = SPI_MAX_TIMEOUT;
  while(SPI_I2S_GetFlagStatus(SPI_Base, SPI_I2S_FLAG_RXNE) == RESET)
  {
	ReloadWatchdogCounter();
		if((SPI_Timeout--) == 0) 
		{
			
					TimeoutCallback();
			USART_Send_String( &DEBUG_USART_Config," SPI TIMEOUT SPI_I2S_FLAG_RXNE writebyte \r\n");
			return 0;
		}
  }
  
  /*!< Return the byte read from the SPI bus */ 
  return (uint8_t)SPI_ReceiveData8(SPI_Base);
}




void BootLoaderInit(void)
{
	uint8_t MessageID = 27;
	// RCC_APB1PeriphClockCmd(RCC_APB1Periph_WWDG, DISABLE);
//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	
	if ((NVRAM_ReadByte(NVR_BootloaderRequest) != 0xA5) && (NVRAM_ReadByte(NVR_BootloaderRequest) != 0x5A)) //)	
	{
		ReloadWatchdogCounter();
		//set the nvram flag for enteriign bootloader

		if (USE_SYSMEM_BOOT == TRUE)
		{
			NVRAM_WriteByte(NVR_BootloaderRequest, 0x5A);
		}
		else
		{
			NVRAM_WriteByte(NVR_BootloaderRequest, 0xA5);
		}
		//bootloader will check for this register if it finds this value then it will enter bootloader mode

		//reset the system
		SystemReset();
	}
	else
	{
		//go on and load bootloader manually if bootloader didnt catch the messgae on nvram
		//bootloder code will reset the nvram address to 0000
	}


	//shut down any task running
	//rcc deinit moved to the if for non sysmem boot
	SysTick->CTRL = 0;  //reset the systick timer
	SysTick->LOAD = 0;
	SysTick->VAL = 0;
	//		RCC_SYSCLKConfig (RCC_SYSCLKSource_HSI ); //select HSI as system clock source

	NVIC->ICPR[0] = 0xFFFFFFFF; //clear all pending interrupts NVIC_ICPR_CLRPEND);
	NVIC->ICPR[1] = 0xFFFFFFFF;

	/* Enable ADC4 */
	ADC_Cmd(ADC4, DISABLE);  //disable the adc so we dont return with the adc read ensuing



	//Delay_ms(500)	;
	//DisableWatchdog();
	//BootloaderAddress = 
	//SysMemBootJump = (void (*) (void)) (*((uint32_t *) (BootloaderAddress + 4)));
	if (USE_SYSMEM_BOOT == TRUE)
	{
		//USB_Cable_Config(ENABLE);   //enable the usb connect pin as the bootloader may not knowo which pin it is connected to
		SysMemBootJump = (void(*)(void)) (*((uint32_t*)(SysMemBootloaderAddress + 4)));  //we add4 because the first word is the stack pointer value.
		__set_MSP(*(__IO uint32_t *) SysMemBootloaderAddress);   //set the main stack pointer to its defaultt value
	}
	else
	{
		RCC_DeInit(); //we do this here as we cant de init the rcc in case we are going to sysboot we will need to enable the usb connect poin so we need the gpio
		SetCNTR(0);  //clear usb control register
		SysMemBootJump = (void(*)(void)) (*((uint32_t*)(CustomBootloaderAddress + 4)));  //we add4 because the first word is the stack pointer value.
		__set_MSP(*(__IO uint32_t *) CustomBootloaderAddress);   //set the main stack pointer to its defaultt value
	}

	//do not call any other function after setting the stack pointer


	SysMemBootJump();

	//		while(1);

}




uint8_t RTC_GetDaysOfMonth(uint8_t year, uint8_t Month)
{

	
	if((Month == 1) || (Month == 3) ||(Month == 5) ||(Month == 7)||(Month == 8)||(Month == 10)||(Month == 12))
	{
		return 31;
	}
	
	if((Month == 4) || (Month == 6) ||(Month == 9) ||(Month == 11))
	{
		return 30;
	}
	
	if(Month == 2)
	{
		//check if this is a leap year if the year is divisible by 4 without remainder
		if(year % 4)
		{
		return 28;
		}
		else
		{
		return 29;	
		}
	}
	
	return 0; //invalid month specified
}
RTC_DateTimeTypeDef RTC_GetDateTimeFromSeconds(uint32_t DateTimeSeconds)
{
uint8_t years ,i;
RTC_DateTimeTypeDef DateTime;	
RTC_DateTimeTypeDef NullDateTime;		
uint32_t RemDays,DaysOfMonth,RemSeconds;
years = ((float)(DateTimeSeconds / (3600 * 24)) / 365.25f) ;//convert secons to days and then years

//store the year	
DateTime.RTC_Year = years;

//remove the toatl days taken by past years
DateTimeSeconds -= ((365 * DateTime.RTC_Year) +	(DateTime.RTC_Year / 4)) * 24 * 3600 ;

//get the total days remoining
RemDays = DateTimeSeconds / (24 * 3600)	;
	
	for(i = RTC_Month_January; i <= RTC_Month_December ;i++)
	{
		DaysOfMonth = RTC_GetDaysOfMonth(DateTime.RTC_Year ,i);
		if (RemDays > DaysOfMonth)
		{
		RemDays -= 	DaysOfMonth ; //remove the days if the current month
		}
		else
		{
			break;
		}
	}
	if(i>RTC_Month_December)
	{
		//error ocurerd
		return NullDateTime;
	}
	DateTime.RTC_Month = i;
	DateTime.RTC_Date = 	RemDays;
	//get the day of the week
	DateTime.RTC_WeekDay = RTC_GetWeekday(DateTime.RTC_Year,DateTime.RTC_Month,DateTime.RTC_Date);
	
	
	RemSeconds = DateTimeSeconds % (24 * 3600);

//convert the remseconds to time of day
	DateTime.RTC_Hours = RemSeconds  / 3600 ; //get the hour
	
	DateTime.RTC_Minutes = (RemSeconds % 3600) / 60 ; //get the minutes
	
	DateTime.RTC_Seconds = (RemSeconds % 3600) % 60 ; //get the seconds

return 	DateTime;
}



uint32_t RTC_GetDateTimeSeconds(RTC_DateTimeTypeDef StartDateTime)
{
	uint32_t TotalDays , TotalSeconds;
	//copy the time and date
//	RTC_DateTimeTypeDef TempDateTime = StartDateTime;
	

	TotalDays = RTC_GetTotalDays(StartDateTime.RTC_Year,StartDateTime.RTC_Month,StartDateTime.RTC_Date);
	//convert the total full days to seconds
	TotalSeconds = TotalDays * 24 * 3600; 
	//get the total seconds so far on this day
	TotalSeconds += StartDateTime.RTC_Hours * 3600 ; //convert the hour
	
	TotalSeconds += StartDateTime.RTC_Minutes * 60 ; //convert the minutes
	
	TotalSeconds += StartDateTime.RTC_Seconds ; //conver the seconds

return TotalSeconds;	
}

uint8_t RTC_GetWeekday(uint8_t year, uint8_t month,uint8_t day)
{
uint8_t 	weekday ;
	uint32_t TotalDays ;
TotalDays =	RTC_GetTotalDays(year,month,day );
//this function can only do for dates from the year 2000
//the first day of the yeah 2000 was a saturday ie RTC_Weekday_Saturday
	weekday = TotalDays % 7;
	if(weekday)
	{
		if(weekday > 1)
		{
			return  weekday - 1;
		}
		else
		{
			return RTC_Weekday_Sunday;
		}
	}
	else
	{
		return RTC_Weekday_Saturday;
	}
}

uint32_t RTC_GetTotalDays(uint8_t year, uint8_t month,uint8_t date)
{
	uint32_t TotalDays ,i;
	TotalDays = (365 * year) +	(year / 4) ;
	for(i = RTC_Month_January; i <= RTC_Month_December ;i++)
	{
		if(month  == i)
		{
			TotalDays += date; 
			break;
		}
		//se the temporary month so we can count the days in it
		TotalDays += RTC_GetDaysOfMonth(year ,i);
	}
	return TotalDays;
}
char *  RTC_GetDateTimeString(RTC_DateTimeTypeDef * DateTime)
{
	uint8_t Cnt;
		//get the current date and time

	
		//insert the date
		Cnt=0;
		Cnt =	sprintf(CurrentDateTimeString,"%0.2d/%0.2d/%0.2d", DateTime->RTC_Date,DateTime->RTC_Month, 2000 + DateTime->RTC_Year); 
		//insert houre:minutes: seconds
		Cnt += sprintf((char *)&CurrentDateTimeString[Cnt],"% 0.2d:%0.2d:%0.2d",DateTime->RTC_Hours, DateTime->RTC_Minutes, DateTime->RTC_Seconds);
		
	//CurrentDateTime[Cnt] = 0;
	return 	CurrentDateTimeString ;
}


int32_t RTC_GetDateTimePeriod(RTC_DateTimeTypeDef StartDateTime, RTC_DateTimeTypeDef EndDateTime)
{
//int8_t years, months, days,hours,minutes,seconds;	
int32_t TimePeriod;
//compare the year value

	
TimePeriod = (int64_t)RTC_GetDateTimeSeconds(EndDateTime) - (int64_t)RTC_GetDateTimeSeconds(StartDateTime);

return TimePeriod;	
}

RTC_DateTimeTypeDef RTC_GetDateTimeOffset(RTC_DateTimeTypeDef CurrentDateTime,int32_t TimeSeconds)
{
///int days,hours,mins,secs;
///uint8_t WeekdaySum,DaysOfMonth;
int32_t CurrentSeconds;
RTC_DateTimeTypeDef NewDateTime;	
if (abs(TimeSeconds) < 1)	
{	//return the current time if the absolute offset is less than 1
	return CurrentDateTime;
}
//calculate the time offset

//get the total seconds of the reference time
CurrentSeconds = RTC_GetDateTimeSeconds(CurrentDateTime);

//offset the current seconds
CurrentSeconds += TimeSeconds ;

//get the new date from the offset
NewDateTime = RTC_GetDateTimeFromSeconds(CurrentSeconds);

return NewDateTime;
/*
DaysOfMonth = RTC_GetDaysOfMonth(CurrentDateTime.RTC_Year, CurrentDateTime.RTC_Month ) ;
days = TimeSeconds / 86400;
if(days)//if its up to an hour
{
	//set the weekday
	WeekdaySum = abs(days % 7);
	DaysOfMonth = RTC_GetDaysOfMonth(CurrentDateTime.RTC_Year, CurrentDateTime.RTC_Month ) ;
	if(days>0)
	{
		while(days >(DaysOfMonth - CurrentDateTime.RTC_Date))
		{
			days -= (DaysOfMonth - CurrentDateTime.RTC_Date);
			//set to first of next month
			CurrentDateTime.RTC_Date = 0;
			//incrememnt the month
			CurrentDateTime.RTC_Month++ ;
			if(CurrentDateTime.RTC_Month > 12)
			{
				//increment the year
				CurrentDateTime.RTC_Year ++;
				if(CurrentDateTime.RTC_Year > 99)
				{
					CurrentDateTime.RTC_Year = 1;
				}
				CurrentDateTime.RTC_Month = 1;
			}
			//calculate the days of the new month
			DaysOfMonth = RTC_GetDaysOfMonth(CurrentDateTime.RTC_Year, CurrentDateTime.RTC_Month ) ;
		}
		//add the remaaining days to the date
		CurrentDateTime.RTC_Date = days;
		
		if(WeekdaySum > (7 - CurrentDateTime.RTC_WeekDay))
		{
			CurrentDateTime.RTC_WeekDay = WeekdaySum - (7 - CurrentDateTime.RTC_WeekDay);
		}
	}
	else if(days<0) 
	{		
		while(abs(days) > CurrentDateTime.RTC_Date)
		{
			//reduce the days to get to the previous month
			days += CurrentDateTime.RTC_Date;
			//set the date to the last day of the month
			CurrentDateTime.RTC_Date = DaysOfMonth;
			//decrement the current month
			if(CurrentDateTime.RTC_Month == 1)
			{
				//decrement the year
				if(CurrentDateTime.RTC_Year ==1)
				{
					CurrentDateTime.RTC_Year = 99;
				}
				else
				{
				CurrentDateTime.RTC_Year --;
				}
				
				CurrentDateTime.RTC_Month = 12;
			}
			else
			{
				CurrentDateTime.RTC_Month-- ;
			}
			//calculate the days of the new month
			DaysOfMonth = RTC_GetDaysOfMonth(CurrentDateTime.RTC_Year, CurrentDateTime.RTC_Month ) ;
		}
		//remove  the remaaining days from the date
		CurrentDateTime.RTC_Date += days;
		
		if( WeekdaySum > (CurrentDateTime.RTC_WeekDay))
		{
			CurrentDateTime.RTC_WeekDay = 7 - (WeekdaySum - (CurrentDateTime.RTC_WeekDay));
		}
	}

}

hours = TimeSeconds / 3600;
if(hours)//if its up to an hour
{ 
	if ((hours>0) &&(hours >(24 - CurrentDateTime.RTC_Hours)))
	{
		hours -= (24 - CurrentDateTime.RTC_Hours);
		CurrentDateTime = RTC_GetDateTimeOffset(CurrentDateTime,86400); //increment the time by 24 hours be reentrant call to self function
	  CurrentDateTime.RTC_Hours = 0;
		//return CurrentDateTime;  //return as the functuion cant handle day overlaps fpr mnow
	}
	else	if((hours<0) &&(abs(hours) > CurrentDateTime.RTC_Hours))
	{
		hours += CurrentDateTime.RTC_Hours;
		CurrentDateTime = RTC_GetDateTimeOffset(CurrentDateTime ,-86400); //decrement the time by 24 hours be reentrant call to self function
		CurrentDateTime.RTC_Hours = 24;
		
		//return CurrentDateTime;  //return as the functuion cant handle day overlaps fpr mnow
	}
	
	CurrentDateTime.RTC_Hours += hours ;
	
}

mins = (TimeSeconds % 3600) /60 ;
if(mins)
{
	if((mins > 0) && (mins >(60 - CurrentDateTime.RTC_Minutes))) //if we are adding wnd will be going to the nedxt hour
	{
		mins -= (59 - CurrentDateTime.RTC_Minutes);
		CurrentDateTime = RTC_GetDateTimeOffset(CurrentDateTime,3600); //increment the time by one hour be reentrant call to self function
	  CurrentDateTime.RTC_Minutes = 0;
	}
	else if((mins < 0) && (abs(mins) > CurrentDateTime.RTC_Minutes)) //if we are subtracting and we will go back the last hour
	{
		mins += CurrentDateTime.RTC_Minutes;
		CurrentDateTime = RTC_GetDateTimeOffset(CurrentDateTime ,-3600); //decrement the time by one hour be reentrant call to self function
		CurrentDateTime.RTC_Minutes = 59;
	}
	
	CurrentDateTime.RTC_Minutes += mins;
}

secs = ((TimeSeconds % 3600) %60);
if(secs)
{
	if((secs > 0) && (secs >(59 - CurrentDateTime.RTC_Seconds))) //if we are adding wnd will be going to the nedxt minute
	{
		secs -= (59 - CurrentDateTime.RTC_Seconds);
		CurrentDateTime = RTC_GetDateTimeOffset(CurrentDateTime,60); //increment the time by one minute be reentrant call to self function
	  CurrentDateTime.RTC_Seconds = 0;
	}
	else if((secs < 0) && (abs(secs) > CurrentDateTime.RTC_Seconds)) //if we are subtracting and we will go back the last minute
	{
		secs += CurrentDateTime.RTC_Seconds;
		CurrentDateTime = RTC_GetDateTimeOffset(CurrentDateTime ,-60); //decrement the time by one minute be reentrant call to self function
		CurrentDateTime.RTC_Seconds = 59;
	}

		CurrentDateTime.RTC_Seconds += secs;
}

return CurrentDateTime;
*/

}

uint16_t ComputeMeanInt16( volatile uint16_t* Array, uint8_t Count)
{
	uint8_t MessageID = 31;
	static uint16_t meanloop, MeanVal;
	uint32_t meansum;
//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
		//compute for Signal 0vs
	meansum = 0;
	for (meanloop = 0; meanloop < Count; meanloop++)
	{
		meansum += Array[meanloop];
	}

	MeanVal = meansum / Count;

	return MeanVal;

}
uint32_t ComputeMeanInt32( volatile uint32_t* Array, uint8_t Count)
{
	uint8_t MessageID = 33;
	static uint32_t meanloop, MeanVal;
	uint32_t meansum;
//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
		//compute for Signal 0vs
	meansum = 0;
	for (meanloop = 0; meanloop < Count; meanloop++)
	{
		meansum += Array[meanloop];
	}

	MeanVal = meansum / Count;

	return MeanVal;

}



uint32_t GetNumberDifference(uint32_t Value1, uint32_t Value2)
{
	uint8_t MessageID = 38;
	uint16_t Diff = 0;
//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	
	if (Value1 > Value2)
	{
		Diff = Value1 - Value2;
	}
	else
	{
		Diff = Value2 - Value1;
	}

	return Diff;
}

float GetNumberDifferenceFloat(float Value1, float Value2)
{
	uint8_t MessageID = 39;
	float Diff = 0;

//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
		if (Value1 > Value2)
	{
		Diff = Value1 - Value2;
	}
	else
	{
		Diff = Value2 - Value1;
	}

	return Diff;
}



void USART_Newline(USART_ConfigType * USART_Conf)
{

	USART_Send_Char(USART_Conf,0x0d);

}


ErrorStatus println(USART_ConfigType * USART_Conf,char *s)
{
	USART_Send_String(USART_Conf,s);
	USART_Newline(USART_Conf);
	return SUCCESS;
}


ErrorStatus USART_Send_String(USART_ConfigType * USART_Conf,char *s) 
{
uint32_t count = 0;
	
	//send debug usart to usb if available
			if((bDeviceState == CONFIGURED) &&(USART_Conf == &DEBUG_USART_Config )) 
			{
				SendControlMessageReportIN(1, 0 ,s);
			}
	
		if((USART_Conf->Configured == FALSE) || ( USART_Conf->Busy  == TRUE))
		{
		return ERROR;	
		}
			 USART_Conf->Busy = TRUE ;
MAX_USART: //consider the maximum usart string oro depend solely on null termination
			while (( *s ) && (count++ <= 1024))
			{
				//	ReloadWatchdogCounter();
				if (USART_Send_Char(USART_Conf , *s++) != SUCCESS)
				{
					return ERROR;
				}
				
				ReloadWatchdogCounter();
			}
			
			 USART_Conf->Busy = FALSE ;
		
	return SUCCESS	;
}




ErrorStatus USART_Send_Char(USART_ConfigType * USART_Conf,unsigned char Data)
{
	UsartTimeout = USART_TIMEOUT_LONG;
 while(USART_GetFlagStatus(USART_Conf->USARTn , USART_FLAG_TXE) == RESET)
 {
	 if((UsartTimeout--) == 0) 
			{
			USARTx_TIMEOUT_UserCallback();
			return ERROR ;
		  }
 }	
USART_SendData (USART_Conf->USARTn,Data); 
return SUCCESS;
}




char * itoha (unsigned int num)
{
static char buf[11];
	uint8_t * byteptr;
int i = -5 ;	
	char temptbyte ;
	char high;
	char low;
	
	byteptr = (uint8_t *) &num	;
	for (i=3;i>= 0;i--)
	{
	//get the first byte
  temptbyte = *(byteptr + i);
		//convert it to ascii
	 high = temptbyte >> 4;
	 low = temptbyte & 0x0F;
	* (buf+((3-i)*2))    = high + '0' + (7 * (high / 10));
	*(buf+((3-i)*2) + 1) = low  + '0' + (7 * (low  / 10));	
		//stuff it in
	}
	*(buf + 8) = 0x0 ; //null terminate
	return buf;
}

ErrorStatus USART_Send_Int(USART_ConfigType * USART_Conf,uint32_t Data)
{
	uint16_t k = 0;
	char Array[6];
	sprintf(Array,"%d",Data ); //convert the data value into ascii format	

	for ( k = 0 ;k<= sizeof(Array) ; k++)
	{	
		if( !Array[k] ) break;
		if (USART_Send_Char(USART_Conf,Array[k]) != SUCCESS)
		{
			return ERROR;
		}
		
	ReloadWatchdogCounter();
	}	
return SUCCESS;	
}

void USART_sprintf(uint32_t Data)
{
	uint16_t k = 0;
	char Array[6];
	sprintf(Array, "%d", Data); //convert the data value into ascii format	

	for (k = 0; k <= sizeof(Array); k++)
	{
		if (!Array[k]) break;
		
		FIX_THIS:
//		UsartTimeout = USART_TIMEOUT_LONG;
//		 while(USART_GetFlagStatus(USART_Conf->USARTn , USART_FLAG_TXE) == RESET)
//		 {
//			 if((UsartTimeout--) == 0) 
//					{
//					USARTx_TIMEOUT_UserCallback();
//					return ERROR ;
//					}
//		 }	
		
		
		while (USART_GetFlagStatus(USART2, USART_FLAG_TXE) == RESET) ; // Wait for transmit buffer to Empty
		USART_SendData(USART2, Array[k]); //send the ascii data of the adc value out serial port

	}

}





static void ADC_Config(void)
{
	uint8_t MessageID = 105;
//	ADC_InitTypeDef ADC_InitStructure;//create the structure used for initialising the adc
//	ADC_CommonInitTypeDef ADC_CommonInitStructure;
//	GPIO_InitTypeDef GPIO_InitStructure; //create the structure used for inititalizing the gpio	
										 //ADC_InjectedInitTypeDef ADC_InjectedInitStructure;
//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	/* Configure the ADC clock */
	RCC_ADCCLKConfig(RCC_ADC34PLLCLK_Div1);

	/* Enable ADC1 clock */
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_ADC34, ENABLE);

	ADC_DeInit(ADC4);



//////	/* Configure signal monitor analogue input*/
//////	/* GPIOC Periph clock enable */
//////	RCC_AHBPeriphClockCmd(Sig_Mon_RCC_AHBPeriph, ENABLE);
//////	GPIO_InitStructure.GPIO_Pin = Sig_Mon_Pin; //we about to configure pin 15 of the specified gpio port
//////	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AN; //configure the gpio pin (PC1 whose additional function is ADC12_in7)for analog input 
//////	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL; //disable pull up and pull down

//////	GPIO_Init(Sig_Mon_Port, &GPIO_InitStructure); //call the gpio_init function and pass the address of the structure to initialize GPIOx


//////	/* Configure power monitor analog inputs*/
//////	/* GPIOE Periph clock enable */
//////	RCC_AHBPeriphClockCmd(Power_Mon_RCC_AHBPeriph, ENABLE);
//////	GPIO_InitStructure.GPIO_Pin = Power_Mon_Pin; //we about to configure pin 15 of the specified gpio port
//////	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AN; //configure the gpio pin (PC1 whose additional function is ADC12_in7)for analog input 
//////	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL; //disable pull up and pull down

//////	GPIO_Init(Power_Mon_Port, &GPIO_InitStructure); //call the gpio_init function and pass the address of the structure to initialize GPIOx


//////	/* Calibration procedure */
//////	ADC_VoltageRegulatorCmd(ADC4, ENABLE); //Enables the ADC1 Voltage Regulator


//////	/* Insert delay equal to 10 �s */
//////	Delay_us(10);

//////	ADC_SelectCalibrationMode(ADC4, ADC_CalibrationMode_Single);  //set calibration mode for single-ended adc operation
//////	ADC_StartCalibration(ADC4); // this starts the selected ADC calibration process


//////	while (ADC_GetCalibrationStatus(ADC4) != RESET) ; //wait untill adc calibration is done and the adc_getcalibration returns a 1

//////	calibration_value = ADC_GetCalibrationValue(ADC4);

//////	ADC_SetCalibrationValue(ADC4, calibration_value);

//////	ADC_StructInit(&ADC_InitStructure); //Fill each ADC_InitStruct member with their default value using & to pass the address

//////	//load the commonInitStructure variables
//////	ADC_CommonInitStructure.ADC_Mode = ADC_Mode_Independent;
//////	ADC_CommonInitStructure.ADC_Clock = ADC_Clock_AsynClkMode;
//////	ADC_CommonInitStructure.ADC_DMAAccessMode = ADC_DMAAccessMode_Disabled;
//////	ADC_CommonInitStructure.ADC_DMAMode = ADC_DMAMode_OneShot;
//////	ADC_CommonInitStructure.ADC_TwoSamplingDelay = 0x02; /*!< Configures the Delay between 2 sampling phases.This parameter can be a value between  0x0 and 0xF  */

//////	ADC_CommonInit(ADC4, &ADC_CommonInitStructure); //Initializes the ADC peripherals according to above parameters 

//////	//Load the InitStructure variables
//////	ADC_InitStructure.ADC_ContinuousConvMode = ADC_ContinuousConvMode_Disable;
//////	ADC_InitStructure.ADC_Resolution = ADC_Resolution_12b;
//////	ADC_InitStructure.ADC_ExternalTrigConvEvent = ADC_ExternalTrigConvEvent_0;
//////	ADC_InitStructure.ADC_ExternalTrigEventEdge = ADC_ExternalTrigEventEdge_None;
//////	ADC_InitStructure.ADC_DataAlign = ADC_DataAlign_Right;
//////	ADC_InitStructure.ADC_OverrunMode = ADC_OverrunMode_Disable;
//////	ADC_InitStructure.ADC_AutoInjMode = ADC_AutoInjec_Disable;
//////	ADC_InitStructure.ADC_NbrOfRegChannel = 2;

//////	ADC_Init(ADC4, &ADC_InitStructure); // Initializes ADCx peripheral using the loaded struct according to above parameters

//////	/* ADC Channel configuration */  //signal monitor channel
//////	ADC_RegularChannelConfig(ADC4, Sig_Mon_ADC_Channel, 1, ADC_SampleTime_601Cycles5);

//////	/* ADC Channel configuration */  //power monitor channel
//////	ADC_RegularChannelConfig(ADC4, Power_Mon_ADC_Channel, 2, ADC_SampleTime_601Cycles5); //ADC_SampleTime_601Cycles5);


//////	ADC_RegularChannelSequencerLengthConfig(ADC4, 2);



//////	/* Enable ADC1 */
//////	ADC_Cmd(ADC4, ENABLE);

//////	/* wait for ADRDY */
//////	while (!ADC_GetFlagStatus(ADC4, ADC_FLAG_RDY)) ;


	/* Start ADC1 Software Conversion */
	//ADC_StartConversion(ADC4);	//depending on the mode you are operating it. single or continuous

}



void Delay_us(uint32_t count)
{
	int i;
	do
	{
		for (i = 0; i < 3; i++)
		{
			__ASM{ nop};
			__ASM{ nop};
			// __ASM{nop};
		}

	} while (--count);

}

void Delay_ms(uint32_t ms)
{
	do
	{
		ReloadWatchdogCounter();
		Delay_us(1000);

	} while (--ms);

}

void USARTx_TIMEOUT_UserCallback(void)
{
	COUNT_THIS_AND:	 //shut down the serial comms if possible
__asm{nop};
//WriteLogFile("Si7021_TIMEOUT_UserCallback");

USART_Send_String(&DEBUG_USART_Config,"USARTx_TIMEOUT_UserCallback");

//Si7021_TIMEOUT_COUNT ++;
//Si7021_Status = -1;

}

void TIMEOUT_UserCallback(void)
{
	while (1)
	{
		//__ASM{nop};
	}

}

ErrorStatus Float2Bytes( float FloatVal, uint8_t * Bytes)
{
	Bytes[0]  = ((uint8_t *)&FloatVal)[0] ; //4 represents 4 bytes of a float
	Bytes[1]  = ((uint8_t *)&FloatVal)[1] ;
	Bytes[2]  = ((uint8_t *)&FloatVal)[2] ;
	Bytes[3]  = ((uint8_t *)&FloatVal)[3] ;
		
return SUCCESS;	
}

float Bytes2Float(uint8_t * Bytes)
{
	float Tempfloat;
	
		((uint8_t*)&Tempfloat)[0] = Bytes[0]; 
		((uint8_t*)&Tempfloat)[1] = Bytes[1]; 
		((uint8_t*)&Tempfloat)[2] = Bytes[2]; 
		((uint8_t*)&Tempfloat)[3] = Bytes[3]; 
						
	return  Tempfloat;
}

#ifdef  USE_FULL_ASSERT

/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t* file, uint32_t line)
{
	/* User can add his own implementation to report the file name and line number,
	   ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */

	/* Infinite loop */
	while (1)
	{
	}
}
#endif



FLASH_Status FLASH_ReadWords(uint32_t* Data, uint32_t Address, uint32_t Count)
{
	uint8_t MessageID = 130;
	uint32_t* wAddr;
//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	wAddr = (uint32_t*)(FLASH_BASE + Address);
	while (Count--)
	{
		*Data++ = *wAddr++;
	}

	return FLASH_COMPLETE;
}

FLASH_Status FLASH_WriteWords(uint32_t* Data, uint32_t Address, uint32_t Count)
{
	uint8_t MessageID = 131;
	FLASH_Status Status;
	uint32_t i;
	uint32_t FLASH_MAX_TIME = 1000;
	__disable_irq();

	//remove this Macro when MessageID variable is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	
	FLASH_Unlock();
	//while(FLASH->PECR & FLASH_PECR_PELOCK); //wait for unlock to be done
	FLASH_WaitForLastOperation(FLASH_MAX_TIME);

	for (i = 0; i < Count; i++)
	{
		Status = FLASH_ProgramWord((FLASH_BASE + Address + i), *(Data + i));
		if (Status != FLASH_COMPLETE)
		{
			FLASH_Lock();
			__enable_irq();
			return Status;
		}
	}

	FLASH_Lock();
	__enable_irq();
	return Status;
}

void USB_Packet_Handler(void)
{
	uint8_t MessageID = 140;
	//remove this when message id is used
DUMMY_MESSAGE_ID_USE_MACRO
	
	IN_USB_HANDLER = TRUE;
	//		uint8_t ,tempx = 0 ;
	//	uint16_t val16 ;
	/*	determine the report that the message contains, using the report ID 	*/
		switch (Receive_Buffer[0])
  {
  	case OUT_SetOperationState: //Change operation mode
		{
			
			break;
		}
  	case OUT_SetClusterPowerLevel : //Set Cluster Power Level
		{
			
			break;
		}
  	case OUT_RequestConfiguration : //
		{
			
  		break;
		}
		case OUT_ControlOperation : //
		{
			
  		break;
		}
		default:
			{

				break;
			}
	}

	SetEPRxStatus(ENDP1, EP_RX_VALID);
	IN_USB_HANDLER = FALSE;
}




void configGPIO(void)
{
	uint8_t MessageID = 155;

	
	GPIO_InitTypeDef GPIO_InitStructure; //create the structure used for inititalizing the gpio
//	EXTI_InitTypeDef EXTI_InitStructure;
//	NVIC_InitTypeDef NVIC_InitStructure;
	
	//remove this when message id is used
DUMMY_MESSAGE_ID_USE_MACRO
	/////////////SETUP OUTPUT PINS USED//////////////////////
	////////////////////////////////////////////////////////
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT; //set the pin function to output for the following pins
	GPIO_InitStructure.GPIO_OType = GPIO_OType_OD;//changed this to open drain as puch pull killed txselect board when processor froze. than made it pull up
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP;//GPIO_PuPd_DOWN;

		 	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
   GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_NOPULL;//GPIO_PuPd_DOWN;
			GPIO_InitStructure.GPIO_Pin =  RED_LED_Pin  ;	// Setup vdd2 enable pin
	RCC_AHBPeriphClockCmd(RED_LED_RCC_AHBPeriph,ENABLE); //enable the ahb peripheral clock for this pin
 	GPIO_Init( RED_LED_Port, &GPIO_InitStructure );    //ini
	
 	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
   GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_NOPULL;//GPIO_PuPd_DOWN;
			GPIO_InitStructure.GPIO_Pin =  GREEN_LED_Pin  ;	// Setup vdd2 enable pin
	RCC_AHBPeriphClockCmd(GREEN_LED_RCC_AHBPeriph,ENABLE); //enable the ahb peripheral clock for this pin
 	GPIO_Init( GREEN_LED_Port, &GPIO_InitStructure );    //inititalize the GPIO pin
	
	//	
	 	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
   GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_NOPULL;//GPIO_PuPd_DOWN;
			GPIO_InitStructure.GPIO_Pin =  BLUE_LED_Pin  ;	// Setup vdd2 enable pin
	RCC_AHBPeriphClockCmd(BLUE_LED_RCC_AHBPeriph,ENABLE); //enable the ahb peripheral clock for this pin
 	GPIO_Init( BLUE_LED_Port, &GPIO_InitStructure );    //ini
	
		 	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
   GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_NOPULL;//GPIO_PuPd_DOWN;
			GPIO_InitStructure.GPIO_Pin =  ORANGE_LED_Pin  ;	// Setup vdd2 enable pin
	RCC_AHBPeriphClockCmd(ORANGE_LED_RCC_AHBPeriph,ENABLE); //enable the ahb peripheral clock for this pin
 	GPIO_Init( ORANGE_LED_Port, &GPIO_InitStructure );    //ini
	
	
	
		 	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
   GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_NOPULL;//GPIO_PuPd_DOWN;
			GPIO_InitStructure.GPIO_Pin =  RED2_LED_Pin  ;	// Setup vdd2 enable pin
	RCC_AHBPeriphClockCmd(RED2_LED_RCC_AHBPeriph,ENABLE); //enable the ahb peripheral clock for this pin
 	GPIO_Init( RED2_LED_Port, &GPIO_InitStructure );    //ini
	
 	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
   GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_NOPULL;//GPIO_PuPd_DOWN;
			GPIO_InitStructure.GPIO_Pin =  GREEN2_LED_Pin  ;	// Setup vdd2 enable pin
	RCC_AHBPeriphClockCmd(GREEN2_LED_RCC_AHBPeriph,ENABLE); //enable the ahb peripheral clock for this pin
 	GPIO_Init( GREEN2_LED_Port, &GPIO_InitStructure );    //inititalize the GPIO pin
	
	//	
	

	
	
	 	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
   GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_NOPULL;//GPIO_PuPd_DOWN;
			GPIO_InitStructure.GPIO_Pin =  BLUE2_LED_Pin  ;	// Setup vdd2 enable pin
	RCC_AHBPeriphClockCmd(BLUE2_LED_RCC_AHBPeriph,ENABLE); //enable the ahb peripheral clock for this pin
 	GPIO_Init( BLUE2_LED_Port, &GPIO_InitStructure );    //ini
	
		 	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
   GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_NOPULL;//GPIO_PuPd_DOWN;
			GPIO_InitStructure.GPIO_Pin =  ORANGE2_LED_Pin  ;	// Setup vdd2 enable pin
	RCC_AHBPeriphClockCmd(ORANGE2_LED_RCC_AHBPeriph,ENABLE); //enable the ahb peripheral clock for this pin
 	GPIO_Init( ORANGE2_LED_Port, &GPIO_InitStructure );    //ini
	

 //GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_UP;//GPIO_PuPd_DOWN;
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStructure.GPIO_Pin = Buzzer_Pin;  // Setup this pin
	RCC_AHBPeriphClockCmd(Buzzer_RCC_AHBPeriph, ENABLE); //enable the ahb peripheral clock for this pin
	GPIO_Init(Buzzer_Port, &GPIO_InitStructure); //inititalize the GPIO pin

	///setup GPIO for selection the bideirectional octal buffer direction /////////////////////////
	//	GPIO_InitStructure.GPIO_Pin =  Buffer_Dir_Pin ;	// Setup this pin
	//	RCC_AHBPeriphClockCmd(Buffer_Dir_RCC_AHBPeriph,ENABLE); //enable the ahb peripheral clock for this pin
	// 	GPIO_Init( Buffer_Dir_Port, &GPIO_InitStructure ); //inititalize the GPIO pin
	//	




	//////////////////////////////////////////////////////////////////////////////	
	/////////////SETUP INPUT PINS USED///////////////////////
	/////////////////////////////////////////////////////////
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN; //set the pin function to input for the remaining pins 
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP;//GPIO_PuPd_DOWN;
												//GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_NOPULL;//GPIO_PuPd_DOWN;
												//template
												//GPIO_InitStructure.GPIO_Pin =  Relay_Single24_Pin ;	// Setup this pin
												//RCC_AHBPeriphClockCmd(Relay_Single24_RCC_AHBPeriph,ENABLE); //enable the ahb peripheral clock for this pin
												//GPIO_Init( Relay_Single24_Port, &GPIO_InitStructure ); //inititalize the GPIO pin

	
	
	//setup mode engaged to know when we are in our boards control mode
//	GPIO_InitStructure.GPIO_Pin = ModeEngaged_Pin;  // Setup this pin
//	RCC_AHBPeriphClockCmd(ModeEngaged_RCC_AHBPeriph, ENABLE); //enable the ahb peripheral clock for this pin
//	GPIO_Init(ModeEngaged_Port, &GPIO_InitStructure); //inititalize the GPIO pin

GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;//GPIO_PuPd_DOWN;
	GPIO_InitStructure.GPIO_Pin = DFU_Btn_Pin;  // Setup this pin
	RCC_AHBPeriphClockCmd(DFU_Btn_RCC_AHBPeriph, ENABLE); //enable the ahb peripheral clock for this pin
	GPIO_Init(DFU_Btn_Port, &GPIO_InitStructure); //inititalize the GPIO pin


	//GPIO_InitStructure.GPIO_Pin =  Bus_MuxEn_Pin ;	// Setup this pin
	//	RCC_AHBPeriphClockCmd(Bus_MuxEn_RCC_AHBPeriph,ENABLE); //enable the ahb peripheral clock for this pin
	// 	GPIO_Init( Bus_MuxEn_Port, &GPIO_InitStructure ); //inititalize the GPIO pin



//	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP;//GPIO_PuPd_DOWN;//GPIO_PuPd_UP;
//	GPIO_InitStructure.GPIO_Pin = Bus_A0_Pin | Bus_A1_Pin | Bus_A2_Pin | Bus_A3_Pin;    // Setup this pin
//	RCC_AHBPeriphClockCmd(Bus_Address_RCC_AHBPeriph, ENABLE); //enable the ahb peripheral clock for this pin
//	GPIO_Init(Bus_Address_Port, &GPIO_InitStructure); //inititalize the GPIO pin




	/*

	*/
	/////SET UP INTERRUPT PINS USED////////

	/* stm32 uses 4 bits to store preemption and sub priorities, the high bits are for preemption and low bits are for sub priority. 
	If the parameter for priority is 0 for the function	above(that�s also what I had in the function), 0 is 0x00 in hex and 0000 in binary,
	since the default priority grouping for stm32 is group 2, which is 2 bits for preemption	priority and 2 bits for sub priority, 
	we get 00 for preemption and 00 for sub. If we change the input from 0 to 7 for the function, the binary form for 7 is 0111, so higher 2 bits is
	01 which is 1 in decimal gives you preemption priority as 1, and the lower 2 bits is 11 which is 3 gives you sub priority as 3. */

	RCC_APB2PeriphClockCmd(RCC_APB2Periph_SYSCFG, ENABLE); //enable sysconfig before using the interrupt as we have to enable the source via sysconfig registers

//	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP;//GPIO_PuPd_DOWN;
//	GPIO_InitStructure.GPIO_Pin = Bus_IdentEn_Pin;  // Setup this pin
//	RCC_AHBPeriphClockCmd(Bus_IdentEn_RCC_AHBPeriph, ENABLE); //enable the ahb peripheral clock for this pin
//	GPIO_Init(Bus_IdentEn_Port, &GPIO_InitStructure); //inititalize the GPIO pin

	//use the below block only if we are using ident enable interrupt

//# ifdef USEIDENT_INT   //define this later

//	SYSCFG_EXTILineConfig(Bus_IdentEn_EXTI_PORT_SOURCE, Bus_IdentEn_EXTI_PIN_SOURCE);
//	EXTI_InitStructure.EXTI_Mode = EXTI_Mode_Interrupt;
//	EXTI_InitStructure.EXTI_Line = Bus_IdentEn_EXTI_LINE;
//	EXTI_InitStructure.EXTI_Trigger = EXTI_Trigger_Rising_Falling; //detect both state change, so we can set and clear the ident code
//	EXTI_InitStructure.EXTI_LineCmd = ENABLE;
//	EXTI_Init(&EXTI_InitStructure);
//	/* Enable the EXTI3 Interrupt */
//	NVIC_InitStructure.NVIC_IRQChannel = Bus_IdentEn_EXTI_IRQn;
//	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;
//	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;
//	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
//	NVIC_Init(&NVIC_InitStructure);
//#endif

	
	//setup demod monitor pin for interrupt when counting frequency
//	GPIO_InitStructure.GPIO_Pin = Demod_Monitor_Pin;    // Setup this pin
//	RCC_AHBPeriphClockCmd(Demod_Monitor_RCC_AHBPeriph, ENABLE); //enable the ahb peripheral clock for this pin
//	GPIO_Init(Demod_Monitor_Port, &GPIO_InitStructure); //inititalize the GPIO pin

//	SYSCFG_EXTILineConfig(Demod_Monitor_EXTI_PORT_SOURCE, Demod_Monitor_EXTI_PIN_SOURCE);
//	EXTI_InitStructure.EXTI_Mode = EXTI_Mode_Interrupt;
//	EXTI_InitStructure.EXTI_Line = Demod_Monitor_EXTI_LINE;
//	EXTI_InitStructure.EXTI_Trigger = EXTI_Trigger_Rising;//EXTI_Trigger_Rising_Falling; //we need to detect both falling and rising edge on the deomod monitor line
//	EXTI_InitStructure.EXTI_LineCmd = ENABLE;
//	EXTI_Init(&EXTI_InitStructure);
//	/* Enable the EXTI3 Interrupt */
//	NVIC_InitStructure.NVIC_IRQChannel = Demod_Monitor_EXTI_IRQn;
//	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 2;
//	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 2;
//	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
//	NVIC_Init(&NVIC_InitStructure);



}

ErrorStatus CompareString( char* char1,  char* char2, unsigned int count)
{
	static unsigned int i = 0;
	for (i = 0; (i <= count - 1); i++) //do loop while i is not zero and is less than count
	{
		if (*(char1 + i) == *(char2 + i))
		{
			continue; //continue loop if the same
		}
		else
		{
			return ERROR; //return error if not the same
		}

	}

	return SUCCESS;
}

//if a zero count is passed
ErrorStatus CopyString( char* charfrom,  char* charto, unsigned int count)
{
	static unsigned int i = 0;
		if (count > 0)
	{
	for (i = 0; (i <= count - 1); i++) //do loop while i is not zero and is less than count
	{

		charto[i] = charfrom[i];
	}
}
	else
	{
		return ERROR;
	}
	return SUCCESS;
}


void SetSystemDateTime(uint8_t * DateBuf)
{
	//RTC_DateTimeTypeDef RTC_DateTimeStructure;
	//RTC_TimeTypeDef RTC_TimeStructure;	
	
     // Allow access to RTC //
  PWR_BackupAccessCmd(ENABLE);

	SystemDateTimeStructure.RTC_WeekDay = DateBuf[3];
	SystemDateTimeStructure.RTC_Date = DateBuf[4];
  SystemDateTimeStructure.RTC_Month = DateBuf[5]; //This parameter must be set to a value in the 1-31 range. */
  SystemDateTimeStructure.RTC_Year = DateBuf[6] ; //This parameter must be set to a value in the 0-99 range.
	
		
 // RTC_SetDate(RTC_Format_BIN, &RTC_DateStructure);
 
  SystemDateTimeStructure.RTC_Hours   = DateBuf[8] ;
  SystemDateTimeStructure.RTC_Minutes = DateBuf[9] ;
  SystemDateTimeStructure.RTC_Seconds = DateBuf[10] ; 
  SystemDateTimeStructure.RTC_H12     = RTC_H12_AM;
	
	//add one hour for summer time
	//SystemDateTimeStructure = RTC_GetDateTimeOffset(SystemDateTimeStructure, 3600) ;//offset time by one hour
	
	RTC_SetDateTime(RTC_Format_BIN, &SystemDateTimeStructure);    
  
	RTC_WriteBackupRegister(RTC_BKP_DR8, 0x0000); //indicate that the time and date have been set
	
//	WriteLogFile("Date and time Changed. . . . ");
				  // disable access to RTC 
  PWR_BackupAccessCmd(DISABLE);
	
	
	
	return;
}	

