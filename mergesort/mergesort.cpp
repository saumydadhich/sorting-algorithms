#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <iostream>
#include <unistd.h>
#include <chrono>
#include <omp.h>

#ifdef __cplusplus
extern "C" {
#endif

  void generateMergeSortData (int* arr, size_t n);
  void checkMergeSortResult (int* arr, size_t n);

#ifdef __cplusplus
}
#endif

void merge(int * arr, int l, int mid, int r, int * arr1) {
  if (l == r) return;
  if (r-l == 1) {
    if (arr[l] > arr[r]) {
      int temp = arr[l];
      arr[l] = arr[r];
      arr[r] = temp;
    } 
    return;
  }

  int i, j, k;
  int n = mid - l;
  
  for (i=0; i<n; ++i){
    arr1[i] = arr[l+i];
	}
  i = 0;   
  j = mid; 
  k = l;   

  while (i<n && j<=r) {
     if (arr1[i] <= arr[j] ) {
       arr[k++] = arr1[i++];
     } else {
       arr[k++] = arr[j++];
     }
  }

  while (i<n) {
    arr[k++] = arr1[i++];
  }
}


void mergesort(int * arr, int low, int high) {
	int * temp = new int [high-low+1];
  if (low < high) {
		
    int mid = (low+high)/2;
	#pragma omp task if(high-low>10000)
		mergesort(arr, low, mid);
	//#pragma omp taskwait
	#pragma omp task if(high-low>10000)
		mergesort(arr, mid+1, high);
	#pragma omp taskwait
    merge(arr, low, mid+1, high, temp);
  }
  delete [] temp;
}


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
	//int * temp = new int [n];
  generateMergeSortData (arr, n);

  //insert sorting code here.
	std::chrono::time_point<std::chrono::system_clock> start = std::chrono::system_clock::now();
	#pragma omp parallel 
	{
		#pragma omp single
		{
			mergesort(arr, 0, n-1);
		}
	}
	std::chrono::time_point<std::chrono::system_clock> end = std::chrono::system_clock::now();
	std::chrono::duration<double> elapsed_seconds = end-start;
	std::cerr<<elapsed_seconds.count()<<std::endl;
	checkMergeSortResult (arr, n);
	delete[] arr;
	//delete[] temp;
  return 0;
}
