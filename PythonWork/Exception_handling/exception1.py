try:
    file=open('read.txt','r')
except IOError as e:
    print('An error occured.{}'.format(e.args[-1]))


#
# try:
#     file=open('read.txt','w')
# except EOFError as e:
#     print('An EOF error occured.')
#     raise e
# except IOError as e:
#     print('An error occurd')
#     raise e