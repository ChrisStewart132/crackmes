#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define TEST_PASSWORD "passwo"
#define STACK_SIZE 10000
time_t START_TIME;

void free_stack(char** stack){
    for(int i = 0; i < STACK_SIZE; i++){
        free(stack[i]);
    }
    free(stack);
}

void brute_force(int max_length, char* symbols, char* starting_candidate) {
    char** stack = (char**)malloc(sizeof(char*) * STACK_SIZE);

    stack[0] = malloc(sizeof(char)*(strlen(starting_candidate)+1));
    strcpy(stack[0], starting_candidate);
    int esp = 0;

    while(esp > -1){
        char* candidate = stack[esp--];
        //printf("%s\n", candidate);
        // Test the candidate
        if (strcmp(candidate, TEST_PASSWORD) == 0) {
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
    }
    free_stack(stack);
}

int main(int argc, char *argv[]) {
    START_TIME = time(NULL);

    char* candidate;
    if (argc == 3) {
        candidate[0] = '\0';
    }else if (argc != 4) {
        printf("usage: %s [max_length_int, symbols_string, opt:candidate_string]\n", argv[0]);
        return 1;
    }else{
        candidate = argv[3];
    }
    int max_length = atoi(argv[1]);
    char* symbols = argv[2];
    //printf("argc: %d, max_length: %d, symbols: %s, candidate: %s\n", argc, max_length, symbols, candidate);
    
    brute_force(max_length, symbols, candidate);  
    return 0;
}
