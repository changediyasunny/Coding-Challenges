#include<stdio.h>
#include<string.h>
#include<stdlib.h>

// Returns length of the longest common sum in arr1[]
// and arr2[]. Both are of same size n.
int longestCommonSum(int arr1[], int arr2[], int n)
{
    // Initialize result
    int maxLen = 0;
 	int i, j;
    // Initialize prefix sums of two arrays
    int preSum1 = 0, preSum2 = 0;
 
    // Create an array to store staring and ending
    // indexes of all possible diff values. diff[i]
    // would store starting and ending points for
    // difference "i-n"
    int diff[2*n+1];
 
    // Initialize all starting and ending values as -1.
    memset(diff, -1, sizeof(diff));
 
    // Traverse both arrays
    for (i=0; i<n; i++)
    {
        // Update prefix sums
        preSum1 += arr1[i];
        preSum2 += arr2[i];
 
        // Comput current diff and index to be used
        // in diff array. Note that diff can be negative
        // and can have minimum value as -1.
        int curr_diff = preSum1 - preSum2;
        int diffIndex = n + curr_diff;
 
        // If current diff is 0, then there are same number
        // of 1's so far in both arrays, i.e., (i+1) is
        // maximum length.
        if (curr_diff == 0)
            maxLen = i+1;
 
        // If current diff is seen first time, then update
        // starting index of diff.
        else if ( diff[diffIndex] == -1)
            diff[diffIndex] = i;
 
        // Current diff is already seen
        else
        {
            // Find lenght of this same sum common span
            int len = i - diff[diffIndex];
 
            // Update max len if needed
            if (len > maxLen)
                maxLen = len;
        }
    }
    return maxLen;
}
 
// Driver progra+m to test above function
int main()
{
    int  arr1[] = {0, 1, 0, 0, 0, 0, 0};
    int  arr2[] = {0, 0, 0, 0, 0, 0, 0};
    int n = sizeof(arr1)/sizeof(arr1[0]);
    printf("\n %d", longestCommonSum(arr1, arr2, n));
    printf("\n");
    return 0;
}
