####################################################################
# Start of path customization
# fill following lines replacing <...> with the proper absolute path
#

####################### Source path ################################
# TF-A source path
directory /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/tf-a-stm32mp-2.0-r0/arm-trusted-firmware-2.0

# OP-TEE source path
#directory <full_path_to_OP-TEE_source>/

# U-Boot source path
set substitute-path /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/u-boot-stm32mp-2018.11-r0/build-trusted/ /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/u-boot-stm32mp-2018.11-r0/u-boot-2018.11/
# <source_path_from_u-boot_elf_file> can be retrieve from u-boot elf with the following readelf command: readelf --string-dump=.debug_str <u-boot_elf_file> | sed -n '/\/\|\.c/{s/.*\] //p}'

# Linux kernel source path
set substitute-path /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/linux-stm32mp-4.19-r0/build /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/linux-stm32mp-4.19-r0/linux-4.19.9/

# <source_path_from_vmlinux> can be retrieve from vmlinux with the following readelf command: readelf --string-dump=.debug_str vmlinux | sed -n '/\/\|\.c/{s/.*\] //p}'
####################################################################

####################### Symbol path ################################
define symload_bl32
#	symbol-file <full_path_to_tf-a-bl32-trusted.elf>
	symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/tf-a-stm32mp-2.0-r0/build/trusted/tf-a-bl32-trusted.elf
end
document symload_bl32
#	format: symbol-file <full_path_to_tf-a-bl32-trusted.elf>
	format: symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/tf-a-stm32mp-2.0-r0/build/trusted/tf-a-bl32-trusted.elf

end

define symadd_bl32
#	add_symbol-file <full_path_to_tf-a-bl32-trusted.elf> $arg0
	add-symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/tf-a-stm32mp-2.0-r0/build/trusted/tf-a-bl32-trusted.elf $arg0
end
document symadd_bl32
#	format: add_symbol-file <full_path_to_tf-a-bl32-trusted.elf> $arg0
	format: add_symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/tf-a-stm32mp-2.0-r0/build/trusted/tf-a-bl32-trusted.elf $arg0
end

define symload_bl2
#	symbol-file <full_path_to_tf-a-bl2-trusted.elf>
	symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/tf-a-stm32mp-2.0-r0/build/trusted/tf-a-bl2-trusted.elf
end
document symload_bl2
#	format: symbol-file <full_path_to_tf-a-bl2-trusted.elf>
	format: symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/tf-a-stm32mp-2.0-r0/build/trusted/tf-a-bl2-trusted.elf
end

define symload_uboot
#	symbol-file <full_path_to_u-boot-stm32mp157c-dk2-trusted.elf>
	symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/u-boot-stm32mp-2018.11-r0/build-trusted/u-boot-stm32mp157c-dk2-trusted.elf
end
document symload_uboot
#	format: symbol-file <full_path_to_u-boot-stm32mp157c-dk2-trusted.elf>
	format: symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/u-boot-stm32mp-2018.11-r0/build-trusted/u-boot-stm32mp157c-dk2-trusted.elf
end

define symadd_uboot
#	set $offset = ((gd_t *)$r9)->relocaddr
#	add-symbol-file <full_path_to_u-boot-stm32mp157c-dk2-trusted.elf> $offset

	set $offset = ((gd_t *)$r9)->relocaddr
	add-symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/u-boot-stm32mp-2018.11-r0/build-trusted/u-boot-stm32mp157c-dk2-trusted.elf $offset
end
document symadd_uboot
#	format: symbol-file <full_path_to_u-boot-stm32mp157c-ev1-trusted.elf> $offset
#	offset is given by command: set $offset = ((gd_t *)$r9)->relocaddr
	set $offset = ((gd_t *)$r9)->relocaddr
	format: symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/u-boot-stm32mp-2018.11-r0/build-trusted/u-boot-stm32mp157c-dk2-trusted.elf $offset
end

define symload_vmlinux
	symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/linux-stm32mp-4.19-r0/linux-4.19.9/vmlinux
end
document symload_vmlinux
	format: symbol-file /local/STM32MP15-Ecosystem-v1.0.0/Developer-Package/stm32mp1-openstlinux-4.19-thud-mp1-19-02-20/sources/arm-openstlinux_weston-linux-gnueabi/linux-stm32mp-4.19-r0/linux-4.19.9/vmlinux
end


define symload_optee
	symbol-file <full_path_to_tee.elf>
end
document symload_optee
	format: symbol-file <full_path_to_tee.elf>
end

define symadd_optee
	add-symbol-file <full_path_to_tee.elf> $arg0
end
document symadd_optee
	format: add_symbol-file <full_path_to_tee.elf> $arg0
end


####################################################################

#
# End of path customization
####################################################################

