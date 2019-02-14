#include <iostream>
int main(){
  int NumberTest=777071;
  bool Prime=true;
  for(int i=2;i<NumberTest;i++){
    if(NumberTest%i==0){
      Prime=false;
      break;
    }
  }
  if(Prime){
   std::cout<<"The number is Prime"<<std::endl;
  }else {
   std::cout<<"The number is not Prime"<<std::endl;
  }
  return 0;
}
