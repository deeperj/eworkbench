/**
  ******************************************************************************
  * @file    SysTick_Example/stm32f30x_it.c 
  * @author  MCD Application Team
  * @version V1.1.0
  * @date    20-September-2012
  * @brief   Main Interrupt Service Routines.
  *          This file provides template for all exceptions handler and 
  *          peripherals interrupt service routine.
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; COPYRIGHT 2012 STMicroelectronics</center></h2>
  *
  * Licensed under MCD-ST Liberty SW License Agreement V2, (the "License");
  * You may not use this file except in compliance with the License.
  * You may obtain a copy of the License at:
  *
  *        http://www.st.com/software_license_agreement_liberty_v2
  *
  * Unless required by applicable law or agreed to in writing, software 
  * distributed under the License is distributed on an "AS IS" BASIS, 
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
  *
  ******************************************************************************
  */

/* Includes ------------------------------------------------------------------*/

#include "stm32f30x_it.h"
#include "main.h"
#include "stm32f30x.h"
#include "usb_lib.h"
#include "usb_conf.h"
#include "usb_pwr.h"

/** @addtogroup STM32F3_Discovery_Peripheral_Examples
  * @{
  */

/** @addtogroup SysTick_Example
  * @{
  */

/* Private typedef -----------------------------------------------------------*/
/* Private define ------------------------------------------------------------*/
/* Private macro -------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/
/* Private function prototypes -----------------------------------------------*/
//extern __IO uint8_t DataReady;
//volatile int8_t FactorPlus = -10; //this is the factor used to compensate for the unequal duty cycle as a result of the camparator in-nuilt hysterisis
//volatile int8_t FactorMinus = -14; 
volatile int8_t SubFactor = 0; 
extern char MessageReportStringBuff[]; //size limited by max buffer size for our usb


volatile uint8_t * DiagTXPointer ;  //this is used to point to the location to read diagnostic data from and transmit to the host
volatile uint8_t DiagRxByteCount; //the counter for transmit or receive of diagnostic data
volatile uint8_t DiagTxByteCount; //the counter for transmit or receive of diagnostic data
volatile uint8_t DiagCRC ; //thi sis used to hold the crc we calculated ourselves
volatile uint8_t DiagCRC_alpha ;
volatile uint8_t  RcvdCRC ; //thi is the crc we received fro the control system
volatile uint8_t TotalDiagRxBytes ; //specifies the total number of bytes expected to be received
volatile uint8_t TotalDiagTxBytes;  //specifies the total number of bytes expected to be transmited

volatile uint32_t EventAddress = 0 ; //temporearily holds the ddwg event address before it it properly stored on nvram and eeprom
volatile uint32_t EventCount = 0 ; //temporearily holds the ddwg event address before it it properly stored on nvram and eeprom

//extern char SIM800_UsartReceiveObject[] ;
//extern uint32_t ESP8266_ReceiveCounter  ;
//volatile HCU_DatatType HCU_Data;

volatile uint8_t SaveIndex = 0 ;
//	volatile uint8_t Saves[300];
	
//volatile bool  IN_RF_RECEIVE =FALSE;

uint8_t intcount = 0;
volatile uint32_t MsSkip = 0;
volatile uint32_t SecSkip = 0;
// uint8_t	addressee ;



extern void  TimingDelay_Decrement(void );
//extern void LCD_DMA_TX_Complete(void); //this function is defines in the LCD driver //this enable the deselection of LCD spi
extern void Delay(volatile uint32_t nTime);
//extern void LDC_DMA_IT_Handler(void );  //this calls the end of dma transfer routine for the LCD
volatile uint32_t CycleCount;	
/* Private functions ---------------------------------------------------------*/
extern __IO uint32_t us_Decrement ;

volatile uint32_t Stack = 0;
/******************************************************************************/
/*            Cortex-M4 Processor Exceptions Handlers                         */
/******************************************************************************/

/**
  * @brief  This function handles NMI exception.
  * @param  None
  * @retval None
  */
void NMI_Handler(void)
{
	  while (1)
  {
  }
}

/**
  * @brief  This function handles Hard Fault exception.
  * @param  None
  * @retval None
  */
