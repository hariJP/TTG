#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void shuffle(int *array, int size) {
    int i, j, temp;
    for (i = 0; i < size; i++) {
        j = rand() % size;
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

int main() {
    int i, j, k, l;
    int subjects[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    int classes[3] = {'A', 'B', 'C'};
    int years[3] = {1, 2, 3};
    int schedule[6][3][3][8];

    srand(time(NULL));

    for (i = 0; i < 6; i++) {
        printf("Day %d\n", i + 1);
        shuffle(classes, 3);
        for (j = 0; j < 3; j++) {
            printf("Class %c\n", classes[j]);
            shuffle(years, 3);
            for (k = 0; k < 3; k++) {
                printf("Year %d\n", years[k]);
                shuffle(subjects, 8);
                for (l = 0; l < 8; l++) {
                    schedule[i][j][k][l] = subjects[l];
                    printf("Period %d: Subject %d\n", l + 1, subjects[l]);
                }
                printf("\n");
            }
            printf("\n");
        }
    }

    return 0;
}
