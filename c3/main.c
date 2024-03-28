#include <stdio.h>
#include <stdbool.h>
#define BUFFER_SIZE 10

/*
solution
NOTE THE STACK IS LITTLE ENDIAN, the tail is pushed to the stack first
    rbp -[0x17:0xd] i.e. 0xe null terminate and 0x17=start
    ...
    rbp -[0xd:0x3] = 10 bytes = buffer2
        -0xd = buffer2[0]
        -0xd = buffer2[1]
        ...
        -0x4 = buffer2[9]// tail
    ...
    rbp -0x3 = c
        -0x2 = b
        -0x1 = a
    password:
        password00
        BBBBBBBBB0e12345678z// note e<->z = buffer2 but will fail as entering appends a new line
        BBBBBBBBB0e12345678zcba// note cba sets the char values a,b,c which are required to remain the same...
*/

void buffer_overflow_success(){
    printf("b4ff3r0v3rf10w\n");
}

int main(int argc, char** argv){
    char buffer2[BUFFER_SIZE];
    buffer2[0] = 'A';
    buffer2[BUFFER_SIZE-1] = 'B';

    char a = 'a';
    char buffer[BUFFER_SIZE];
    char b = 'b';
    char c = 'c';

    printf("Password: ");
    gets(buffer);// buffer overflow vulnerability
    buffer[BUFFER_SIZE-1] = '\0';
    if(a != 'a' || b != 'b' || c != 'c'){
        printf("invalid! a: %c, b: %c, c: %c\n", a, b, c);
        getc(stdin);
        return 1;
    }

    printf("terminated_password: %s, a: %c, b: %c, c: %c\n", buffer, a, b, c);
    if(buffer2[0] == 'e' && buffer2[BUFFER_SIZE-1] == 'z'){
        buffer_overflow_success();
    }else{
        printf("e: %c z: %c\n", buffer2[0], buffer2[1]);
    }
    getc(stdin);
    return 0;
}