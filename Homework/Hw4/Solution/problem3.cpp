#include<iostream>
int fib(int n){
  if( n==1 || n==0){
    return n;
  }else{
    return fib(n-1)+fib(n-2);
  } 
}
int main(){
  for(int i=0;i<10;i++){
    std::cout<<fib(i)<<std::endl;
  }
  return 0;
}
