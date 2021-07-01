# Set debug phase:
#	1: Attach at Cortex-A7 / TF-A(BL2)
#	2: Attach at Cortex-A7 / TF-A(BL32) or OP-TEE
#	3: Attach at Cortex-A7 / U-Boot
#	4: Attach at Cortex-A7 / Linux kernel
set $debug_phase = 4
#	0: Attach at boot
#	1: Attach running target
set $debug_mode = 0
# Set debug trusted bootchain:
#	0: TF-A BL2 / TF-A BL32 / U-Boot / Linux kernel
#	1: TF-A BL2 / OP-TEE / U-Boot / Linux kernel
set $debug_trusted_bootchain = 0 
#depending on your software boot chain configuration

source Path_env.gdb


####################################################################
########################## functions ###############################
####################################################################
define break_bl2initram
	thbreak bl2_el3_plat_prepare_exit
	c
end

define break_boot_tf-a
	thbreak bl2_entrypoint
	c
end

define break_boot_bl32
	thbreak sp_min_entrypoint
	c
end

define break_boot_optee
	thbreak generic_entry_a32.S:_start
	c
end

define break_boot_uboot
	thbreak vectors.S:_start
	c
end

define break_boot_linuxkernel
	thbreak stext
	c
end
####################################################################


######################## common config. ############################
# Disables confirmation requests
# Set environment configuration
set confirm off

# Connection to the host gdbserver port for Cortex-A7 SMP
target remote localhost:3334

# Configure GDB for OpenOCD
set remote hardware-breakpoint-limit 6
set remote hardware-watchpoint-limit 4

# Switch to Core0
monitor cortex_a smp_gdb 0
stepi
monitor cortex_a smp_gdb -1
# No SMP, only core 0 for the moment. We'll re-enable it in kernel
monitor cortex_a smp_off

# Get load address for BL32 or OP-TEE
if $debug_trusted_bootchain == 0
	#get load-address of BL32
	symload_bl32
	set $bl32_load_addr = sp_min_entrypoint
else
	#get load-address of OP-TEE
	symload_optee
	set $optee_load_addr = _start
end

# Reset the system and halt in bootrom in case of attach at boot
if $debug_mode == 0
	monitor reset
	monitor sleep 2000
	monitor reset halt
	monitor gdb_sync
	stepi

	# Switch to Core0 after reset halt
	monitor cortex_a smp_gdb 0
	stepi
	monitor cortex_a smp_gdb -1
	# No SMP, only core 0 for the moment. We'll re-enable it in kernel
	monitor cortex_a smp_off

	symload_bl2

	if $debug_trusted_bootchain == 0
		symadd_bl32 $bl32_load_addr
	else
		symadd_optee $optee_load_addr
	end
end
####################################################################

# Set hardware breakpoint mode for TF-A OP-TEE and U-Boot
if $debug_phase <= 3
	monitor gdb_breakpoint_override hard
end

#####################################################
# To stop at TF-A BL2
if $debug_phase == 1
	break_boot_tf-a

else

	#####################################################
	# To stop at TF-A BL32 or OP-TEE
	if $debug_phase == 2
		if $debug_trusted_bootchain == 0
			break_boot_bl32
		else
			break_boot_optee
		end
	
	else

		#####################################################
		# To stop at U-Boot
		if $debug_phase == 3
			if $debug_mode == 0
				break_bl2initram
			end

			# Load U-Boot symbols
			symload_uboot

			if $debug_mode == 1
				# Relocate U-Boot symbols
				symadd_uboot
			end


			if $debug_trusted_bootchain == 0
				symadd_bl32 $bl32_load_addr
			else
				symadd_optee $optee_load_addr
			end

			if $debug_mode == 0
				break_boot_uboot
			end

		else

			#####################################################
			# To stop at Linux kernel
			if $debug_phase == 4
				if $debug_mode == 0
					break_bl2initram
				end
			
				symload_vmlinux
			
				if $debug_mode == 1
					if $debug_trusted_bootchain == 0
						symadd_bl32 $bl32_load_addr
					else
						symadd_optee $optee_load_addr
					end
				end

				# if you are going to halt in kernel, re-enable SMP
				monitor cortex_a smp_on

				if $debug_mode == 0
					break_boot_linuxkernel
				end
			end
		end
	end
end