void HardFault_Handler(void)
{	
uint32_t MessageID,StringCount;
uint8_t wd = 0;
	uint32_t TempAddress = 0 ;
uint8_t ExcType ,TempType ; 
__ASM{nop};	
	 ReloadWatchdogCounter();
//do some housekeeping here	
ExcType = 2 ; // this tells the type of exception	
	TempType = 0;
	//log this in the error register
	ErrorStatusBits1.Hard_falt_Exception = TRUE;
	UpdateErrorStatus(); //wwe have to update this as we will be restarting the system subsequently
	

	
sprintf(MessageReportStringBuff, "Entered the HARD FAULT interrupt handler\r\n" );
SendControlMessageReportIN(MessageID, 0 ,MessageReportStringBuff);	
	//get the stack pointer address
	Stack = __get_MSP() ;
//log the location where the watchdog was triggered	
	//first check if this has recently occured
	//read the current index from eep_WWDG_Stack_base_41B
//	Read_24Cxx( eep_ADC_SIG_MIDDLE_2B , (uint8_t *) &ADC_SIG_MIDDLE, 2 );
EventAddress = *(uint32_t *)(Stack + (WWDG_STACK_OFFSET * 4 ));  //get the wwdg event address
	
 ReloadWatchdogCounter();	


//write the stack pointer and related addresses to log file
	//first generate the file name		
	StringCount = sprintf((char *)MessageReportStringBuff,"LOC 0x");
		
		//insert the date
		StringCount +=	sprintf((char *)&MessageReportStringBuff[StringCount],"%s",itoha( *(uint32_t *)(Stack + (6*4))));  //first address on stack
	
	StringCount += sprintf((char *)&MessageReportStringBuff[StringCount]," 0x");
	
	StringCount +=	sprintf((char *)&MessageReportStringBuff[StringCount],"%s",itoha( *(uint32_t *)(Stack + (7*4)))); //second address on stack
	
		StringCount += sprintf((char *)&MessageReportStringBuff[StringCount]," 0x");
	StringCount +=	sprintf((char *)&MessageReportStringBuff[StringCount],"%s",itoha( *(uint32_t *)(Stack + (8*4))));//third address on stack
	
		StringCount += sprintf((char *)&MessageReportStringBuff[StringCount]," 0x");
	StringCount +=	sprintf((char *)&MessageReportStringBuff[StringCount],"%s",itoha( *(uint32_t *)(Stack + (9*4))));; //fouth address on stack
	
			StringCount += sprintf((char *)&MessageReportStringBuff[StringCount]," 0x");
	StringCount +=	sprintf((char *)&MessageReportStringBuff[StringCount],"%s",itoha( *(uint32_t *)(Stack + (10*4))));; //fouth address on stack
		
		StringCount += sprintf((char *)&MessageReportStringBuff[StringCount]," 0x");
	StringCount +=	sprintf((char *)&MessageReportStringBuff[StringCount],"%s",itoha( *(uint32_t *)(Stack + (11*4))));; //fouth address on stack
//terminate with zero so writelog detects the end

//USART_Send_String ( &DEBUG_USART_Config ,(char *)MessageReportStringBuff );	
//WriteLogFile(MessageReportStringBuff);

	//get the current address count from the location base
//Read_24Cxx(eep_WWDG_Stack_base_41B, (uint8_t *)&EventCount, 1) ;//&

//if the cout is not zero so there is already a record
if((EventCount > 0) && (EventCount <= TOTAL_WWDG_RECORD))
{
//look at the addresses stored for a possible repeat occurence
	for (wd = 0 ; wd <= EventCount -1 ; wd++)
	{//*5 as each record is 5 bytes first byte is exception type and the last 4 bytes are address where it occured
		//+2 is so we skip over the type byte and the initial counter byte
		
//		Read_24Cxx(eep_WWDG_Stack_base_41B + (wd *5) + 2 , (uint8_t *)&TempAddress  , 4);
		//if there is a match
		if (EventAddress ==  TempAddress)
		{
			//check if the exception type is alsop the same
///			Read_24Cxx(eep_WWDG_Stack_base_41B + (wd *5) + 1 , &TempType  , 1);
			if( ExcType== TempType )
			{
				break; //exit the for loop
			}
			//no need to overwrite just save to nvram and move on
			
		}
	}
}	
//	if no match was found at the endo of the search or there was no seach at all then the next if will be true
if((EventAddress !=  TempAddress) &&( ExcType != TempType)) 
{
	//chec if we still have room for more else reuse the last location 
	if((EventCount >= TOTAL_WWDG_RECORD) && (TOTAL_WWDG_RECORD > 0)) //make sure we dont enter if they are both zero so we make sure at lease one is not zer
	{
		EventCount--; //reduce the count so we resave on the last location
		//raise an error flag for this situation
	//log this in the error register
	ErrorStatusBits1.WatchDog_Address_List_Full = TRUE;
	UpdateErrorStatus(); //wwe have to update this as we will be restarting the system subsequently
	}
	//write exception byte to eeprom
//	MultiWrite_24Cxx( eep_WWDG_Stack_base_41B +((EventCount) *5)+1 , &ExcType, 1 );
//	//write the address bytes to eeprom
//	MultiWrite_24Cxx( eep_WWDG_Stack_base_41B +((EventCount) *5)+2 , (uint8_t *) &EventAddress, 4 );
//	//update the event counts
//	Write_24Cxx( eep_WWDG_Stack_base_41B ,  EventCount+1);
}

//reagardless of match found or not we need to store the location of the latest occcurence on nvram	
//store that location on nvram
PWR_BackupAccessCmd(ENABLE);
	//cast the location to 32 and dereference it
RTC_WriteBackupRegister(NVR_HARDFAULT_ADDRESS, EventAddress); //six steps of 32 bit so 6 * 4 bytes
PWR_BackupAccessCmd(DISABLE);


  /* Go to infinite loop when Hard Fault exception occurs */

__ASM{nop};
 while (1); //wait here till reset occurs
	
	

}

