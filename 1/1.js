function multiplesOf3and5(number) {

  let ans=0
  for (let i = 0; i < number; i++) {
    if(i%3==0 || i%5==0)
      ans+=i;
} 
  console.log(ans)
  return ans
}

multiplesOf3and5(10);