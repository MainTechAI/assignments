#include "mpi.h"
#include <iostream>
using namespace std;


int main(int argc, char* argv[])
{
    MPI_Init(&argc, &argv);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) {
        int size;
        MPI_Comm_size(MPI_COMM_WORLD, &size);
        printf("%d processes!\n", size);
    }
    else if (rank % 2 == 0) {
        printf("I am %d process: SECOND!\n", rank);
    }
    else {
        printf("I am %d process: FIRST!\n", rank);
    }
 
    MPI_Finalize();
    return 0;
}
