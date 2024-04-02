#include "Windows.h"
#include "winsock2.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

const char* HOST = "127.0.0.1";
#define PORT 10487
#define VALID_MESSAGE "success"
#define BUFFER_SIZE 16
#define STACK_SIZE 6400
time_t START_TIME;

void free_stack(char** stack){
    for(int i = 0; i < STACK_SIZE; i++){
        free(stack[i]);
    }
    free(stack);
}

bool test_candidate(const char* candidate, SOCKET s, struct sockaddr_in serverAddr, char* buffer){
    int res = sendto(s, candidate, strlen(candidate), 0, &serverAddr, sizeof(serverAddr));
    if (res == SOCKET_ERROR) {
        printf("Recvfrom failed %d\n", WSAGetLastError());
    }
    int bytesReceived = recv(s, buffer, BUFFER_SIZE, 0);
    buffer[bytesReceived] = '\0';
    return strcmp(buffer, VALID_MESSAGE) == 0;
}

void brute_force(int max_length, char* symbols, char* starting_candidate, SOCKET s, struct sockaddr_in serverAddr, char* buffer) {
    char** stack = (char**)malloc(sizeof(char*) * STACK_SIZE);
    stack[0] = malloc(sizeof(char)*(strlen(starting_candidate)+1));
    strcpy(stack[0], starting_candidate);
    int esp = 0;
    while(esp > -1){
        char* candidate = stack[esp--];
        //printf("%s\n", candidate);
        // Test the candidate
        if (test_candidate(candidate, s, serverAddr, buffer)) {
            printf("%s %.2fs\n", candidate, difftime(time(NULL), START_TIME));
            break;
        }
        // Test the candidate's children if applicable
        if (strlen(candidate) < max_length) {
            int candidate_length = strlen(candidate);
            for (int i = 0; i < strlen(symbols); i++) {
                stack[++esp] = malloc((candidate_length + 2) * sizeof(char));  // Allocate memory for child candidate on the stack
                sprintf(stack[esp], "%s%c", candidate, symbols[i]);  // Create child candidate and null terminates
            }
        }
        free(candidate);
    }
    free_stack(stack);
}

int main(int argc, char *argv[]) {
    START_TIME = time(NULL);

    // setup socket
    WSADATA wsaData;
    int result = WSAStartup(MAKEWORD(2, 2), &wsaData);
    SOCKET s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    // server addr info
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = inet_addr(HOST);
    serverAddr.sin_port = htons(PORT);
    // recv buffer
    char buffer[BUFFER_SIZE];


    int max_length = atoi(argv[1]);
    char* symbols = argv[2];
    if (argc == 3) {
        brute_force(max_length, symbols, "", s, serverAddr, buffer);  
    }else if (argc != 4) {
        printf("usage: %s [max_length_int, symbols_string, opt:candidate_string]\n", argv[0]);
        return 1;
    }else{
        brute_force(max_length, symbols, argv[3], s, serverAddr, buffer);  
    }
    closesocket(s);
    WSACleanup();
    return 0;
}