/**
  * @brief  This function handles Memory Manage exception.
  * @param  None
  * @retval None
  */
void MemManage_Handler(void)
{
  /* Go to infinite loop when Memory Manage exception occurs */
  while (1)
  {
  }
}

/**
  * @brief  This function handles Bus Fault exception.
  * @param  None
  * @retval None
  */
void BusFault_Handler(void)
{
  /* Go to infinite loop when Bus Fault exception occurs */
  while (1)
  {
  }
}

/**
  * @brief  This function handles Usage Fault exception.
  * @param  None
  * @retval None
  */
void UsageFault_Handler(void)
{
  /* Go to infinite loop when Usage Fault exception occurs */
  while (1)
  {
  }
}

/**
  * @brief  This function handles SVCall exception.
  * @param  None
  * @retval None
  */
void SVC_Handler(void)
{
}

/**
  * @brief  This function handles Debug Monitor exception.
  * @param  None
  * @retval None
  */
void DebugMon_Handler(void)
{
}

/**
  * @brief  This function handles PendSVC exception.
  * @param  None
  * @retval None
  */
void PendSV_Handler(void)
{
}

/**
  * @brief  This function handles SysTick Handler.
  * @param  None
  * @retval None
  */
void SysTick_Handler(void)
{
SystickCount_us ++;

}
////
////
/******************************************************************************/
/*                 STM32F30x Peripherals Interrupt Handlers                   */
/*  Add here the Interrupt Handler for the used peripheral(s) (PPP), for the  */
/*  available peripheral interrupt handler's name please refer to the startup */
/*  file (startup_stm32f30x.s).                                            */
/******************************************************************************/

/**
  * @brief  This function handles DMA1 Channel 1 interrupt request.
  * @param  None
  * @retval None
  */
void DMA1_Channel3_IRQHandler(void)
{

		DMA_ClearITPendingBit(DMA1_Channel3_IRQn);
}

/**
  * @brief  This function handles DMA1 Channel 1 interrupt request.
  * @param  None
  * @retval None
  */
void DMA1_Channel5_IRQHandler(void)
{

	DMA_ClearITPendingBit(DMA1_Channel5_IRQn);
}

void DMA1_Channel6_IRQHandler(void)
{

		DMA_ClearITPendingBit(DMA1_Channel6_IRQn);
}
/**
  * @brief  This function handles DMA1 Channel 1 interrupt request.
  * @param  None
  * @retval None
  */
