#include <stdio.h>

/*This program contains the simplest form of a buffer overflow vulnerability.
It is very easily solved in this case, but its more common exploitable variants
are displayed in many of the practice CTFs we do.*/

int main(int argc,char** argv){

//keep an eye on padding and how it changes even when only overflowing into i
	int padding = 0x11111111;
	int i = 0xFFFFFFFF;
	char buf[8];

	printf("i=%x%08x\n",i);
	printf("Change the value of i to 0x67416c46\n");

	fgets(buf,16,stdin);

	printf("i=0x%08x\n",i);
	printf("padding=0x%08x\n",padding);

	if (i == 0x67416c46){
		printf("Congratulations you did it!\n");
	} else {
		printf("You have not changed the value of i to the correct value\n");
	}
	return 0;
}
