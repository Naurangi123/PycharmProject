def cheaper(string,k)->str:
    enc = ""
    for i in string:
        if ord(i) > 64 and ord(i) < 91 or ord(i) > 96 and ord(i) < 123:
            enc += chr(ord(i)+k)
            if(ord(i) + k > 90):
                rot = ord(i) + k - 90
                enc += chr(64 + rot)
            elif ord(i) + k > 122:
                rot = ord(i) + k - 122
                enc += chr(96 + rot)
        else:
            enc += i
    return enc

if __name__ == '__main__':
    print(cheaper("abcdefghijklmnopqrsuvwxyz",4)) 