void DMA2_Channel2_IRQHandler(void)
{

		DMA_ClearITPendingBit(DMA1_Channel2_IRQn);
}


/**
  * @brief  This function handles SPI1 1 interrupt request.
  * @param  None
  * @retval None
  */
void SPI1_IRQHandler (void)
{
	//test to know the particular interrupt that occurred in this case RXNE
 // if (SPI_I2S_GetITStatus(SPI1, SPI_I2S_IT_RXNE) == SET)
  //{
  // LCD_DMA_TX_Complete(); // DeSelect LCD Slave Select after the DMA transfer completes 
__ASM{nop};
	//SPI_I2S_ReceiveData16(SPI1); //Do a dummy read to clear the RXNE complete flag.		
  //}
}

/*******************************************************************************
* Function Name  : WWDG_IRQHandler
* Description    : This function handles the Window Watchdog Early Wakeup Interrupt EWI.
* Input          : None
* Output         : None
* Return         : None
*******************************************************************************/
void WWDG_IRQHandler(void)
{
	uint32_t MessageID;
uint8_t wd = 0;
	uint32_t TempAddress = 0 ;
uint8_t ExcType ,TempType ; 	
	 ReloadWatchdogCounter();
		//USART_Send_String ( &DEBUG_USART_Config ,"USART1 Buffer overflow problem occurring . . .\r\n" );
//do some housekeeping here	
ExcType = 1 ; // this tells the type of exception	
	TempType = 0;
	//log this in the error register
	ErrorStatusBits1.WatchdogTimerOverflow = TRUE;
	UpdateErrorStatus(); //wwe have to update this as we will be restarting the system subsequently
	
	//get the stack pointer address
	Stack = __get_MSP() ;
//log the location where the watchdog was triggered	
	//first check if this has recently occured
	//read the current index from eep_WWDG_Stack_base_41B
//	Read_24Cxx( eep_ADC_SIG_MIDDLE_2B , (uint8_t *) &ADC_SIG_MIDDLE, 2 );
EventAddress = *(uint32_t *)(Stack + (WWDG_STACK_OFFSET * 4 ));  //get the wwdg event address
	
 ReloadWatchdogCounter();	


//WriteLogFile("Entered the WWDG EWI interrupt routine");
sprintf(MessageReportStringBuff, "Entered the WWDG EWI interrupt routine \r\n" );
SendControlMessageReportIN(MessageID, 0 ,MessageReportStringBuff);

//if the cout is not zero so there is already a record
if((EventCount > 0) && (EventCount <= TOTAL_WWDG_RECORD))
{
//look at the addresses stored for a possible repeat occurence
	for (wd = 0 ; wd <= EventCount -1 ; wd++)
	{//*5 as each record is 5 bytes first byte is exception type and the last 4 bytes are address where it occured
		//+2 is so we skip over the type byte and the initial counter byte
		
//		Read_24Cxx(eep_WWDG_Stack_base_41B + (wd *5) + 2 , (uint8_t *)&TempAddress  , 4);
		//if there is a match
		if (EventAddress ==  TempAddress)
		{
			//check if the exception type is alsop the same
//			Read_24Cxx(eep_WWDG_Stack_base_41B + (wd *5) + 1 , &TempType  , 1);
			if( ExcType== TempType )
			{
				break; //exit the for loop
			}
			//no need to overwrite just save to nvram and move on
			
		}
	}
}	
//	if no match was found at the endo of the search or there was no seach at all then the next if will be true
if((EventAddress !=  TempAddress) &&( ExcType != TempType)) 
{
	//chec if we still have room for more else reuse the last location 
	if((EventCount >= TOTAL_WWDG_RECORD) && (TOTAL_WWDG_RECORD > 0)) //make sure we dont enter if they are both zero so we make sure at lease one is not zer
	{
		EventCount--; //reduce the count so we resave on the last location
		//raise an error flag for this situation
	//log this in the error register
	ErrorStatusBits1.WatchDog_Address_List_Full = TRUE;
	UpdateErrorStatus(); //wwe have to update this as we will be restarting the system subsequently
	}
	//write exception byte to eeprom
//	MultiWrite_24Cxx( eep_WWDG_Stack_base_41B +((EventCount) *5)+1 , &ExcType, 1 );
	//write the address bytes to eeprom
//	MultiWrite_24Cxx( eep_WWDG_Stack_base_41B +((EventCount) *5)+2 , (uint8_t *) &EventAddress, 4 );
	//update the event counts
//	Write_24Cxx( eep_WWDG_Stack_base_41B ,  EventCount+1);
}

//reagardless of match found or not we need to store the location of the latest occcurence on nvram	
//store that location on nvram
PWR_BackupAccessCmd(ENABLE);
	//cast the location to 32 and dereference it
RTC_WriteBackupRegister(NVR_WWDT_ADDRESS, EventAddress); //six steps of 32 bit so 6 * 4 bytes
PWR_BackupAccessCmd(DISABLE);



__ASM{nop};
 while (1); //wait here till reset occurs
}




