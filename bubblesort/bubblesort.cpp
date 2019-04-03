#include<omp.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <iostream>
#include <unistd.h>
#include<chrono>

using namespace std;

#ifdef __cplusplus
extern "C" {
#endif

  void generateMergeSortData (int* arr, size_t n);
  void checkMergeSortResult (const int* arr, size_t n);

#ifdef __cplusplus
}
#endif


int main (int argc, char* argv[]) {


  //forces openmp to create the threads beforehand
#pragma omp parallel
  {
    int fd = open (argv[0], O_RDONLY);
    if (fd != -1) {
      close (fd);
    }
    else {
      std::cerr<<"something is amiss"<<std::endl;
    }
  }
  
  if (argc < 3) { std::cerr<<"usage: "<<argv[0]<<" <n> <nbthreads>"<<std::endl;
    return -1;
  }

  int n = atoi(argv[1]);
  int nbthreads = atoi(argv[2]);
  
  omp_set_num_threads(nbthreads);

  // get arr data
  int * arr = new int [n];
  generateMergeSortData (arr, n);
  //insert sorting code here.
  std::chrono::time_point<std::chrono::system_clock> start = std::chrono::system_clock::now();
  for (int i = 0; i < n; ++i)
  {
    int begin = i%2;

      #pragma omp parallel for default(none) shared(arr, begin) firstprivate(n)
      for (int j = begin; j < n-1; j+=2)
      {
        if (arr[j]>arr[j+1])
        {
          //swap(&arr[j], &arr[j+1]);
          arr[j] = arr[j+1] + arr[j];
          arr[j+1] = arr[j] - arr[j+1];
          arr[j] = arr[j] - arr[j+1];
        }
      } 
  }

  checkMergeSortResult (arr, n);
  std::chrono::time_point<std::chrono::system_clock> end = std::chrono::system_clock::now();
  std::chrono::duration<double> elapsed_seconds = end-start;
  std::cerr<<elapsed_seconds.count()<<std::endl;
  delete[] arr;

  return 0;
}
