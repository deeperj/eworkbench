################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_exti.c \
../Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_gpio.c \
../Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_pwr.c \
../Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_rcc.c \
../Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_utils.c 

OBJS += \
./Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_exti.o \
./Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_gpio.o \
./Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_pwr.o \
./Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_rcc.o \
./Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_utils.o 

C_DEPS += \
./Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_exti.d \
./Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_gpio.d \
./Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_pwr.d \
./Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_rcc.d \
./Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_utils.d 


# Each subdirectory must supply rules for building sources it contributes
Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_exti.o: ../Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_exti.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DSTM32H750xx '-DEXTERNAL_CLOCK_VALUE=12288000' '-DVDD_VALUE=3300' '-DLSI_VALUE=32000' '-DHSI_VALUE=64000000' '-DHSE_VALUE=25000000' '-DHSE_STARTUP_TIMEOUT=100' -DUSE_FULL_LL_DRIVER '-DLSE_STARTUP_TIMEOUT=5000' -DDEBUG '-DLSE_VALUE=32768' -c -I../Core/Inc -I../Drivers/STM32H7xx_HAL_Driver/Inc -I../Drivers/CMSIS/Device/ST/STM32H7xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_exti.d" -MT"$@" --specs=nano.specs -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -o "$@"
Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_gpio.o: ../Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_gpio.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DSTM32H750xx '-DEXTERNAL_CLOCK_VALUE=12288000' '-DVDD_VALUE=3300' '-DLSI_VALUE=32000' '-DHSI_VALUE=64000000' '-DHSE_VALUE=25000000' '-DHSE_STARTUP_TIMEOUT=100' -DUSE_FULL_LL_DRIVER '-DLSE_STARTUP_TIMEOUT=5000' -DDEBUG '-DLSE_VALUE=32768' -c -I../Core/Inc -I../Drivers/STM32H7xx_HAL_Driver/Inc -I../Drivers/CMSIS/Device/ST/STM32H7xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_gpio.d" -MT"$@" --specs=nano.specs -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -o "$@"
Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_pwr.o: ../Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_pwr.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DSTM32H750xx '-DEXTERNAL_CLOCK_VALUE=12288000' '-DVDD_VALUE=3300' '-DLSI_VALUE=32000' '-DHSI_VALUE=64000000' '-DHSE_VALUE=25000000' '-DHSE_STARTUP_TIMEOUT=100' -DUSE_FULL_LL_DRIVER '-DLSE_STARTUP_TIMEOUT=5000' -DDEBUG '-DLSE_VALUE=32768' -c -I../Core/Inc -I../Drivers/STM32H7xx_HAL_Driver/Inc -I../Drivers/CMSIS/Device/ST/STM32H7xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_pwr.d" -MT"$@" --specs=nano.specs -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -o "$@"
Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_rcc.o: ../Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_rcc.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DSTM32H750xx '-DEXTERNAL_CLOCK_VALUE=12288000' '-DVDD_VALUE=3300' '-DLSI_VALUE=32000' '-DHSI_VALUE=64000000' '-DHSE_VALUE=25000000' '-DHSE_STARTUP_TIMEOUT=100' -DUSE_FULL_LL_DRIVER '-DLSE_STARTUP_TIMEOUT=5000' -DDEBUG '-DLSE_VALUE=32768' -c -I../Core/Inc -I../Drivers/STM32H7xx_HAL_Driver/Inc -I../Drivers/CMSIS/Device/ST/STM32H7xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_rcc.d" -MT"$@" --specs=nano.specs -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -o "$@"
Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_utils.o: ../Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_utils.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DSTM32H750xx '-DEXTERNAL_CLOCK_VALUE=12288000' '-DVDD_VALUE=3300' '-DLSI_VALUE=32000' '-DHSI_VALUE=64000000' '-DHSE_VALUE=25000000' '-DHSE_STARTUP_TIMEOUT=100' -DUSE_FULL_LL_DRIVER '-DLSE_STARTUP_TIMEOUT=5000' -DDEBUG '-DLSE_VALUE=32768' -c -I../Core/Inc -I../Drivers/STM32H7xx_HAL_Driver/Inc -I../Drivers/CMSIS/Device/ST/STM32H7xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_ll_utils.d" -MT"$@" --specs=nano.specs -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -o "$@"

