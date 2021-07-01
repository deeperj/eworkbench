// SPDX-identifier: GPL-2.0
/*
 * Copyright (C) STMicroelectronics SA 2018
 *
 * Authors: Bernard PUEL <bernard.puel@st.com>
 *
 */


#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <linux/gpio.h>

int main(int argc, char **argv)
{
	struct gpiohandle_request req;
	struct gpioevent_request ereq;
	struct gpiohandle_data data;
	struct gpioevent_data event;
	char chrdev_name[20];
	int fd, ret;

	strcpy(chrdev_name, "/dev/gpiochip0");

	memset(&data.values, 0, sizeof(data.values));

	/*  Open device: gpiochip0 for GPIO bank A */
	fd = open(chrdev_name, 0);
	if (fd == -1) {
		ret = -errno;
		fprintf(stderr, "Failed to open %s\n", chrdev_name);
		return ret;
	}

	/* request GPIO line: GPIO_A_14 for Led switching */
	req.lineoffsets[0] = 14;
	req.flags = GPIOHANDLE_REQUEST_OUTPUT | GPIOHANDLE_REQUEST_ACTIVE_LOW;
	memcpy(req.default_values, &data, sizeof(req.default_values));
	strcpy(req.consumer_label, "User PA14");
	req.lines  = 1;

	ret = ioctl(fd, GPIO_GET_LINEHANDLE_IOCTL, &req);
	if (ret == -1) {
		ret = -errno;
		fprintf(stderr, "Failed to issue GET LINEHANDLE IOCTL (%d)\n", ret);
		goto exit_close_error;
	}

	/* request GPIO line: GPIO_A_13 for Button activation*/
	ereq.lineoffset = 13;
	ereq.handleflags = GPIOHANDLE_REQUEST_INPUT;
	ereq.eventflags = GPIOEVENT_EVENT_FALLING_EDGE;
	strcpy(ereq.consumer_label, "User PA13");

	ret = ioctl(fd, GPIO_GET_LINEEVENT_IOCTL, &ereq);
	if (ret == -1) {
		ret = -errno;
		fprintf(stderr, "Failed to issue GET EVENT IOCTL (%d)\n",ret);
		goto exit_close_error;
	}

	fprintf(stdout, "Monitoring line %d on %s\n", ereq.lineoffset, chrdev_name);

	/*  Start main loop */
	while(1) {
 
		/* read GPIO_A_13 input event */
		ret = read(ereq.fd, &event, sizeof(event));
		if (ret == -1) {
			if (errno == -EAGAIN) {
				fprintf(stderr, "nothing available\n");
				continue;
			} else {
				ret = -errno;
				fprintf(stderr, "Failed to read event (%d)\n",ret);
				break;
			}
		}
		if (ret != sizeof(event)) {
			fprintf(stderr, "Reading event failed\n");
			ret = -EIO;
			break;
		}

		/* process the event received */
		switch (event.id) {
		case GPIOEVENT_EVENT_FALLING_EDGE:
			data.values[0] = !data.values[0];
			ret = ioctl(req.fd, GPIOHANDLE_SET_LINE_VALUES_IOCTL, &data);
			if (ret == -1) {
				ret = -errno;
				fprintf(stderr, "Failed to issue %s (%d)\n", "GPIOHANDLE_SET_LINE_VALUES_IOCTL", ret);
			}
			break;
		default:
			fprintf(stdout, "unknown event\n");
		}
	}

	/* release line */
exit_close_error:
	if (close(fd) == -1)
	perror("Failed to close GPIO character device file");
	return ret;
}
