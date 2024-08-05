def largestValue(datas):
  largest=datas[0]
  for number in datas: 
    if number>largest:
      largest=number;

  return largest
