#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main()
{
pid_t pid,p;
pid=fork();
if(pid<0)
{
printf(stderr, "\n Error");
exit(1);
}
 else if(pid==0){
printf("\n I am a child process");
printf("\n My pid is %d", getpid());
exit(0);
} 
else{
   printf("\n I am parent process");
   printf("\n My actual pid is : %d", getpid());
  wait(NULL);
  exit(1);
}
}
