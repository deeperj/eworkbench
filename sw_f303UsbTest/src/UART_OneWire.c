/**
  ******************************************************************************
  * @file    UART_OneWire.c
  * @author  Edison O.
  * @version V1.0.0
  * @date    23-August-2013
  * @brief   This file provides firmware functions to read and write to the AD5752 DAC 
  *         
  *         
  @verbatim
  ==============================================================================
                             ##### How to use this driver #####
  ==============================================================================
    
		
  */
#include "UART_OneWire.h"
#include "usb_type.h"


unsigned char OneWireState = ResetDetect;
bool OneWire_Initialized = FALSE;


ErrorStatus OneWireResetDetect()
{
	static unsigned char data = 0;
	
	if (OneWireState == ReadWrite)
	{
		OneWire_Init(ResetDetect);
	}
	else
	{
	//do nothing
	}
//reset and detect a sensor
	//send the reset pulse
	while(USART_GetFlagStatus(Onewire_USARTx, USART_FLAG_TC) == RESET); // Wait for transmit any pending transmission to complete
	//clear received buffer
	//data = USART_ReceiveData(Onewire_USARTx);
	
	USART_RequestCmd(Onewire_USARTx, USART_Request_RXFRQ , ENABLE);  //flush the receive buffer

	
	//send the reset pulse
	USART_SendData(Onewire_USARTx,0xF0);  //send the RESET pulse at 9600 baud
	
	
	while(USART_GetFlagStatus(Onewire_USARTx, USART_FLAG_TXE) == RESET); // Wait for transmission to complete
	
	//wait for reception to complete
while(USART_GetFlagStatus(Onewire_USARTx, USART_FLAG_RXNE) == RESET); // Wait for reception to complete
	//detect a present sensor by reading back
	data = USART_ReceiveData(Onewire_USARTx);
	//compare the two data to know if any sensor responded
	if (0xF0 == data)
	{
		//no sensor was detected exact same data was received
			__ASM{nop};
	return ERROR ; 
	
	}
	else if (data == 0xE0)  //if ((data >= 0x10) && (data <= 0x90) ) //if data recieved is within the range indicating possible detected sensor
		{
					
			//OneWire_Init(ReadWrite);	//return settings to readwrite mode
			
		__ASM{nop};
		return SUCCESS ;
		}
		
	//OneWire_Init(ReadWrite);	//return settings to readwrite mode anyway
	
return ERROR  ;	//i will call this an error because of undefined returned data
}



//Reads an 8-byte page from the device starting at specified address //returns ERROR or SUCCESS
ErrorStatus  OneWireReadMemory(uint8_t *address,uint8_t * data, uint32_t count) 
{	
	static unsigned int i=0;
//	static uint16_t CRCValue; //this holds the crc value 
	
		//do the reset and presence detect sequence again
if (OneWireResetDetect() == SUCCESS )
	{
		//double check to make sure in the right mode
		if (OneWireState != ReadWrite)
		{
			OneWire_Init(ReadWrite);
		}
	
			//specify the device address or skip over(SKIP ROM)	if only one device is connected
		if (SKIPROM == 0)
		{
			//specify and send device rom address
		}
		else
			{
		//issue "skip Rom" command
			OneWire_Write_Char( CommandSkipRom);
			}
			
		//issue "Read Memory" command	to read data from internal storage
		OneWire_Write_Char( CommandReadMemory );
		
		//now loop over to send the targeted memory address			
		for(i=0 ; i<= 1; i++) //loop over to send the address  // in this case, read 0:1 //write 2 bytes
		{
			
		OneWire_Write_Char( *(address+i));
	
		}
		
	//loop over to read the data payload	from the slave	
		for(i=0 ; i<= count-1; i++) //loop over to read the data
		{
			data[i] =	OneWire_Read_Char ();
		}
	}
	
	else
	{
		//initial reset detect failed
		return ERROR; //error sending the reset and detect command.
	}
	//send a reset and presence signal to end the reading process
	if (OneWireResetDetect() != SUCCESS )
{
	return ERROR; //error sending the final reset and detect command. maybe he just died !!!
}
	


return SUCCESS ; //memory Read successful

	
}

