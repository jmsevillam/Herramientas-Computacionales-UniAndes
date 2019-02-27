#include<iostream>
#include<vector>
//To compile, use the flag -std=c++11
//g++ -std=c++11 problem.cpp 
int main(){
  bool swapped;
  double aux;
  std::vector<double> list_test{1,3,8,1.2,6,2,9,3,8,5,10};
  for(int i =0; i< list_test.size();i++){
    std::cout<<list_test[i]<<' ';
  }
  std::cout<<std::endl;
  for(int i =0; i< list_test.size()-1;i++){
    swapped=false;
    for(int j =0; j< list_test.size()-1;j++){
      if(list_test[j]>list_test[j+1]){
	aux=list_test[j];
	list_test[j]=list_test[j+1];
	list_test[j+1]=aux;
	swapped=true;
      }
    }
    if(!swapped){
      break;
    }
  }
  for(int i =0; i< list_test.size();i++){
    std::cout<<list_test[i]<<' ';
  }
  std::cout<<std::endl;
  return 0;
}
