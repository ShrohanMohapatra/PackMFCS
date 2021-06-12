#include<stdio.h>
long int ackermann(long int matrix[100][100],long int m,long int n){
    printf("Entering the function with the following parameters-> %ld, %ld\n",m,n);
    if(m==0){
        matrix[m][n]=n+1;
    }
    else if(n==0){
        matrix[m][n]=ackermann(matrix,m-1,1);
    }
    else{
        matrix[m][n]=ackermann(matrix,m-1,ackermann(matrix,m,n-1));
    }
    return matrix[m][n];
}
int main(){
    long int size = 100;
    printf("Just entered the dynamic programming section now\n");
    long int dynamicProg[size][size];
    long int k, m;
    for(k=0;k<size;k++){
        for(m=0;m<size;m++){
            printf("Processing Row number %ld Processing Column number %ld\n",k,m);
            dynamicProg[k][m] = 0;
        }
    }
    for(k=0;k<4;k++){
        for(m=0;m<4;m++){
            printf("DynamicPBacker (%ld, %ld) -> %ld\n",k,m,dynamicProg[k][m]);
            printf("FunctionBacker (%ld, %ld) -> %ld\n",k,m,ackermann(dynamicProg,k,m));
        }
    }
    printf("\n");
    return 0;
}