################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Src/main.c \
../Src/syscalls.c \
../Src/sysmem.c 

C_DEPS += \
./Src/main.d \
./Src/syscalls.d \
./Src/sysmem.d 

OBJS += \
./Src/main.o \
./Src/syscalls.o \
./Src/sysmem.o 


# Each subdirectory must supply rules for building sources it contributes
Src/main.o: ../Src/main.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DSTM32F303VCTx -DSTM32 -DSTM32F3 -DSTM32F3DISCOVERY -DDEBUG -c -I../Inc -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/CMSIS/Core/Include" -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/CMSIS/Device/ST/STM32F3xx/Include" -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/STM32F3xx_HAL_Driver/Inc" -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/STM32F3xx_HAL_Driver/Inc/Legacy" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/main.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"
Src/syscalls.o: ../Src/syscalls.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DSTM32F303VCTx -DSTM32 -DSTM32F3 -DSTM32F3DISCOVERY -DDEBUG -c -I../Inc -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/CMSIS/Core/Include" -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/CMSIS/Device/ST/STM32F3xx/Include" -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/STM32F3xx_HAL_Driver/Inc" -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/STM32F3xx_HAL_Driver/Inc/Legacy" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/syscalls.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"
Src/sysmem.o: ../Src/sysmem.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DSTM32F303VCTx -DSTM32 -DSTM32F3 -DSTM32F3DISCOVERY -DDEBUG -c -I../Inc -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/CMSIS/Core/Include" -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/CMSIS/Device/ST/STM32F3xx/Include" -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/STM32F3xx_HAL_Driver/Inc" -I"C:/Users/User/STM32Cube/Repository/STM32Cube_FW_F3_V1.11.2/Drivers/STM32F3xx_HAL_Driver/Inc/Legacy" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Src/sysmem.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

