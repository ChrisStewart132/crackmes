#include <stdio.h>
#include <stdbool.h>
#define BUFFER_SIZE 16

void buffer_overflow_success(){
    printf("b4ff3r0v3rf10w\n");
}

int main(int argc, char** argv){
    char a = 'a';
    char b = 'b';
    char c = 'c';
    char un_buffer[BUFFER_SIZE];
    char pw_buffer[BUFFER_SIZE];
    const char* buffer1 = "buffer1";// buffer ptr to .data stored in stack overwrite carefully
    const char* buffer2 = "buffer2";// buffer ptr to .data stored in stack overwrite carefully
    
    printf("Username: ");
    fgets(un_buffer, BUFFER_SIZE, stdin);
    printf("Password: ");
    gets(pw_buffer);// buffer overflow vulnerability
    pw_buffer[BUFFER_SIZE-1] = '\0';// null terminate password
    printf("buffer21: %s, buffer2: %s, un: %s, pw: %s, a: %c, b: %c, c: %c\n", buffer1, buffer2, un_buffer, pw_buffer, a, b, c);
    if(a != 'a' && b != 'b' && c != 'c'){
        buffer_overflow_success();
    }
    getc(stdin);
    return 0;
}