//reads the unique rom code from the one wire device if present.
//romcode[0] = 8bit family code //romcode[1:6] =  6-byte unique serial number //romcode[7] = 8bit crc byte
ErrorStatus  OneWireReadROM(uint8_t * romcode)
{
	static unsigned int i=0;
	static uint8_t CRCValue = 0; //this holds the crc value calculated
	
		//do the reset and presence detect sequence again
if (OneWireResetDetect() == SUCCESS )
	{
		//double check to make sure in the right mode
		if (OneWireState != ReadWrite)
		{
			OneWire_Init(ReadWrite);
		}
	
//no need to issue a skip rom command here
			
		//issue "Read ROM" command	to read the unique ID from a single connected slave (works only when there is just one slave connected, else collision occurs)
		OneWire_Write_Char( CommandReadRom  );
		
		
		//now loop over to receive a 64 bit data with the rom code		
		
		//romcode[0] = 8bit family code
		//romcode[1:6] =  6-byte unique serial number
		//romcode[7] = 8bit crc byte
		for(i=0 ; i<= 7; i++) 
		{
			
		romcode[i] =	OneWire_Read_Char (); 
	
		}
	//now we do a CRC-8 Check to verify the rom code data
	
CRCValue = OneWireCRC8 (romcode,7); //calculate the CRC of the bytes received

if (romcode[7] != CRCValue)
	{
	//crc mismatched 
	return ERROR ;
	
	}
		
		
		
	}//end of reset detect IF	
		else
	{
		//initial reset detect failed
		return ERROR; //error sending the reset and detect command.
	}
	//send a reset and presence signal to end the reading process
	if (OneWireResetDetect() != SUCCESS )
{
	return ERROR; //error sending the final reset and detect command. maybe he just died !!!
}
	


return SUCCESS ; //Rom Read successful

}



/*writes an 8-byte page to the device starting at specified address //returns ERROR or SUCCESS
*address: a pointer to a 3 byte array containing the 
[0]target address 1 TA1, 
[1]target address 2 TA2
[2]Ending address with data status(read only)
*Data: a pointer to an 8-byte array containing the data to be transmitted

*/
ErrorStatus  OneWireWritePage(uint8_t *address,uint8_t * data) 
{

	static uint16_t CRCValue; //this holds the crc value 
	static unsigned char AddressVerify[3]; // this stores the addres detailsed read back from the scratchpad  during verification
	
	
	
	if (OneWireScratchpadWrite (address,data, &CRCValue) == ERROR  ) //write data to scratchpad
	{
			return ERROR ; //srite to scratchpad failed
	
	}
	
	//now we readback the scratchpad to verify the data

	if (OneWireScratchpadVerify (address,AddressVerify,data) == ERROR  ) //pass the addressverify arrray to it to be filled up with the third byte
	{
		//verify failed
		return ERROR ; //
	}
			

//what was written has be confirmed crc checking was also dont in the scratchpad write and verify functions	

	
	//before you move on to copy first check the (Autorization Accepted)AA bit of the status ref=gister returedfrom the scratchpad verify
if(AddressVerify[2] & 0x80) //if bit 7 is high then the data in the scratchpad has already been written to the memory so no need issue copy command
			{
				//data in the scratchpad has already been written to the memory
				return SUCCESS  ; //well!! we can call this success, as we dont need to issue copy command.
			}

	
	
//proceed with issueing scratchpad copy command as data integrity is intact

	if (OneWireScratchpadCopy(AddressVerify  ) == ERROR )
	{
			return ERROR ; //encountered a copy scratchpad error
	}

return SUCCESS ; //page write successful

}