void USART1_IRQHandler(void)
{
	ReloadWatchdogCounter();
	
	if((USART_GetITStatus(USART1,USART_IT_TXE) == SET) || (USART_GetITStatus(USART1,USART_IT_TC) == SET) || (USART_GetITStatus(USART1,USART_IT_RXNE) == SET) )
	{
		while (USART_GetITStatus(USART1,USART_IT_TXE) == SET) 
		{
		//USART_Receive_Data(USART1);	

		USART_ClearITPendingBit(USART1,  USART_IT_TXE);// clear interrupt
			 // disable TX interrupt if nothing to send
		}
		
		while (USART_GetITStatus(USART1,USART_IT_TC) == SET)
		{
		//USART_Receive_Data(USART1);	
		USART_ClearITPendingBit(USART1,  USART_IT_TC);// clear interrupt

		}
		//use a while loop to handle all the characters received before leaving the interrupt	
		while(USART_GetITStatus(USART1,USART_IT_RXNE) == SET)  
		{
			//clear the flag before ahndling the data so that in return we can handle the next one
		//NOTE!! 	RXNE pending bit is cleared by a read to the USART_RDR register 
		USART_ClearITPendingBit(USART1,  USART_IT_RXNE);// clear interrupt	
		#ifdef _ESP8266_H
			USART_Receive_Data(&ESP8266_USART_Config);
		#endif //_ESP8266_H

		}
	}
	else
	{
		//usart buffer overflow
		USART_Send_String ( &DEBUG_USART_Config ,"USART1 Buffer overflow problem occurring . . .\r\n" );	
	__asm{ nop};
		__asm{ nop};
	}
}
void USART2_IRQHandler(void)
{
		 ReloadWatchdogCounter();
	if((USART_GetITStatus(USART2,USART_IT_TXE) == SET) || (USART_GetITStatus(USART2,USART_IT_TC) == SET) || (USART_GetITStatus(USART2,USART_IT_RXNE) == SET) )
	{
		while (USART_GetITStatus(USART2,USART_IT_TXE) != RESET) 
	{
	USART_ClearITPendingBit(USART2,  USART_IT_TXE);// clear interrupt	
	//USART_Receive_Data(USART2);	
	}
	
	
	while (USART_GetITStatus(USART2,USART_IT_TC) != RESET)
	{
	USART_ClearITPendingBit(USART2,  USART_IT_TC);// clear interrupt	
	//USART_Receive_Data(USART2);	
	}
	//use a while loop to handle all the characters received before leaving the interrupt	
	while (USART_GetITStatus(USART2,USART_IT_RXNE) != RESET)  
	{		
			//clear the flag before handling the data so that in return we can handle the next one
		//NOTE!! 	RXNE pending bit is cleared by a read to the USART_RDR register 
	USART_ClearITPendingBit(USART2,  USART_IT_RXNE);// clear interrupt	
	//USART_Receive_Data(USART2);	
		
	//	#ifdef _ESP8266_H
			USART_Receive_Data(&DEBUG_USART_Config);
	//	#endif //_ESP8266_H	
	}
	}
	else
	{
		//usart buffer overflow
		USART_Send_String ( &DEBUG_USART_Config ,"USART2 Buffer overflow problem occurring . . .\r\n" );	
	__asm{ nop};
		__asm{ nop};
	}
	
	
}
void USART3_IRQHandler(void)
{
			 ReloadWatchdogCounter();
	if((USART_GetITStatus(USART3,USART_IT_TXE) == SET) || (USART_GetITStatus(USART3,USART_IT_TC) == SET) || (USART_GetITStatus(USART3,USART_IT_RXNE) == SET) )
	{
		while (USART_GetITStatus(USART3,USART_IT_TXE) != RESET) 
		{
		USART_ClearITPendingBit(USART3,  USART_IT_TXE);// clear interrupt	
			//USART_Receive_Data(USART3);	
		// disable TX interrupt if nothing to send
		}
			
		while (USART_GetITStatus(USART3,USART_IT_TC) != RESET)
		{
		USART_ClearITPendingBit(USART3,  USART_IT_TC);// clear interrupt	
		//USART_Receive_Data(USART3);	
		}
		
		//use a while loop to handle all the characters received before leaving the interrupt
		while (USART_GetITStatus(USART3,USART_IT_RXNE) != RESET)  
		{
		//clear the flag before ahndling the data so that in return we can handle the next one
	USART_ClearITPendingBit(USART3,  USART_IT_RXNE);// clear interrupt	
	//USART_Receive_Data(USART3);	
	}
	}
	else
	{
		//usart buffer overflow
		USART_Send_String ( &DEBUG_USART_Config ,"USART3 Buffer overflow problem occurring . . .\r\n" );	
	__asm{ nop};
		__asm{ nop};
	}
	
}
  

