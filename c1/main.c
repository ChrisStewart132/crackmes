#include <stdio.h>
#define BUFFER_SIZE 10

int main(int argc, char** argv){
    printf("argc: %d\n", argc);
    for(int i = 0; i < argc; i++){
        printf("arg[%d]: %s\n", i, argv[i]);
    }
    char buffer[BUFFER_SIZE];
    printf("Password: ");
    gets(buffer);// buffer overflow vulnerability
    buffer[BUFFER_SIZE-1] = '\0';
    if(strlen(buffer) == BUFFER_SIZE/2){
        printf("success\n");
        return 0;
    }
    return 1;
}