#include <stdio.h>
#include <stdbool.h>
#define BUFFER_SIZE 10

/*
solution
NOTE THE STACK IS LITTLE ENDIAN, the tail is pushed to the stack first
NOTE entering the password as input adds a newline to the tail

    rbp -[0x1c:0x12] i.e. 0xe null terminate and 0x1c=start
    ...
    rbp -0x12 = c
        -0x11 = b
    ...
        -0x10
        ptr that mustn't be changed
        -0x2
    ...
        -0x1 = a
    password:
        AAAAAAAAAAkjBBBBBBBBBBBBBBBi
            buffer 2 BB...BB will crash as the ptr to buffer2 is inaccessible
            see payload.py script to generate payload with nullbytes so buffer2 is still accessible
*/

void buffer_overflow_success(){
    printf("b4ff3r0v3rf10w\n");
}

int main(int argc, char** argv){
    
    char a = 'a';
    char pw_buffer[BUFFER_SIZE];
    const char* buffer2 = "buffer2";// buffer ptr to .data stored in stack overwrite carefully
    char b = 'b';
    char c = 'c';

    printf("Password: ");
    gets(pw_buffer);// buffer overflow vulnerability
    pw_buffer[BUFFER_SIZE-1] = '\0';// null terminate password
    printf("buffer2: %s, terminated_password: %s, a: %c, b: %c, c: %c\n", buffer2, pw_buffer, a, b, c);
    if(a != 'a' && b != 'b' && c != 'c'){
        buffer_overflow_success();
    }
    getc(stdin);
    return 0;
}