#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

const char* days[] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
const char* classes[] = {"A", "B", "C"};
const char* subjects[] = {"Sub1", "Sub2", "Sub3", "Sub4", "Sub5", "Sub6", "Sub7", "Sub8"};

int main() {
    srand(time(0));
    char timetable[3][6][8][20];
    for (int c = 0; c < 3; c++) {
        for (int d = 0; d < 6; d++) {
            for (int p = 0; p < 8; p++) {
                int i = rand() % 8;
                strcpy(timetable[c][d][p], subjects[i]);
            }
        }
    }

    printf("Weekly Timetable:\n\n");
    for (int c = 0; c < 3; c++) {
        printf("Class %s\n\n", classes[c]);
        for (int d = 0; d < 6; d++) {
            printf("%20s", days[d]);
        }
        printf("\n");
        for (int p = 0; p < 8; p++) {
            for (int d = 0; d < 6; d++) {
                printf("%20s", timetable[c][d][p]);
            }
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}
