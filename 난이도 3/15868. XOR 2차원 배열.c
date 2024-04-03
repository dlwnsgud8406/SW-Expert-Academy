#include <stdio.h>
#include <stdbool.h>

// Function to check if the matrix can be represented as XOR of two arrays
char* check_xor_matrix(int n, int m, int T[][m]) {
    int a[n], b[m];

    // Initialize arrays a and b based on the value of T[0][0]
    if (T[0][0] == 1) {
        a[0] = 0; // Since a[0] is always 0
        for (int i = 1; i < n; i++) {
            a[i] = T[i][0] ^ 1;
        }
        for (int j = 0; j < m; j++) {
            b[j] = T[0][j];
        }
    } else {
        for (int i = 0; i < n; i++) {
            a[i] = T[i][0];
        }
        b[0] = 0; // Since b[0] is always 0
        for (int j = 1; j < m; j++) {
            b[j] = T[0][j];
        }
    }

    // Check if the matrix can be represented as XOR of a[i] and b[j]
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if ((a[i] ^ b[j]) != T[i][j]) {
                return "no";
            }
        }
    }
    return "yes";
}

int main() {
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        int n, m;
        scanf("%d %d", &n, &m);
        int matrix[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf("%1d", &matrix[i][j]);
            }
        }

        printf("#%d %s\n", t, check_xor_matrix(n, m, matrix));
    }

    return 0;
}