ErrorStatus OneWireScratchpadCopy(uint8_t *address)
{
	static uint16_t i = 0;	
//do the reset and detect sequence first	
if (OneWireResetDetect() == SUCCESS )
	{
		//double check to make sure in the right mode
		if (OneWireState != ReadWrite)
		{
			OneWire_Init(ReadWrite);
		}
		//specify the device address or skip over(SKIP ROM)	if only one device is connected
		if (SKIPROM == 0)
			{
				//specify and send device rom address

				
			}
		else
			{
		//issue "skip Rom" command
			OneWire_Write_Char( CommandSkipRom);
			
			}
			
		//issue "Copy Scratchpad" command	
		OneWire_Write_Char( CommandCopyScratchpad  );
			

//now loop over to write the target memory address			
		for(i=0 ; i<= 2; i++) //loop over to send the address  //send 0:2 for copy scratchpad command
		{
			OneWire_Write_Char( *(address+i));
		}

//wait for the copy function to complete
OneWireIdleHigh();

	//	return ERROR; //one wire scraatpad copy error as a result of FF loop possible attempt to write to wrong address

if (OneWireCheckPattern() == ERROR )
{
	return ERROR; //write finish pattern was not detected so ERROR!!!
}

//do the reset and detect sequence to end the copy command and stop the 0 and 1 pattern generation	
if (OneWireResetDetect() != SUCCESS )
{
	return ERROR; //error sending the final reset and detect command. maybe he just died !!!
}
	
return SUCCESS ; //scratchpad copy completed successfully

	}	
else
	{
	return ERROR; //one wire detect failed
	}

	
}

ErrorStatus  OneWireCheckPattern(void)
{
unsigned int i = 20;
do //keep checking for the patterns
{
	if ((OneWire_Read_Char() == 0xAA )  || (OneWire_Read_Char() == 0x55))	//check for patters of 0 and 1
	{
	return SUCCESS ;
	}
Delay_ms (1); //wait for some time	
i--; //reduce i	
} while (i<= 0);
	
return ERROR  ; // the wait timed out therefore the pattern was not detected

}
void OneWireIdleHigh(void)
{//wait for the inernal programming to finish
	Delay_ms (10); ///TProgmMAX is 10 ms according to datasheet.
	
}



ErrorStatus OneWireScratchpadWrite(uint8_t *address,uint8_t * data, uint16_t * CRCval)
{
	static uint16_t CRCcalculated = 0;
static uint16_t i = 0;
static unsigned char CRCpack[11];  //used to pack 8 bytes data + 2 bytes address + 1 byte command
//do the reset and detect sequence first	
	if (OneWireResetDetect() == SUCCESS )
	{
		//double check to make sure in the right mode
		if (OneWireState != ReadWrite)
		{
			OneWire_Init(ReadWrite);
		}
//specify the device address or skip over(SKIP ROM)	if only one device is connected
if (SKIPROM == 0)
{
	//specify and send device rom address

	
}
else
	{
//issue "skip Rom" command
	OneWire_Write_Char( CommandSkipRom);
	
	}
	
//issue "Write Scratchpad" command	
OneWire_Write_Char( CommandWriteScratchpad  );
	

//now loop over to write the target memory address			
		for(i=0 ; i<= 1; i++) //loop over to send the address  //send 0:1 for write and 0:2 for read
		{
			OneWire_Write_Char( *(address+i));
		}
		
//loop over to send the data payload		
		for(i=0 ; i<= 7; i++) //loop over to send the data
		{
			OneWire_Write_Char( *(data+i));
		}

//	
//		GPIO_ResetBits(Output_Enable_Port, Output_Enable_Pin);
//	GPIO_SetBits(Output_Enable_Port, Output_Enable_Pin);
//	GPIO_ResetBits(Output_Enable_Port, Output_Enable_Pin);

//	Delay_ms(10);

//read two bytes of the CRC from the device
		*CRCval = OneWire_Read_Char();  //read the first crc value and write it to the LSB position of the 16 bit variable
		*CRCval |= ( ((uint16_t)OneWire_Read_Char()) << 8);  //read the second crc value  //cast it to 16 bit and then shift it to the MSB position

//pack data for crc check

CRCpack [0] = CommandWriteScratchpad;
CRCpack [1] = address[0] ;
CRCpack [2] = address[1] ;
for (i=0;i<=7;i++)
{
	CRCpack [i+3] = data[i];
}

CRCcalculated = ~(OneWireCRC16(CRCpack , 11));

if( CRCcalculated != *CRCval  )
{
	//crc error
	return ERROR;
}

return SUCCESS ; //scratchpad write successful

}
	else 
	{
		//detect and reset no successful
		return ERROR ;
	}

}


