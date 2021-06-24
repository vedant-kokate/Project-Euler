function sumSquareDifference(n) {
let a=0,b=0
for(let i = 0;i<n+1;i++){
  a+=i*i
  b+=i
}
return(b*b-a)
}

sumSquareDifference(100);