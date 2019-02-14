#include <iostream>
int main(){
  int NumberTest=777071;
  for(int i=2;i<NumberTest;i++){
    if(NumberTest%i==0){
      std::cout<<"The number is not Prime"<<std::endl;
      break;
    }
    if (i==(NumberTest-1)){
      std::cout<<"The number is Prime"<<std::endl;
	}
  }
  return 0;
}
