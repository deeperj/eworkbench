/**
  ******************************************************************************
  * @file    main.c
  * @author  Ac6
  * @version V1.0
  * @date    01-December-2013
  * @brief   Default main function.
  ******************************************************************************
*/


#include "stm32f30x.h"
#include "stm32f3_discovery.h"
			

void Delay_us(uint32_t count)
{
	int i;
	do
	{
		for (i = 0; i < 3; i++)
		{
			while(0);

			// __ASM{nop};
		}

	} while (--count);

}

void Delay_ms(uint32_t ms)
{
	do
	{
		//ReloadWatchdogCounter();
		Delay_us(1000);

	} while (--ms);

}

int main(void)
{

	STM_EVAL_LEDInit(LED4);
	for(;;){
		STM_EVAL_LEDOn(LED4);
		Delay_ms(1000);
		STM_EVAL_LEDOff(LED4);
	}
}
