# 0x04-utf8_validation

Write a method that determines if a given data set represents a valid UTF-8 encoding.
```
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
```


A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

### Workings

This method works by first checking if the data is empty. If it is, then it is not a valid UTF-8 encoding. Next, the method checks if the first byte of the data is a valid UTF-8 start byte. If it is not, then the data is not a valid UTF-8 encoding. Finally, the method checks if the remaining bytes of the data are valid UTF-8 continuation bytes. If any of the remaining bytes are not valid UTF-8 continuation bytes, then the data is not a valid UTF-8 encoding. If all of the bytes in the data are valid UTF-8 start bytes and continuation bytes, then the data is a valid UTF-8 encoding.
