#include<iostream>
int fac(int n){
  if( n==1 || n==0){
    return 1;
  }else{
    return n*fac(n-1);
  } 
}
int main(){
  int m=10;
  std::cout<<fac(m)<<std::endl;
  return 0;
}
