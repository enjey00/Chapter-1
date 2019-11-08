def biggest_guy(num1, num2, num3):
    if num2 < num1 > num3:
      return num1
    elif num1 < num2 > num3:
      return num2
    else:
      return num3

def test_biggest_guy():
  try:
      assert biggest_guy(1, 3, 2) == 3
      assert biggest_guy(30, 10, 20) == 30
      assert biggest_guy(20, 10, 30) == 30
      assert biggest_guy(2, 1, 9) == 9
      assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'
      print("Correct buddy!!!")
  except (AssertionError) as e:
      print(e)
      print("Wrong!!")

#test your code by un-commenting the line(s) below
test_biggest_guy()