ErrorStatus OneWireScratchpadVerify(uint8_t *address,uint8_t * addressverify,uint8_t * data)
{
	static uint16_t CRCcalculated = 0;
static uint16_t i = 0;
static unsigned char CRCpack[12];  //used to pack 8 bytes data + 3 bytes address + 1 byte command
	static uint16_t CRCValue = 0; //this holds the crc value 
	static unsigned char  addressoffset = 0;
	static unsigned char DataVerify[8];
	//static unsigned char deletelater [2]; //
	//do the reset and presence detect sequence again
if (OneWireResetDetect() == SUCCESS )
	{
		//double check to make sure in the right mode
		if (OneWireState != ReadWrite)
		{
			OneWire_Init(ReadWrite);
		}
	
			//specify the device address or skip over(SKIP ROM)	if only one device is connected
		if (SKIPROM == 0)
		{
			//specify and send device rom address
		}
		else
			{
		//issue "skip Rom" command
			OneWire_Write_Char( CommandSkipRom);
			}
			
		//issue "Read Scratchpad" command	to write the data into the internal storage
		OneWire_Write_Char( CommandReadScratchpad  );
		
		//now loop over to read back the targeted memory address			
		for(i=0 ; i<= 2; i++) //loop over to read the address  // in this case, read 0:2 //read three bytes
		{
		*(addressverify+i) =	OneWire_Read_Char ();
			//deletelater[i] = OneWire_Read_Char ();
		}
		//compare the readback address values  // compare just the first two bytes received
		if ( CompareString ( (char *)addressverify,(char *)address,2) == ERROR ) 
		{
			 
			return ERROR ; //comparison of address failed
		}
		//read the E/S register to verify data integrity
				//compare the returned E/S(ie. addressverify[2] ) [2:0] with the originally specified address[0] bits[2:0] + bytecount. these should be the same
				addressoffset = (0x07 & *(address +0)) + 7 ; //first and the address[0] with a mask to preserve only bits [2:0] 
																									//then add 8(number of bytes sent) to the value to get the offset count. to be used below
			
				if (addressoffset !=	(*(addressverify+2) & 0x07)) //also mask the adressverify[2] to preserve bits[2:0]
				{
					return ERROR ; //comparison of address offset failed
				}
			
			//check the status of bit PF if this is 1 then there is trouble see datasheet page 8 paragraph 5
			
			if(*(addressverify +2) & 0x20) //if bit 5 is high then the datain scratchpad is invalid
			{
				//scratchpad data invalid 
				//either loss of power or inadequate bytes sent to fill the scratchpad (8 bytes required)
				return ERROR ; //invalid scratchpad data
			}
			
		
						
		//loop over to read the data payload	earlier sent	
		for(i=0 ; i<= 7; i++) //loop over to read the data
		{
			DataVerify[i] =	OneWire_Read_Char ();
		}
		//compare the readback data values
		if ( CompareString ( (char *)DataVerify,(char *)data,8) == ERROR ) 
		{
			
			return ERROR ; //comparison of data failed
		}
		
		//read two bytes of the CRC from the device
		CRCValue = OneWire_Read_Char();  //read the first crc value
		CRCValue |= ( ((uint16_t)OneWire_Read_Char()) << 8);  //read the second crc value  //cast it to 16 bit and then shift it to the MSB position
		
		
		//calculate the crc
		//pack data for crc check

CRCpack [0] = CommandReadScratchpad;
CRCpack [1] = addressverify [0] ; //the crc is based on the data returned by the slave, which inclues an extra byte, the E/S register
CRCpack [2] = addressverify[1] ;
CRCpack [3] = addressverify[2] ; //note that 3 address bytes were returned but 2 were sent
		
for (i=0;i<=7;i++)
{
	CRCpack [i+4] = data[i];
}

CRCcalculated = ~(OneWireCRC16(CRCpack , 12));

if( CRCcalculated != CRCValue  )
{
	//crc error
	return ERROR;
}
	

//well! all seems to have gone on successfully
return SUCCESS ;		
		
	
	}		
else
		{
			return ERROR ; //reset and presence detect failed
		}
}


void OneWire_Write_Char(unsigned char data)
{
	unsigned char i= 0;
	
	//first make sure the right state of the uart is in place
	if (OneWireState != ReadWrite)
	{
		OneWire_Init(ReadWrite);
	}
	
	
	//loop to shift out the bits for sending
for (i=0; i<=7;i++)
{
	while(USART_GetFlagStatus(Onewire_USARTx, USART_FLAG_TXE) == RESET); // Wait for transmit to complete	

	if (data & (0x01 << i)) //if this bit position in 1
	{
		USART_SendData(Onewire_USARTx,0xFF); //onewire write 1 time slot

	}
	else
	{
			USART_SendData(Onewire_USARTx,0x00);  //onewire write 0 time slot

	}
}

}

	
	
