char_dict = {}
left = 0
max_len = 0

for right in range(len(s)):
  if s[right] not in char_dict:
    char_dict[s[right]] = 1
  else:
    char_dict[s[right]] += 1
  
  while len(char_dict) > k:
    char_dict[s[left]] -=1
    if char_dict[s[left]] == 0:
      del char_dict[s[left]] 
    left += 1
  
  max_len = max(max_len, right - left + 1)

print(max_len)