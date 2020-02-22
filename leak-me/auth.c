#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int flag() {
  char flag[48];
  FILE *file;
  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);
  printf("%s", flag);
  return 0;
}


int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  
  // real pw: 
  FILE *file;
  char password[64];
  char name[256];
  char password_input[64];
  
  memset(password, 0, sizeof(password));
  memset(name, 0, sizeof(name));
  memset(password_input, 0, sizeof(password_input));
  
  printf("What is your name?\n");
  
  fgets(name, sizeof(name), stdin); //if buffer overflow, the input will write in password[64] (stack structure), name and password buf will merge
  char *end = strchr(name, '\n'); //strchr: find char and return the pointer
  if (end != NULL) {  //if overflow, it cannot find \n
    *end = '\x00';
  }

  strcat(name, ",\nPlease Enter the Password."); //if overflow, nothing to do

  file = fopen("password.txt", "r");
  if (file == NULL) {
    printf("Password File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(password, sizeof(password), file);

  printf("Hello ");
  puts(name); //Since puts determine NULL, the name include password

  fgets(password_input, sizeof(password_input), stdin);
  password_input[sizeof(password_input)] = '\x00';
  
  if (!strcmp(password_input, password)) {
    flag();
  }
  else {
    printf("Incorrect Password!\n");
  }
  return 0;
}