unsigned char OneWire_Read_Char(void)
{

	
	static unsigned char i= 0;
		static unsigned char recv= 0;
	static 	unsigned char data = 0;
	
//	
//		GPIO_ResetBits(Output_Enable_Port, Output_Enable_Pin);
//	GPIO_SetBits(Output_Enable_Port, Output_Enable_Pin);
//	GPIO_ResetBits(Output_Enable_Port, Output_Enable_Pin);
	
	//first make sure the right state of the uart is in place
	if (OneWireState != ReadWrite)
	{
		OneWire_Init(ReadWrite);
	}
	else; //do nothing else
	


while(USART_GetFlagStatus(Onewire_USARTx, USART_FLAG_TC) == RESET); // Wait for any previous transmission to complete
USART_ClearFlag(Onewire_USARTx, USART_FLAG_ORE) ;//clear any overrun error flagfrom previous transmissions
recv = USART_ReceiveData(Onewire_USARTx); //do a dummy read

//USART_RequestCmd(Onewire_USARTx, USART_Request_RXFRQ , ENABLE);  //flush the receive buffer
//USART_RequestCmd(Onewire_USARTx, USART_Request_TXFRQ , ENABLE);  //flush the transmit buffer

//loop pack received bits
for (i=0; i<=7;i++)
{
 	
while(USART_GetFlagStatus(Onewire_USARTx, USART_FLAG_TC) == RESET);// Wait for transmission to complete
//USART_RequestCmd(Onewire_USARTx, USART_Request_TXFRQ , ENABLE);  //flush the tx buffer	
		//clear received buffer
 //recv = USART_ReceiveData(Onewire_USARTx); //do a dummy read
//USART_RequestCmd(Onewire_USARTx, USART_Request_RXFRQ , ENABLE);  //flush the receive buffer


	USART_SendData(Onewire_USARTx,0xFF); //onewire read time slot

while(USART_GetFlagStatus(Onewire_USARTx, USART_FLAG_TC) == RESET); // Wait for transmission to complete
	
	//wait for reception to complete
while(USART_GetFlagStatus(Onewire_USARTx, USART_FLAG_RXNE) == RESET); // Wait for reception to complete	//read received data
	
//GPIO_ResetBits(Output_Enable_Port, Output_Enable_Pin);
//GPIO_SetBits(Output_Enable_Port, Output_Enable_Pin);

	recv = USART_ReceiveData(Onewire_USARTx);


//Delay_ms(10);

if ( recv <= 0xFE) //if a zero bit was received
{
	data &= ~(0x01 << i); //make the bit position zero using ~ to flip the bits after the shift
}

else if(recv == 0xFF) //if a one bit was received
{
	data |= (0x01 << i);  // make the bit position one
}


}
	return data;
}
	
	




/* 
   get all rom address when multiple slave are connected
   depending on  conditional value, get All the
   slave or just the slave which are in alarm state (cf conditional search)
   it's your responsability to give a pointer on an sufficently large
   array for all the slave, otherwise you will miss some slave.
*/
//uint8_t  oneWireSearchRom (OneWireDriver* drv, bool_t conditional, OneWireRomAddress *addrs, uint8_t len)
//{
	
//}


