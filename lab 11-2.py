def fileopen(data):
  with open(data, 'r', encoding='UTF8') as file:
    text = file.read()

    spount_character(data):
  count = 0

  for i in data:
    count += len(i)

  return count


data, count = fileopen("Lab11-2_sample.txt")

print("공백 수 : ", count - 1)

print("공백을 제외한 문자수 : ", count_character(data))

print("공백을 포함한 문자수 : ", count_character(data) + count - 1)

print("단어 수 : ", count)litdata = text.split()

  return splitdata, len(splitdata)


def c
