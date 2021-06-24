function largestPrimeFactor(number) {
  let i =2
while(number>1){
  while (number%i==0){
    number/=i
  
  }  
  i+=1
}
console.log(i-1)
return i-1
}

largestPrimeFactor(13195);