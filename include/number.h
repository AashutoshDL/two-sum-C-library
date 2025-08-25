#ifndef NUMLIB_NUMUTILS_H //prevent multiple exclusion of this header
#define NUMLIB_NUMUTILS_H

#include <stdint.h> //for fixed width integre types

#ifdef __cplusplus
extern "C"{
#endif

//checks if the number is even
int is_even(int64_t n);

//checks if the number is odd
int is_odd(int64_t n);

//this function adds the number
int sum_number(int64_t a,int64_t b);

#ifdef __cplusplus
}
#endif

#endif //exits the numlib 
