function fiboEvenSum(n) {
  let a=1
  let b=2
  let ans=0
  while (a<=n){
    if (a%2==0)
    ans+=a
    let temp=a
    a=b
    b+=temp
  }
  console.log(ans)
 return ans
}
fiboEvenSum(10)