void OneWire_Init(OwMode mode)
{
  //uint32_t PeriphClock;

  GPIO_InitTypeDef  GPIO_InitStructure;
	USART_InitTypeDef 	USART_InitStructure;
 
 /* --------------------------- System Clocks Configuration -----------------*/
  
	/* USARTx clock enable */
 RCC_APB1PeriphClockCmd(Onewire_Usart_Peripheral_RCC , ENABLE); //specify the uart to use and the APB peripheril it belongs to
  /* GPIOx clock enable */
  RCC_AHBPeriphClockCmd(Onewire_Port_Peripheral_RCC, ENABLE);  //specify the gpio that the serial port selected is located

  /*-------------------------- GPIO Configuration ----------------------------*/
  GPIO_InitStructure.GPIO_Pin = Onewire_txPin;  //| GPIO_Pin_3; //pin A9 is for uart1 tx
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_OD; //GPIO_PuPd_NOPULL  //configure tx pin as open drain instead of push-pull
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP; //see ref. manual section 26.5.12
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_Init(Onewire_txPort, &GPIO_InitStructure);
	
	
	//remove
	//GPIO_PinAFConfig(Onewire_txPort, GPIO_PinSource3 , Onewire_PinAF);
 //remove
 
  /* Connect USART pins to AF */
  GPIO_PinAFConfig(Onewire_txPort, Onewire_PinSource , Onewire_PinAF); // configure alternate function for PA9//AF7 is for the uart, see ref. manual
  //GPIO_PinAFConfig(GPIOA, GPIO_PinSource3, GPIO_AF_7); no need for RX
if (mode == ReadWrite)
{
	//set a different baud rate for normal one wire comms
	 USART_InitStructure.USART_BaudRate = Uart_1wire_Baudrate_ReadWrite;
	 OneWireState = ReadWrite;  //specify the current configured state
}
else if (mode == ResetDetect)
{
	//set a different baud rate for reset and detect pulse mode
	 USART_InitStructure.USART_BaudRate = Uart_1wire_Baudrate_ResetDetect;
	 OneWireState = ResetDetect; //specify the current configured state
}
	else
{
//wrong mode specified
}
 
  USART_InitStructure.USART_WordLength = USART_WordLength_8b;
  USART_InitStructure.USART_StopBits = USART_StopBits_1;
  USART_InitStructure.USART_Parity = USART_Parity_No;
  USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;
  USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx; //  
 
  USART_Init(Onewire_USARTx, &USART_InitStructure);
 
 	USART_HalfDuplexCmd(Onewire_USARTx,ENABLE);  //enable the half duplex mode which connects rx and tx internally together out of tx line
//the above must be done before enabling the usart
 
  USART_Cmd(Onewire_USARTx, ENABLE);
	
    

OneWire_Initialized =  TRUE ;

/////////////////////////////////////////////////////////////////////////////////////////
}




//uint16_t OneWireCRC(unsigned char *ptr,  unsigned int count)
//{
//static unsigned char i;
//static   uint32_t crc = 0x0000; //try this with initial value as  0xffff
//	//try ny initializing with the absolute page number 
//	
//   for (; count>0; count--)  //while (--count >= 0)
//   {
//     crc = crc ^ ((uint32_t) *ptr++ << 8);
//     for (i=0; i<8; i++)
//     {
//       if (crc & 0x8000)
//       {
//         crc = (crc << 1) ^ 0xC001;  //^ 0x1021
//       }
//       else
//       {
//         crc = crc << 1;
//       }
//     }
//   }
//   return crc; //invert the reesult as sepcified by the one wire device
//}


uint16_t OneWireCRC16(unsigned char * input,  unsigned int len)
{
	uint16_t i=0;
    static const uint8_t oddparity[16] ={ 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0 };
    uint16_t crc = 0;    // Starting seed is zero.

    for ( i = 0 ; i < len ; i++) 
				{
      // Even though we're just copying a byte from the input,
      // we'll be doing 16-bit computation with it.
      uint16_t cdata = input[i];
      cdata = (cdata ^ (crc & 0xff)) & 0xff;
      crc >>= 8;

      if (oddparity[cdata & 0x0F] ^ oddparity[cdata >> 4])
			{
          crc ^= 0xC001;
			}
      cdata <<= 6;
      crc ^= cdata;
      cdata <<= 1;
      crc ^= cdata;
    }
    return crc;
}

// Compute a Dallas Semiconductor 8 bit CRC directly.
// this is much slower, but much smaller, than the lookup table.
//
uint8_t OneWireCRC8( uint8_t *addr, uint8_t len)
{
	uint8_t i =0;
	uint8_t crc = 0;

	while (len--) 
		{
		uint8_t inbyte = *addr++;
		for ( i = 8; i; i--) 
			{
			uint8_t mix = (crc ^ inbyte) & 0x01;
			crc >>= 1;
			if (mix)
				{
					crc ^= 0x8C;
				}
			inbyte >>= 1;
			}
		}
	return crc;
}


