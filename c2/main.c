#include <stdio.h>
#include <stdbool.h>
#define BUFFER_SIZE 10

void buffer_overflow_success(){
    printf("b4ff3r0v3rf10w\n");
}

int main(int argc, char** argv){
    char a = 'a';
    char buffer[BUFFER_SIZE];
    char b = 'b';
    printf("Password: ");
    gets(buffer);// buffer overflow vulnerability
    buffer[BUFFER_SIZE-1] = '\0';
    
    printf("terminated_password: %s, a: %c, b: %c\n", buffer, a, b);
    if(a != 'a' || b != 'b'){
        buffer_overflow_success();
    }

    getc(stdin);
    return 0;
}