void USB_LP_CAN1_RX0_IRQHandler(void)
{
   USB_Istr();
}

void EXTI15_10_IRQHandler(void)
{

}
void EXTI9_5_IRQHandler(void)
{
	#ifdef _RFOOK_H
	//check if it is interrupt request for Accelerometer
	if (EXTI_GetITStatus(RF_OOK_RX_EXTI_LINE) != RESET)
	{
//		Delay_us(50);
		if((RF_OOK_RX_GPIO_PORT->IDR & RF_OOK_RX_GPIO_PIN)) //if signal is still high 
		{
		GPIO_SetBits(Buzzer_Port,Buzzer_Pin);
//IN_RF_RECEIVE = TRUE ;
		RF_OOK_Receive();
		GPIO_ResetBits(Buzzer_Port,Buzzer_Pin);
//IN_RF_RECEIVE = FALSE ;
		}
		
		EXTI_ClearITPendingBit(RF_OOK_RX_EXTI_LINE);
	}
#endif //_RFOOK_H
	

#ifdef	_CC1100_CC2500_H
///check for rf interrupt occurence/////////////
if (EXTI_GetITStatus(CC2500_IRQ_EXTI_LINE) != RESET)
{
	
	if (INITIALIZATION_COMPLETE == TRUE)
	{
	CC2500Int = TRUE;
	}
	EXTI_ClearITPendingBit(CC2500_IRQ_EXTI_LINE);
}
	
#endif //	_CC1100_CC2500_H
	
#ifdef	RFM69_HPP_
///check for rf interrupt occurence/////////////
if (EXTI_GetITStatus(RFM69_IRQ_EXTI_LINE) != RESET)
{
	
//	if (INITIALIZATION_COMPLETE == TRUE)
//	{
//	//RFM69_receive(cc2500_rx_buffer, dataLength);
//	}
	EXTI_ClearITPendingBit(RFM69_IRQ_EXTI_LINE);
}
	
#endif //	RFM69_HPP_
}
	
	

//interrupt routine for AEN on the bus
void EXTI1_IRQHandler(void)
{
	
}



		

//interrupt routine for ident enable
void EXTI2_TS_IRQHandler(void)
{
	
	#ifdef RFM69_USE_INTERRUPT

	if (EXTI_GetITStatus(RFM69_IRQ_EXTI_LINE) != RESET)
  {
		
			
		EXTI_ClearITPendingBit(RFM69_IRQ_EXTI_LINE);
	}	
		#endif  //RFM69_USE_INTERRUPT

}

void EXTI3_IRQHandler(void)
{

}


void USBWakeUp_IRQHandler(void)
{
  /* Initiate external resume sequence (1 step) */
  Resume(RESUME_EXTERNAL);  
  EXTI_ClearITPendingBit(EXTI_Line18);
}




/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
