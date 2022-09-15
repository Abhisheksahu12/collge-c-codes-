#include<unistd.h>
#include<stdlib.h>
#include<stdio.h>

int main()
{

/*
printf("\n The kernel version is: \n");
system("cat /proc/sys/kernel/osrelease");
printf("\n The CPU info: \n");
system("cat /proc/cpuinfo\n");
return 0;
}
*/

int a;
printf("\nKernel Version:");
system("cat /proc/sys/kernel/osrelease");
printf("\nConfigured free and Used memory:\n");
system("cat /proc/meminfo | awk 'NR==1, NR==2 {print}'");
return 0;
}

