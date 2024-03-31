#include "Windows.h"
#include "winsock2.h"
#include <stdio.h>

#define PORT 10487
#define PASSWORD "23633395"
#define INVALID_MESSAGE "IM"
#define VALID_MESSAGE "success"
#define BUFFER_SIZE 64
const char* HOST = "127.0.0.1";


int main(int argc, char** argv){
    WSADATA wsaData;
    int result = WSAStartup(MAKEWORD(2, 2), &wsaData);


    //s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    SOCKET s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

    //s.bind((HOST, PORT))
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = inet_addr(HOST);
    serverAddr.sin_port = htons(PORT);
    bind(s, &serverAddr, sizeof(serverAddr));


    char buffer[BUFFER_SIZE];
    int flag = 0;
    const char* validMessage = VALID_MESSAGE;
    const char* invalidMessage = INVALID_MESSAGE;
    struct sockaddr_in clientAddr;
    int clientAddrSize = sizeof(clientAddr);
    int i = 0;
    while(1){
        //data, addr = s.recvfrom(64)
        int bytesReceived = recvfrom(s, buffer, BUFFER_SIZE, flag, &clientAddr, &clientAddrSize);
        if (bytesReceived == SOCKET_ERROR) {
            printf("Recvfrom failed %d\n", WSAGetLastError());
        }else if(i%1000000==0){
            buffer[bytesReceived] = '\0';
            printf("%d %s recvd from: %d\n", strlen(buffer), buffer, clientAddr.sin_port);
            //printf("recvfrom: %d\n", clientAddr.sin_port);
        }
        

        //s.sendto(response.encode("utf-8"), addr)
        if(strcmp(PASSWORD, buffer) == 0){
            printf("%s success\n", PASSWORD);
            sendto(s, validMessage, strlen(validMessage), flag, &clientAddr, sizeof(clientAddr));
            break;
        }else{
            sendto(s, invalidMessage, strlen(invalidMessage), flag, &clientAddr, sizeof(clientAddr));
        }
        i++;
    }
    
    getchar();

    // Cleanup
    closesocket(s);
    WSACleanup();
    return 0;
}