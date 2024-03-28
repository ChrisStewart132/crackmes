#include <stdio.h>
#include <stdbool.h>
#define BUFFER_SIZE 16
// NOT SURE WHY THE BYTES VALUES IN PAYLOAD ARNT CORRECTLY BEING WRITTEN
// AND BUFFER OVERFLOW SUCCESS NOT CALLED

// 00007FF7E1FC14A4 (relative addr of the function)
// return ptr at rbp+8 (x64)
// buffer overflow at rbp-0x18
void buffer_overflow_success(){
    printf("b4ff3r0v3rf10w\n");
    getc(stdin);
    exit(0);
}

int main(int argc, char** argv){
    char buffer[BUFFER_SIZE];
    printf("BufferOverflowVulnerability: ");
    gets(buffer);
    buffer[BUFFER_SIZE-1] = '\0';
    printf("buffer: %s\n", buffer);

    getc(stdin);
    return 0;
}